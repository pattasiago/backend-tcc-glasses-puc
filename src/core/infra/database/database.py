from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    @abstractmethod
    def remove_session(self):
        pass

    def init_session(self):
        pass
