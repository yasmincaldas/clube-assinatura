from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.payment import Payment


class PaymentRepository(ABC):
    @abstractmethod
    async def get_by_id(self, payment_id: UUID) -> Payment | None: ...

    @abstractmethod
    async def get_by_subscription_id(
        self, subscription_id: UUID
    ) -> list[Payment]: ...

    @abstractmethod
    async def get_by_stripe_payment_intent_id(
        self, payment_intent_id: str
    ) -> Payment | None: ...

    @abstractmethod
    async def save(self, payment: Payment) -> Payment: ...
