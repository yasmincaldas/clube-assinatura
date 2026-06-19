from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.plan import Plan


class PlanRepository(ABC):
    @abstractmethod
    async def get_by_id(self, plan_id: UUID) -> Plan | None: ...

    @abstractmethod
    async def get_by_stripe_price_id(
        self, stripe_price_id: str
    ) -> Plan | None: ...

    @abstractmethod
    async def get_by_stripe_product_id(
        self, stripe_product_id: str
    ) -> Plan | None: ...

    @abstractmethod
    async def list_all(self) -> list[Plan]: ...

    @abstractmethod
    async def save(self, plan: Plan) -> Plan: ...

    @abstractmethod
    async def delete(self, plan_id: UUID) -> None: ...
