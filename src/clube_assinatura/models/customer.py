# models/customer.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, JSON, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from typing import Optional, List

from .base import Base

class Customer(Base):
    """
    Representa um cliente.
    """
    __tablename__ = "customers"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)

    stripe_customer_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    email: Mapped[str] = mapped_column(String, nullable=False, index=True)
    name: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    default_payment_method_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    stripe_subscription_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    
    user: Mapped["User"] = relationship(back_populates="customer")
    payments: Mapped[List["Payment"]] = relationship(back_populates="customer")

