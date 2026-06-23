from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.plan import Plan


class PlanRepository(ABC):
    """Interface de repositório para a entidade ``Plan``.

    Define o contrato de persistência dos planos de assinatura,
    abstraindo o mecanismo de armazenamento subjacente.
    """

    @abstractmethod
    async def get_by_id(self, plan_id: UUID) -> Plan | None:
        """Recupera um plano pelo seu identificador único."""
        ...

    @abstractmethod
    async def get_by_stripe_price_id(
        self, stripe_price_id: str
    ) -> Plan | None:
        """Recupera um plano pelo ID de preço do Stripe."""
        ...

    @abstractmethod
    async def get_by_stripe_product_id(
        self, stripe_product_id: str
    ) -> Plan | None:
        """Recupera um plano pelo ID de produto do Stripe."""
        ...

    @abstractmethod
    async def list_all(self) -> list[Plan]:
        """Lista todos os planos disponíveis."""
        ...

    @abstractmethod
    async def save(self, plan: Plan) -> Plan:
        """Persiste um plano (criação ou atualização)."""
        ...

    @abstractmethod
    async def delete(self, plan_id: UUID) -> None:
        """Remove um plano pelo seu identificador único."""
        ...
