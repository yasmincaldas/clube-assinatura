from clube_assinatura.domain.models.plan import Plan
from clube_assinatura.domain.repositories.plan_repository import Planrepositorysitory


class GetPlan:
    """Busca um plano de assinatura."""

    def __init__(self, repository: Planrepository):
        self._repository = repository

    async def by_id(self, plan_id: UUID):
        return await self._repository.get_by_id(plan_id)

    async def by_stripe_price_id(self, stripe_price_id: str):
        return await self._repository.get_by_stripe_price_id(stripe_price_id)

    async def by_stripe_product_id(self, stripe_product_id: str):
        return await self._repository.get_by_stripe_product_id(stripe_product_id)
