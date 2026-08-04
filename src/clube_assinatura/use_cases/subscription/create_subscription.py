from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from clube_assinatura.domain.models.subscription import Subscription, SubscriptionStatus
from clube_assinatura.domain.repositories.subscription_repository import SubscriptionRepository


@dataclass
class CreateSubscriptionData:
    customer_id: UUID
    plan_id: UUID
    stripe_subscription_id: str
    status: SubscriptionStatus
    current_period_start: datetime
    current_period_end: datetime
    cancel_at_period_end: bool = False


class CreateSubscription:
    """Registra uma nova assinatura a partir do webhook customer.subscription.created."""

    def __init__(self, repository: SubscriptionRepository):
        self._repository = repository

    async def execute(self, data: CreateSubscriptionData) -> Subscription:
        existing = await self._repository.get_by_stripe_subscription_id(
            data.stripe_subscription_id
        )

        if existing is not None:
            return existing

        subscription = Subscription(
            customer_id=data.customer_id,
            plan_id=data.plan_id,
            stripe_subscription_id=data.stripe_subscription_id,
            status=data.status,
            current_period_start=data.current_period_start,
            current_period_end=data.current_period_end,
            cancel_at_period_end=data.cancel_at_period_end,
        )

        return await self._repository.save(subscription)