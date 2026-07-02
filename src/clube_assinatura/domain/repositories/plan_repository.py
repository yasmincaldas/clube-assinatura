from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.plan import Plan


class PlanRepository(ABC):
    """Contrato de persistência para a entidade Plan."""

    @abstractmethod
    async def get_by_id(self, plan_id: UUID) -> Plan | None:
        """Busca um plano pelo UUID interno."""
        ...

    @abstractmethod
    async def get_by_stripe_price_id(
        self, stripe_price_id: str
    ) -> Plan | None:
        """Busca um plano pelo ID de preço do Stripe."""
        ...

    @abstractmethod
    async def get_by_stripe_product_id(
        self, stripe_product_id: str
    ) -> Plan | None:
        """Busca um plano pelo ID de produto do Stripe."""
        ...

    @abstractmethod
    async def list_all(self) -> list[Plan]:
        """Retorna todos os planos cadastrados."""
        ...

    @abstractmethod
    async def save(self, plan: Plan) -> Plan:
        """Persiste um plano."""
        ...

    @abstractmethod
    async def delete(self, plan_id: UUID) -> None:
        """Remove um plano pelo UUID. """
        ...