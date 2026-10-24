import pytest

from fake_payment_factory import FakePaymentFactory
from payment_integration.payment_app import PaymentApp
from payment_integration.payment_provider_selector import PaymentProviderSelector


@pytest.mark.parametrize(
    "provider, expected",
    [
        ("stripe", "stripe:authorized:50.00"),
        ("adyen", "adyen:authorized:50.00"),
        ("mercado_pago", "mercadopago:authorized:50.00"),
    ],
)
def test_app_builds_checkout_for_configured_provider(provider, expected):
    checkout = PaymentApp().build_checkout(provider)

    assert checkout.authorize_payment(50) == expected


def test_unsupported_provider_is_rejected():
    with pytest.raises(ValueError):
        PaymentApp().build_checkout("paypal")


def test_selector_accepts_injected_factories():
    fake = FakePaymentFactory()
    app = PaymentApp(PaymentProviderSelector({"fake": fake}))

    assert app.build_checkout("fake").verify_webhook("fake-valid") is True
