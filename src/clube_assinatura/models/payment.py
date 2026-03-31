from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Integer, Enum  
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from typing import Optional
import enum

from .base import Base

class PaymentStatus(enum.Enum):
    """
    Possíveis status de pagamento.
    """
    SUCCEEDED = "succeeded"
    PENDING = "pending"
    FAILED = "failed"
    REFUNDED = "refunded"


class Payment(Base):
    """
    Representa um pagamento de uma assinatura.
    """
    __tablename__ = "payments"
    
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    subscription_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("subscriptions.id"), nullable=False)
    customer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("customers.id"), nullable=False)
    
    stripe_invoice_id: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    stripe_payment_intent_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    
    amount: Mapped[int] = mapped_column(Integer, nullable=False) 
    currency: Mapped[str] = mapped_column(String, default="BRL", nullable=False)
    status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus), default=PaymentStatus.SUCCEEDED)
    
    payment_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    period_start: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    period_end: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
        
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    subscription: Mapped["Subscription"] = relationship(back_populates="payments")
    customer: Mapped["Customer"] = relationship(back_populates="payments")
    

