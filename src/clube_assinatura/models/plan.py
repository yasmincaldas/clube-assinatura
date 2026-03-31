import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean, relationship

from .base import Base, User
from .plan import Plan


class Plan(Base):
    """
    Representa um plano de assinatura.
    """
    __tablename__ = 'plans'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer, nullable=False)  
    currency: Mapped[str] = mapped_column(String, default='brl')
    interval: Mapped[str] = mapped_column(String, nullable=False) 
    
    stripe_product_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    stripe_price_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    
    subscriptions: Mapped[list["Subscription"]] = relationship(
        back_populates="plan",
        cascade="all, delete-orphan"
    )