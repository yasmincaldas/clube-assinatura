from sqlalchemy.orm import Mapped, mapped_column
import uuid
from sqlalchemy import String, Integer, Boolean, ForeignKey

from .base import Base
import enum
import datetime

class SubscriptionStatus(enum.Enum):
    ACTIVE = "active"
    CANCELED = "canceled"
    PAST_DUE = "past_due"
    UNPAID = "unpaid"


class Subscription(Base):
    """
    Representa uma assinatura.
    """
    __tablename__= 'subscriptions'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    status: Mapped[SubscriptionStatus] = mapped_column(Enum(SubscriptionStatus))
    stripe_subscription_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    current_period_start: Mapped[datetime]
    current_period_end: Mapped[datetime]
    cancel_at_period_end: Mapped[bool] = mapped_column(Boolean, default=False)

    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    plan_id: Mapped[UUID] = mapped_column(ForeignKey("plans.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="subscriptions")
    plan: Mapped["Plan"] = relationship(back_populates="subscriptions")
