from .mercado_pago_authorizer import MercadoPagoAuthorizer
from .mercado_pago_refund_processor import MercadoPagoRefundProcessor
from .mercado_pago_webhook_verifier import MercadoPagoWebhookVerifier
from .payment_authorizer import PaymentAuthorizer
from .payment_provider_factory import PaymentProviderFactory
from .refund_processor import RefundProcessor
from .webhook_verifier import WebhookVerifier


class MercadoPagoPaymentFactory(PaymentProviderFactory):
    def create_authorizer(self) -> PaymentAuthorizer:
        return MercadoPagoAuthorizer()

    def create_refund_processor(self) -> RefundProcessor:
        return MercadoPagoRefundProcessor()

    def create_webhook_verifier(self) -> WebhookVerifier:
        return MercadoPagoWebhookVerifier()
