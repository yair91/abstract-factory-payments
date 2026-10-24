from abc import ABC, abstractmethod


class WebhookVerifier(ABC):
    @abstractmethod
    def verify(self, signature: str) -> bool:
        raise NotImplementedError
