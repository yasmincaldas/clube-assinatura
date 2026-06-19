from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.customer import Customer


class CustomerRepository(ABC):
    @abstractmethod
    async def get_by_id(self, customer_id: UUID) -> Customer | None: ...

    @abstractmethod
    async def get_by_email(self, email: str) -> Customer | None: ...

    @abstractmethod
    async def get_by_stripe_customer_id(
        self, stripe_customer_id: str
    ) -> Customer | None: ...

    @abstractmethod
    async def save(self, customer: Customer) -> Customer: ...

    @abstractmethod
    async def delete(self, customer_id: UUID) -> None: ...
