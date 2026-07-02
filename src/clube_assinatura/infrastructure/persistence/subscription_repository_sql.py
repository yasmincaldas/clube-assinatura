from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from clube_assinatura.domain.models.subscription import Subscription
from clube_assinatura.domain.repositories.subscription_repository import SubscriptionRepository


class SubscriptionRepositorySQL(SubscriptionRepository):
    """ Implementa SQLAlchemy para o SubscriptionRepository. """
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, subscription_id: UUID):
        result = await self.session.execute(
            select(Subscription).where(Subscription.id == subscription_id)
        )

        return result.scalar_one_or_none()

    async def get_by_user_id(self, user_id: int):
        result = await self.session.execute(
            select(Subscription).where(Subscription.user_id == user_id)
        )

        return result.scalar_one_or_none()

    async def get_by_stripe_subscription_id(self, stripe_subscription_id:str):
        result = await self.session.execute(
            select(Subscription).where(Subscription.stripe_subscription_id == stripe_subscription_id)
        )
        
        return result.scalar_one_or_none()

    async def save(self, subscription: Subscription):
        self.session.add(subscription)

        await self.session.flush()
        await self.session.refresh(subscription)
        return subscription

    async def delete(self, subscription_id:UUID):
        subscription = await self.get_by_id(subscription_id)

        if subscription:
            await self.session.delete(subscription)
            await self.session.flush()