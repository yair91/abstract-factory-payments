class AdyenRefundProcessor:
    def refund(self, amount: float) -> str:
        return f"adyen:refunded:{amount:.2f}"
