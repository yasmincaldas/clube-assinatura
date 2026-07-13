from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from clube_assinatura.domain.models.payment import Payment
from clube_assinatura.domain.repositories.payment_repository import PaymentRepository


class PaymentRepositorySQL(PaymentRepository):
    """Implementa SQLAlchemy para PaymentRepository."""
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, payment_id:UUID):
        result = await self.session.execute(
            select(Payment).where(Payment.id == payment_id)
        )

        return result.scalar_one_or_none()

    async def get_by_subscription_id(self, subscription_id: UUID):
        result = await self.session.execute(
            select(Payment).where(Payment.subscription_id == subscription_id)
        )
        return list(result.scalars().all())

    async def get_by_stripe_invoice_id(self, invoice_id: str):
        result = await self.session.execute(
            select(Payment).where(Payment.stripe_invoice_id == invoice_id)
        )
        return result.scalar_one_or_none()

    async def get_by_stripe_payment_intent_id(self, payment_intent_id: str):
        result = await self.session.execute(
            select(Payment).where(Payment.stripe_payment_intent_id == payment_intent_id)
        )
        return result.scalar_one_or_none()

    async def save(self, payment: Payment):
        self.session.add(payment)
        await self.session.flush()
        await self.session.refresh(payment)
        return payment
