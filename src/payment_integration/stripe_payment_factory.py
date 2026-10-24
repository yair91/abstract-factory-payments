from .stripe_authorizer import StripeAuthorizer
from .stripe_refund_processor import StripeRefundProcessor
from .stripe_webhook_verifier import StripeWebhookVerifier
from .payment_authorizer import PaymentAuthorizer
from .payment_provider_factory import PaymentProviderFactory
from .refund_processor import RefundProcessor
from .webhook_verifier import WebhookVerifier


class StripePaymentFactory(PaymentProviderFactory):
    def create_authorizer(self) -> PaymentAuthorizer:
        return StripeAuthorizer()

    def create_refund_processor(self) -> RefundProcessor:
        return StripeRefundProcessor()

    def create_webhook_verifier(self) -> WebhookVerifier:
        return StripeWebhookVerifier()
