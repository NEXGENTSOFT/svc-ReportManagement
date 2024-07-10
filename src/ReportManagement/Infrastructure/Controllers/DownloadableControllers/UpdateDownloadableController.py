from src.ReportManagement.Application.UseCase.DownloadableUseCase.UpdateDownloadableUseCase import UpdateDownloadableUseCase as UseCase, Port
import json
class UpdateDownloadableController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, payload: str):
        self.__use_case.upda(json.loads(payload))
