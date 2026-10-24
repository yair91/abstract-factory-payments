class AdyenAuthorizer:
    def authorize(self, amount: float) -> str:
        return f"adyen:authorized:{amount:.2f}"
