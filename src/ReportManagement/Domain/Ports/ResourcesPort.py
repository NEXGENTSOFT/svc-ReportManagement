from abc import ABC, abstractmethod
from src.ReportManagement.Domain.Entity.Resources import Resources

class ResourcesPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_resources(self):
        pass

    @abstractmethod
    def create_resources(self, resources: list[Resources]):
        pass

    @abstractmethod
    def delete_resources(self, id):
        pass

    @abstractmethod
    def update_resources(self, id, title):
        pass
