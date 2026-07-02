from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.customer import Customer


class CustomerRepository(ABC):
    """Contrato de persistência para a entidade Customer."""

    @abstractmethod
    async def get_by_id(self, customer_id: UUID) -> Customer | None:
        """Busca um cliente pelo UUID interno."""
        ...

    @abstractmethod
    async def get_by_email(self, email: str) -> Customer | None:
        """Busca um cliente pelo e-mail."""
        ...

    @abstractmethod
    async def get_by_stripe_customer_id(
        self, stripe_customer_id: str
    ) -> Customer | None:
        """Busca um cliente pelo ID de cliente do Stripe (ex: cus_xxx)."""
        ...

    @abstractmethod
    async def save(self, customer: Customer) -> Customer:
        """Persiste um cliente novo ou atualiza um existente."""
        ...

    @abstractmethod
    async def delete(self, customer_id: UUID) -> None:
        """Remove um cliente pelo UUID. Silencioso se não existir."""
        ...