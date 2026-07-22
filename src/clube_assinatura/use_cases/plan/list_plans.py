from clube_assinatura.domain.models.plan import Plan
from clube_assinatura.domain.repositories.plan_repository import PlanRepository


class ListPlans:
    """Lista todos os planos."""

    def __init__(self, repository: PlanRepository):
        self._repository = repository

    async def execute(self):
        return await self._repository.list_all()