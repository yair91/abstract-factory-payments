from .webhook_verifier import WebhookVerifier


class MercadoPagoWebhookVerifier(WebhookVerifier):
    def verify(self, signature: str) -> bool:
        return signature == "mercadopago-valid"
