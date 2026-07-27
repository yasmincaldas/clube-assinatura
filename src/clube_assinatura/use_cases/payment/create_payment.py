from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from clube_assinatura.domain.models.payment import Payment, PaymentStatus
from clube_assinatura.domain.repositories.payment_repository import PaymentRepository


@dataclass
class CreatePaymentData:
    subscription_id: UUID
    customer_id: UUID
    stripe_invoice_id: str
    stripe_payment_intent_id: str | None
    amount: int
    currency: str
    payment_date: datetime
    period_start: datetime | None
    period_end: datetime | None


class CreatePayment:
    """Registra um pagamento a partir do webhook invoice.paid do Stripe."""

    def __init__(self, repository: PaymentRepository):
        self._repository = repository

    async def execute(self, data: CreatePaymentData):
        existing = await self._repository.get_by_stripe_invoice_id(
            data.stripe_invoice_id
        )

        if existing is not None:
            return existing

        payment = Payment(
            subscription_id=data.subscription_id,
            customer_id=data.customer_id,
            stripe_invoice_id=data.stripe_invoice_id,
            stripe_payment_intent_id=data.stripe_payment_intent_id,
            amount=data.amount,
            currency=data.currency,
            status=PaymentStatus.SUCCEEDED,
            payment_date=data.payment_date,
            period_start=data.period_start,
            period_end=data.period_end,
        )

        return await self._repository.save(payment)