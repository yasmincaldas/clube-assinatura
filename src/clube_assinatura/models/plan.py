import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean, relationship

from .base import Base, User
from .plan import Plan


class Plan(Base):
    """
    Representa um plano de assinatura.
    """
    __tablename__='plans'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    currency = Mapped[str] = mapped_column(String, default='brl')
    interval = Mapped[str] = mapped_column(String)

    stripe_product_id: Mapped(str) = mapped_column(String)
    stripe_price_id: Mapped(str) = mapped_column(String)
 
    subscriptions: Mapped[list["Subscription"]] = relationship(
        back_populates="plan"
    )
