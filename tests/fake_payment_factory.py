from payment_integration.payment_authorizer import PaymentAuthorizer
from payment_integration.payment_provider_factory import PaymentProviderFactory
from payment_integration.refund_processor import RefundProcessor
from payment_integration.webhook_verifier import WebhookVerifier


class FakeAuthorizer(PaymentAuthorizer):
    def authorize(self, amount: float) -> str:
        return f"fake:authorized:{amount:.2f}"


class FakeRefundProcessor(RefundProcessor):
    def refund(self, amount: float) -> str:
        return f"fake:refunded:{amount:.2f}"


class FakeWebhookVerifier(WebhookVerifier):
    def verify(self, signature: str) -> bool:
        return signature == "fake-valid"


class FakePaymentFactory(PaymentProviderFactory):
    def __init__(self):
        self.calls = []

    def create_authorizer(self) -> PaymentAuthorizer:
        self.calls.append("authorizer")
        return FakeAuthorizer()

    def create_refund_processor(self) -> RefundProcessor:
        self.calls.append("refund_processor")
        return FakeRefundProcessor()

    def create_webhook_verifier(self) -> WebhookVerifier:
        self.calls.append("webhook_verifier")
        return FakeWebhookVerifier()
