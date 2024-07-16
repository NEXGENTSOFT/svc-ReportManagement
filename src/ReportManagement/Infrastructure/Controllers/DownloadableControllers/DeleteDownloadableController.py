from src.ReportManagement.Application.UseCase.DownloadableUseCase.DeleteDownloadableUseCase import DeleteDownloadableUseCase as UseCase, Port

class DeleteDownloadableController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, id: str):
        return self.__use_case.delete(id)

