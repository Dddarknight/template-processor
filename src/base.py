from abc import ABC, abstractmethod


class AbstractRenderer(ABC):
    @abstractmethod
    def render(self):
        pass


class AbstractValidator(ABC):
    @abstractmethod
    def validate(self):
        pass
