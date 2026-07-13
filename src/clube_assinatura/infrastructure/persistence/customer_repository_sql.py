from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from clube_assinatura.domain.models.customer import Customer
from clube_assinatura.domain.repositories.customer_repository import CustomerRepository


class CustomerRepositorySQL(CustomerRepository):
    """Implementa SQLAlchemy para CustomerRepository."""
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, customer_id: UUID):
        result = await self.session.execute(
            select(Customer).where(Customer.id == customer_id)
        )

        return result.scalar_one_or_none()

    async def get_by_email(self, email: str):
        result = await self.session.execute(
            select(Customer).where(Customer.email == email)
        )

        return result.scalar_one_or_none()

    async def get_by_stripe_customer_id(self, stripe_customer_id: str):
        result = self.session.execute(
            select(Customer).where(Customer.stripe_customer_id == stripe_customer_id)
        )

        return result.scalar_one_or_none()

    async def save(self, customer: Customer):
        self.session.add(customer)
        await self.session.flush()
        await self.session.refresh(customer)
        return customer


    async def delete(self, customer_id: UUID): 
        customer = await self.get_by_id(customer_id)
        if customer:
            await self.session.delete(customer)
            await self.session.flush()





