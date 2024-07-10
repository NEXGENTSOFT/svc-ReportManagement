from src.ReportManagement.Application.UseCase.DownloadableUseCase.CreateDownloadableUseCase import CreateDownloadableUseCase as UseCase, Port

class CreateDownloadableController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, request):
        return self.__use_case.create(request.get_json())