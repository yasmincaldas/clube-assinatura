from sqlalchemy.orm import Mapped, mapped_column
import uuid
from sqlalchemy import String, Integer, Boolean

from .base import Base


class Plan(Base):
    __tablename__='plans'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    stripe_price_id: Mapped(str) = mapped_column(String)
 
