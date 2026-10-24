from .payment_authorizer import PaymentAuthorizer


class StripeAuthorizer(PaymentAuthorizer):
    def authorize(self, amount: float) -> str:
        return f"stripe:authorized:{amount:.2f}"
