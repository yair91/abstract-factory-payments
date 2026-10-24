from .payment_provider_factory import PaymentProviderFactory


class PaymentProviderSelector:
    """Composition root helper: maps a configured provider name to its factory."""

    def __init__(self, factories: dict[str, PaymentProviderFactory]):
        self._factories = dict(factories)

    def select(self, provider: str) -> PaymentProviderFactory:
        if provider not in self._factories:
            raise ValueError(f"Unsupported provider: {provider}")
        return self._factories[provider]
