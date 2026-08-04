from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum
from datetime import datetime

from .base import Base


class SubscriptionStatus(enum.Enum):
    INCOMPLETE = 'incomplete'
    INCOMPLETE_EXPIRED = 'incomplete_expired'
    TRIALING = 'trialing'
    ACTIVE = 'active'
    PAST_DUE = 'past_due'
    CANCELED = 'canceled'
    UNPAID = 'unpaid'


class Subscription(Base):
    """Representa uma assinatura."""

    __tablename__ = 'subscriptions'

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    stripe_subscription_id: Mapped[str] = mapped_column(
        String, unique=True, nullable=False
    )
    status: Mapped[SubscriptionStatus] = mapped_column(
        Enum(SubscriptionStatus), nullable=False
    )

    current_period_start: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    current_period_end: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    cancel_at_period_end: Mapped[bool] = mapped_column(Boolean, default=False)

    customer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('customers.id'), nullable=False
    )
    plan_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey('plans.id'), nullable=False
    )

    customer: Mapped['Customer'] = relationship(back_populates='subscriptions')
    plan: Mapped['Plan'] = relationship(back_populates='subscriptions')
    payments: Mapped[list['Payment']] = relationship(back_populates='subscription')