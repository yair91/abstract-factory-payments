from .refund_processor import RefundProcessor


class StripeRefundProcessor(RefundProcessor):
    def refund(self, amount: float) -> str:
        return f"stripe:refunded:{amount:.2f}"
