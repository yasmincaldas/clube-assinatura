from dataclasses import dataclass

from clube_assinatura.domain.repositories.plan_repository import PlanRepository


@dataclass
class DeletePlanData:
    stripe_product_id: str


class DeletePlan:
    """Remove um plano a partir de um evento webhook do Stripe."""

    def __init__(self, repo: PlanRepository):
        self._repository = repo

    async def execute(self, data: DeletePlanData):
        plan = await self._repository.get_by_stripe_product_id(data.stripe_product_id)

        if plan is None:
            return

        await self._repository.delete(plan.id)