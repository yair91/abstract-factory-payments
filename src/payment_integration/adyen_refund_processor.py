from .refund_processor import RefundProcessor


class AdyenRefundProcessor(RefundProcessor):
    def refund(self, amount: float) -> str:
        return f"adyen:refunded:{amount:.2f}"
