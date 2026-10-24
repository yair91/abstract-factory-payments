from abc import ABC, abstractmethod

from .payment_authorizer import PaymentAuthorizer
from .refund_processor import RefundProcessor
from .webhook_verifier import WebhookVerifier


class PaymentProviderFactory(ABC):
    """Creates every capability of one payment provider, so they always match."""

    @abstractmethod
    def create_authorizer(self) -> PaymentAuthorizer:
        raise NotImplementedError

    @abstractmethod
    def create_refund_processor(self) -> RefundProcessor:
        raise NotImplementedError

    @abstractmethod
    def create_webhook_verifier(self) -> WebhookVerifier:
        raise NotImplementedError
