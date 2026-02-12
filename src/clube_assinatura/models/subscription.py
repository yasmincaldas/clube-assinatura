from sqlalchemy.orm import Mapped, mapped_column
import uuid
from sqlalchemy import String, Integer, Boolean

from .base import Base


class Subscription(Base):
    """
    Representa uma assinatura.
    """
    __tablename__= 'subscriptions'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

