from src.ReportManagement.Application.UseCase.DownloadableUseCase.GetDownloadableUseCase import GetDownloadableUseCase as UseCase, Port

class GetDownloadableController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self):
        return self.__use_case.get()
