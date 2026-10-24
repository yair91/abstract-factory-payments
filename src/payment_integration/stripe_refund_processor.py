class StripeRefundProcessor:
    def refund(self, amount: float) -> str:
        return f"stripe:refunded:{amount:.2f}"
