from .adyen_authorizer import AdyenAuthorizer
from .adyen_refund_processor import AdyenRefundProcessor
from .adyen_webhook_verifier import AdyenWebhookVerifier
from .stripe_authorizer import StripeAuthorizer
from .stripe_refund_processor import StripeRefundProcessor
from .stripe_webhook_verifier import StripeWebhookVerifier


class CheckoutService:
    def __init__(self, provider: str):
        self.authorizer = None
        self.refunds = None
        self.webhooks = None
        self._build_integration(provider)

    def _build_integration(self, provider: str) -> None:
        if provider == "stripe":
            self.authorizer = StripeAuthorizer()
            self.refunds = StripeRefundProcessor()
            self.webhooks = StripeWebhookVerifier()
        elif provider == "adyen":
            self.authorizer = AdyenAuthorizer()
            self.refunds = AdyenRefundProcessor()
            self.webhooks = AdyenWebhookVerifier()
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def authorize_payment(self, amount: float) -> str:
        return self.authorizer.authorize(amount)

    def refund_payment(self, amount: float) -> str:
        return self.refunds.refund(amount)

    def verify_webhook(self, signature: str) -> bool:
        return self.webhooks.verify(signature)
