from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from clube_assinatura.domain.models.plan import Plan
from clube_assinatura.domain.repositories.plan_repository import PlanRepository


class PlanRepositorySQL(PlanRepository):
    """Implementa SQLAlchemy para o PlanRepository."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, plan_id: UUID):
        result = await self.session.execute(
            select(Plan).where(Plan.id == plan_id)
        )
        return result.scalar_one_or_none()

    async def get_by_stripe_price_id(
        self, stripe_price_id: str
    ) -> Plan | None:
        result = await self.session.execute(
            select(Plan).where(Plan.stripe_price_id == stripe_price_id)
        )
        return result.scalar_one_or_none()

    async def get_by_stripe_product_id(
        self, stripe_product_id: str
    ) -> Plan | None:
        result = await self.session.execute(
            select(Plan).where(Plan.stripe_product_id == stripe_product_id)
        )
        return result.scalar_one_or_none()

    async def list_all(self):
        result = await self.session.execute(select(Plan))
        return list(result.scalars().all())

    async def save(self, plan: Plan):
        self.session.add(plan)
        await self.session.flush()
        await self.session.refresh(plan)
        return plan

    async def delete(self, plan_id: UUID):
        plan = await self.get_by_id(plan_id)
        if plan:
            await self.session.delete(plan)
            await self.session.flush()
