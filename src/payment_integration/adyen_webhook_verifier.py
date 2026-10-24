class AdyenWebhookVerifier:
    def verify(self, signature: str) -> bool:
        return signature == "adyen-valid"
