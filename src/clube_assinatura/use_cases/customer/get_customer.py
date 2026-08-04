from uuid import UUID

from clube_assinatura.domain.models.cusomer import Customer
from clube_assinatura.domain.repositories.customer_repository import CustomerRepository


class GetCustomer:
    """Busca um cliente."""
    def __init__(self, repository: CustomerRepository):
        self._repository = repository

    async def by_id(self, customer_id: UUID):
        return await self._repository.get_by_id(customer_id)

    async def get_by_stripe_customer_id(self, stripe_customer_id: str):
        return await self._repository.get_by_stripe_customer_id(stripe_customer_id)

    async def get_by_email(self, email: str):
        return await self._repository.get_by_email(email)