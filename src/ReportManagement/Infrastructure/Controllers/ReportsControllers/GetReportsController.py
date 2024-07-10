from src.ReportManagement.Application.UseCase.ReportsUseCase.GetReportsUseCase import GetReportsUseCase as UseCase, Port

class GetReportsController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self):
        return self.__use_case.get()