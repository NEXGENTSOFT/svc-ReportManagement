from src.ReportManagement.Domain.Ports.ReportsPort import ReportsPort as Port

class DeleteReportsUseCase:
    def __init__(self, repository: Port):
        self.__repository = repository

    def delete(self, id):
        return self.__repository.delete_report(id)

