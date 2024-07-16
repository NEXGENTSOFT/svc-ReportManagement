from src.ReportManagement.Application.UseCase.ReportsUseCase.DeleteReportsUseCase import DeleteReportsUseCase as UseCase, Port

class DeleteReportsController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, id: str):
        return self.__use_case.delete(id)
