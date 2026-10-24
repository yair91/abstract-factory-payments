class StripeWebhookVerifier:
    def verify(self, signature: str) -> bool:
        return signature == "stripe-valid"
