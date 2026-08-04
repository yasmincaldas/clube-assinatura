from uuid import UUID

from clube_assinatura.domain.repositories.customer_repository import CustomerRepository


class DeleteCustomer:
    """Remove um cliente existente."""

    def __init__(self, repository: CustomerRepository):
        self._repository = repository

    async def execute(self, customer_id: UUID):
        customer = await self._repository.get_by_id(customer_id)

        if customer is None:
            return

        await self._repository.delete(customer_id)