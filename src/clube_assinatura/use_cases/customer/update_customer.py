from dataclasses import dataclass
from uuid import UUID

from clube_assinatura.domain.models.customer import Customer
from clube_assinatura.domain.repositories.customer_repository import CustomerRepository


@dataclass
class UpdateCustomerData:
    customer_id: UUID
    name: str | None = None
    default_payment_method_id: str | None = None


class UpdateCustomer:
    """Atualiza os dados de um cliente existente."""

    def __init__(self, repository: CustomerRepository):
        self._repository = repository

    async def execute(self, data: UpdateCustomerData):
        customer = await self._repository.get_by_id(data.customer_id)

        if customer is None:
            return None

        if data.name is not None:
            customer.name = data.name
        if data.default_payment_method_id is not None:
            customer.default_payment_method_id = data.default_payment_method_id

        return await self._repository.save(customer)