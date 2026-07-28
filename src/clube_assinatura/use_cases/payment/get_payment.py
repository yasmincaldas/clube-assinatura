from uuid import UUID

from clube_assinatura.domain.models.payment import Payment
from clube_assinatura.domain.repositories.payment_repository import PaymentRepository


class GetPayment:
    """Busca um pagamento."""

    def __init__(self, repository: PaymentRepository):
        self._repository = repository

    async def by_id(self, payment_id: UUID):
        return await self._repository.get_by_id(payment_id)

    async def by_stripe_invoice_id(self, stripe_invoice_id: str):
        return await self._repository.get_by_stripe_invoice_id(stripe_invoice_id)