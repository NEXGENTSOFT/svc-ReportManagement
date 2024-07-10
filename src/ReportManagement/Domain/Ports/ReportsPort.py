from abc import ABC, abstractmethod
from src.ReportManagement.Domain.Entity.Reports import Report

class ReportsPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_report(self):
        pass

    @abstractmethod
    def create_report(self, report: list[Report]):
        pass

    @abstractmethod
    def delete_report(self, id):
        pass

    @abstractmethod
    def update_report(self, id, title):
        pass
