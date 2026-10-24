import pytest

from payment_integration.adyen_payment_factory import AdyenPaymentFactory
from payment_integration.mercado_pago_payment_factory import MercadoPagoPaymentFactory
from payment_integration.payment_authorizer import PaymentAuthorizer
from payment_integration.payment_provider_factory import PaymentProviderFactory
from payment_integration.refund_processor import RefundProcessor
from payment_integration.stripe_payment_factory import StripePaymentFactory
from payment_integration.webhook_verifier import WebhookVerifier

FACTORIES = [
    (StripePaymentFactory, "stripe"),
    (AdyenPaymentFactory, "adyen"),
    (MercadoPagoPaymentFactory, "mercadopago"),
]


@pytest.mark.parametrize("factory_class, tag", FACTORIES)
def test_factory_creates_products_that_honor_each_contract(factory_class, tag):
    factory = factory_class()

    assert isinstance(factory, PaymentProviderFactory)
    assert isinstance(factory.create_authorizer(), PaymentAuthorizer)
    assert isinstance(factory.create_refund_processor(), RefundProcessor)
    assert isinstance(factory.create_webhook_verifier(), WebhookVerifier)


@pytest.mark.parametrize("factory_class, tag", FACTORIES)
def test_factory_products_belong_to_the_same_provider(factory_class, tag):
    factory = factory_class()

    assert factory.create_authorizer().authorize(1).startswith(f"{tag}:")
    assert factory.create_refund_processor().refund(1).startswith(f"{tag}:")
    assert factory.create_webhook_verifier().verify(f"{tag}-valid") is True


def test_factory_contract_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        PaymentProviderFactory()


def test_incomplete_family_is_rejected():
    class HalfFactory(PaymentProviderFactory):
        def create_authorizer(self):
            return None

    with pytest.raises(TypeError):
        HalfFactory()
