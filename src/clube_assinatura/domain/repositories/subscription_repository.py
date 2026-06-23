from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.subscription import Subscription


class SubscriptionRepository(ABC):
    """Interface de repositório para a entidade ``Subscription``.

    Define o contrato de persistência das assinaturas,
    abstraindo o mecanismo de armazenamento subjacente.
    """

    @abstractmethod
    async def get_by_id(self, subscription_id: UUID) -> Subscription | None:
        """Recupera uma assinatura pelo seu identificador único."""
        ...

    @abstractmethod
    async def get_by_user_id(self, customer_id: UUID) -> list[Subscription]:
        """Recupera todas as assinaturas vinculadas a um cliente."""
        ...

    @abstractmethod
    async def get_by_stripe_subscription_id(
        self, stripe_subscription_id: str
    ) -> Subscription | None:
        """Recupera uma assinatura pelo ID de assinatura do Stripe."""
        ...

    @abstractmethod
    async def save(self, subscription: Subscription) -> Subscription:
        """Persiste uma assinatura (criação ou atualização)."""
        ...

    @abstractmethod
    async def update_status(self, subscription_id: UUID, status: str) -> None:
        """Atualiza o status de uma assinatura existente."""
        ...
