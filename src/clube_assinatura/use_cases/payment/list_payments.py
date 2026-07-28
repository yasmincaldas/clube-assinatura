from uuid import UUID

from clube_assinatura.domain.models.payment import Payment
from clube_assinatura.domain.repositories.payment_repository import PaymentRepository


class ListPayments:
    """Lista pagamentos de uma assinatura."""

    def __init__(self, repository: PaymentRepository):
        self._repository = repository

    async def by_subscription_id(self, subscription_id: UUID):
        return await self._repository.get_by_subscription_id(subscription_id)