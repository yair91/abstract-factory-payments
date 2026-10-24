from abc import ABC, abstractmethod


class PaymentAuthorizer(ABC):
    @abstractmethod
    def authorize(self, amount: float) -> str:
        raise NotImplementedError
