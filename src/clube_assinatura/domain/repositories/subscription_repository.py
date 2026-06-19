from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.subscription import Subscription


class SubscriptionRepository(ABC):
    @abstractmethod
    async def get_by_id(
        self, subscription_id: UUID
    ) -> Subscription | None: ...

    @abstractmethod
    async def get_by_user_id(
        self, customer_id: UUID
    ) -> list[Subscription]: ...

    @abstractmethod
    async def get_by_stripe_subscription_id(
        self, stripe_subscription_id: str
    ) -> Subscription | None: ...

    @abstractmethod
    async def save(self, subscription: Subscription) -> Subscription: ...

    @abstractmethod
    async def update_status(
        self, subscription_id: UUID, status: str
    ) -> None: ...
