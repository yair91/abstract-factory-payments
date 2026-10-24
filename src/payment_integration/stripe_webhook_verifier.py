from .webhook_verifier import WebhookVerifier


class StripeWebhookVerifier(WebhookVerifier):
    def verify(self, signature: str) -> bool:
        return signature == "stripe-valid"
