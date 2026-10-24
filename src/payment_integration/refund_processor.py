from abc import ABC, abstractmethod


class RefundProcessor(ABC):
    @abstractmethod
    def refund(self, amount: float) -> str:
        raise NotImplementedError
