from src.ReportManagement.Application.UseCase.ReportsUseCase.UpdateReportsUseCase import UpdateReportsUseCase as UseCase, Port
import json

class UpdateReportsController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, payload: dict):
        return self.__use_case.update(payload)
