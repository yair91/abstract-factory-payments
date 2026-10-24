from .webhook_verifier import WebhookVerifier


class AdyenWebhookVerifier(WebhookVerifier):
    def verify(self, signature: str) -> bool:
        return signature == "adyen-valid"
