from dataclasses import dataclass
from uuid import UUID

from clube_assinatura.domain.models.plan import Plan
from clube_assinatura.domain.repositories.plan_repository import PlanRepository


@dataclass
class UpdatePlanData:
    stripe_product_id: str
    name: str | None = None
    description: str | None = None
    price: int | None = None
    interval: str | None = None


class UpdatePlan:
    """Atualiza um plano a partir de um evento webhook do Stripe."""

    def __init__(self, repository: PlanRepository):
        self._repository = repository

    async def execute(self, data: UpdatePlanData):
        plan = await self._repository.get_by_stripe_product_id(data.stripe_product_id)

        if plan is None:
            return None

        if data.name is not None:
            plan.name = data.name
        if data.description is not None:
            plan.description = data.description
        if data.price is not None:
            plan.price = data.price
        if data.interval is not None:
            plan.interval = data.interval

        return await self._repository.save(plan)