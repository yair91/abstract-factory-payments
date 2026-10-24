from .payment_authorizer import PaymentAuthorizer


class AdyenAuthorizer(PaymentAuthorizer):
    def authorize(self, amount: float) -> str:
        return f"adyen:authorized:{amount:.2f}"
