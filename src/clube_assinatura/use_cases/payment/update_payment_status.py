from dataclasses import dataclass

from clube_assinatura.domain.models.payment import PaymentStatus
from clube_assinatura.domain.repositories.payment_repository import PaymentRepository


@dataclass
class UpdatePaymentStatusData:
    stripe_invoice_id: str
    status: PaymentStatus


class UpdatePaymentStatus:
    """Atualiza o status de um pagamento a partir de webhooks do Stripe.
    
    Acionado pelos eventos invoice.payment_failed e charge.refunded.
    """

    def __init__(self, repository: PaymentRepository):
        self._repository = repository

    async def execute(self, data: UpdatePaymentStatusData):
        payment = await self._repository.get_by_stripe_invoice_id(
            data.stripe_invoice_id
        )

        if payment is None:
            return

        payment.status = data.status
        await self._repository.save(payment)