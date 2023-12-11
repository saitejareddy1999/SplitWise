from abc import ABC, abstractmethod


class SettleUpStrategy(ABC):
    @abstractmethod
    def settle_up_heap(self,expense):
        pass
