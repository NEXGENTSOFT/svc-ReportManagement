from abc import ABC, abstractmethod
from src.ReportManagement.Domain.Entity.Downloadable import Downloadable

class DownloadablePort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_downloadable(self):
        pass

    @abstractmethod
    def delete_downloadable(self, id):
        pass

    @abstractmethod
    def update_downloadable(self, id, title):
        pass

    @abstractmethod
    def create_downloadable(self, downloadable: list[Downloadable]):
        pass