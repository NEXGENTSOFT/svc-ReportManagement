from src.ReportManagement.Domain.Ports.ReportsPort import ReportsPort as Port

class GetReportsUseCase:
    def __init__(self, repository: Port):
        self.__repository = repository

    def get(self):
        return self.__repository.get_report()
