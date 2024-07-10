from src.ReportManagement.Application.UseCase.ResourcesUseCase.UpdateResourcesUseCase import UpdateResourcesUseCase as UseCase, Port
import json

class UpdateResourcesController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, payload: str):
        self.__use_case.upda(json.loads(payload))
