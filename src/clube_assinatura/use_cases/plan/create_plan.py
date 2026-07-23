from dataclasses import dataclass

from clube_assinatura.domain.models.plan import Plan
from clube_assinatura.domain.repositories.plan_repository import PlanRepository


@dataclass
class CreatePlanData:
    name: str
    description: str
    price: int
    currency: str
    interval: str
    stripe_product_id: str
    stripe_price_id: str


class CreatePlan:
    """Cria um novo plano de assinatura a partir de um evento webhook do Stripe."""

    def __init__(self, repository: PlanRepository):
        self._repository = repository

    async def execute(self, data: CreatePlanData):
        plan = Plan(
            name=data.name,
            description=data.description,
            price=data.price,
            currency=data.currency,
            interval=dataput.interval,
            stripe_product_id=data.stripe_product_id,
            stripe_price_id=data.stripe_price_id,
        )
        return await self._repository.save(plan)