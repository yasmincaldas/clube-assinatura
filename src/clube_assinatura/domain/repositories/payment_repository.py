from abc import ABC, abstractmethod
from uuid import UUID

from clube_assinatura.domain.models.payment import Payment


class PaymentRepository(ABC):
    """Interface de repositório para a entidade ``Payment``.

    Define o contrato de persistência dos pagamentos,
    abstraindo o mecanismo de armazenamento subjacente.
    """

    @abstractmethod
    async def get_by_id(self, payment_id: UUID) -> Payment | None:
        """Recupera um pagamento pelo seu identificador único."""
        ...

    @abstractmethod
    async def get_by_subscription_id(
        self, subscription_id: UUID
    ) -> list[Payment]:
        """Recupera todos os pagamentos vinculados a uma assinatura."""
        ...

    @abstractmethod
    async def get_by_stripe_payment_intent_id(
        self, payment_intent_id: str
    ) -> Payment | None:
        """Recupera um pagamento pelo ID de Payment Intent do Stripe."""
        ...

    @abstractmethod
    async def save(self, payment: Payment) -> Payment:
        """Persiste um pagamento (criação ou atualização)."""
        ...
