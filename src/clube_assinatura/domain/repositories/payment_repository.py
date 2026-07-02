from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.payment import Payment


class IPaymentRepository(ABC):
    """Contrato de persistência para a entidade Payment."""

    @abstractmethod
    async def get_by_id(self, payment_id: UUID) -> Payment | None:
        """Busca um pagamento pelo UUID interno."""
        ...

    @abstractmethod
    async def get_by_subscription_id(self, subscription_id: UUID) -> list[Payment]:
        """Retorna todos os pagamentos de uma assinatura."""
        ...

    @abstractmethod
    async def get_by_stripe_invoice_id(self, invoice_id: str) -> Payment | None:
        """Busca um pagamento pelo ID de invoice do Stripe."""
        ...

    @abstractmethod
    async def get_by_stripe_payment_intent_id(self, payment_intent_id: str) -> Payment | None:
        """Busca um pagamento pelo ID de PaymentIntent do Stripe."""
        ...

    @abstractmethod
    async def save(self, payment: Payment) -> Payment:
        """Persiste um pagamento novo ou atualiza um existente."""
        ...