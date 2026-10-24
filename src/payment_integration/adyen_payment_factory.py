from .adyen_authorizer import AdyenAuthorizer
from .adyen_refund_processor import AdyenRefundProcessor
from .adyen_webhook_verifier import AdyenWebhookVerifier
from .payment_authorizer import PaymentAuthorizer
from .payment_provider_factory import PaymentProviderFactory
from .refund_processor import RefundProcessor
from .webhook_verifier import WebhookVerifier


class AdyenPaymentFactory(PaymentProviderFactory):
    def create_authorizer(self) -> PaymentAuthorizer:
        return AdyenAuthorizer()

    def create_refund_processor(self) -> RefundProcessor:
        return AdyenRefundProcessor()

    def create_webhook_verifier(self) -> WebhookVerifier:
        return AdyenWebhookVerifier()
