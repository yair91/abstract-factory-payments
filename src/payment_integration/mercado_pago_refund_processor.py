from .refund_processor import RefundProcessor


class MercadoPagoRefundProcessor(RefundProcessor):
    def refund(self, amount: float) -> str:
        return f"mercadopago:refunded:{amount:.2f}"
