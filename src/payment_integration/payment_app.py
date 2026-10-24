from typing import Optional

from .adyen_payment_factory import AdyenPaymentFactory
from .checkout_service import CheckoutService
from .mercado_pago_payment_factory import MercadoPagoPaymentFactory
from .payment_provider_selector import PaymentProviderSelector
from .stripe_payment_factory import StripePaymentFactory


class PaymentApp:
    """Composition root: the only place that knows the concrete provider families."""

    def __init__(self, selector: Optional[PaymentProviderSelector] = None):
        self._selector = selector or PaymentProviderSelector(
            {
                "stripe": StripePaymentFactory(),
                "adyen": AdyenPaymentFactory(),
                "mercado_pago": MercadoPagoPaymentFactory(),
            }
        )

    def build_checkout(self, provider: str) -> CheckoutService:
        return CheckoutService(self._selector.select(provider))
