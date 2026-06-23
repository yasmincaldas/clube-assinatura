from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.customer import Customer


class CustomerRepository(ABC):
    """Interface de repositório para a entidade ``Customer``.

    Define o contrato de persistência dos clientes,
    abstraindo o mecanismo de armazenamento subjacente.
    """

    @abstractmethod
    async def get_by_id(self, customer_id: UUID) -> Customer | None:
        """Recupera um cliente pelo seu identificador único."""
        ...

    @abstractmethod
    async def get_by_email(self, email: str) -> Customer | None:
        """Recupera um cliente pelo endereço de e-mail."""
        ...

    @abstractmethod
    async def get_by_stripe_customer_id(
        self, stripe_customer_id: str
    ) -> Customer | None:
        """Recupera um cliente pelo ID de cliente do Stripe."""
        ...

    @abstractmethod
    async def save(self, customer: Customer) -> Customer:
        """Persiste um cliente (criação ou atualização)."""
        ...

    @abstractmethod
    async def delete(self, customer_id: UUID) -> None:
        """Remove um cliente pelo seu identificador único."""
        ...
