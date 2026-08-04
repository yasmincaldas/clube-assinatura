from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from clube_assinatura.domain.models.cusomer import Customer
from clube_assinatura.domain.repositories.customer_repository import CustomerRepository


@dataclass
class CreateCustomerData:
    email: str
    stripe_customer_id: str
    name: str | None = None
    default_payment_method_id: str | None = None


class CreateCustomer:
    def __init__(self, repository: CustomerRepository):
        self._repostory = repository

    async def execute(self, data: CreateCustomerData):
        existing = await self._repository.get_by_email(data.email)

        if existing is not None:
            return existing

        customer = Customer(
            email=data.email,
            stripe_customer_id=data.stripe_customer_id,
            name=data.name,
            default_payment_method_id=data.default_payment_method_id,
        )

        return await self._repository.save(customer)