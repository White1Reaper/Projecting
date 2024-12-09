from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def write_all(self, data):
        pass