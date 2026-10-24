import inspect

from fake_payment_factory import FakePaymentFactory
from payment_integration import checkout_service
from payment_integration.adyen_payment_factory import AdyenPaymentFactory
from payment_integration.checkout_service import CheckoutService
from payment_integration.mercado_pago_payment_factory import MercadoPagoPaymentFactory
from payment_integration.stripe_payment_factory import StripePaymentFactory


def test_stripe_family_is_selected_together():
    checkout = CheckoutService(StripePaymentFactory())

    assert checkout.authorize_payment(125.50) == "stripe:authorized:125.50"
    assert checkout.refund_payment(25.00) == "stripe:refunded:25.00"
    assert checkout.verify_webhook("stripe-valid") is True
    assert checkout.verify_webhook("adyen-valid") is False


def test_adyen_family_is_selected_together():
    checkout = CheckoutService(AdyenPaymentFactory())

    assert checkout.authorize_payment(125.50) == "adyen:authorized:125.50"
    assert checkout.refund_payment(25.00) == "adyen:refunded:25.00"
    assert checkout.verify_webhook("adyen-valid") is True
    assert checkout.verify_webhook("stripe-valid") is False


def test_mercado_pago_family_is_selected_together():
    checkout = CheckoutService(MercadoPagoPaymentFactory())

    assert checkout.authorize_payment(125.50) == "mercadopago:authorized:125.50"
    assert checkout.refund_payment(25.00) == "mercadopago:refunded:25.00"
    assert checkout.verify_webhook("mercadopago-valid") is True
    assert checkout.verify_webhook("stripe-valid") is False


def test_checkout_works_with_any_factory_that_honors_the_contract():
    factory = FakePaymentFactory()
    checkout = CheckoutService(factory)

    assert factory.calls == ["authorizer", "refund_processor", "webhook_verifier"]
    assert checkout.authorize_payment(10) == "fake:authorized:10.00"
    assert checkout.refund_payment(5) == "fake:refunded:5.00"
    assert checkout.verify_webhook("fake-valid") is True


def test_checkout_does_not_reference_provider_specific_classes():
    source = inspect.getsource(checkout_service).lower()

    for provider in ("stripe", "adyen", "mercado"):
        assert provider not in source
