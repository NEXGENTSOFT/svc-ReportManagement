from src.ReportManagement.Application.UseCase.ResourcesUseCase.GetResourcesUseCase import GetResourcesUseCase as UseCase, Port

class GetResourcesController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self):
        return self.__use_case.get()
