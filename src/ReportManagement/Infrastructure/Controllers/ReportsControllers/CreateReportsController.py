from src.ReportManagement.Application.UseCase.ReportsUseCase.CreateReportsUseCase import CreateReportsUseCase as UseCase, Port


class CreateReportsController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, request):
        return self.__use_case.create(request.get_json())