from src.ReportManagement.Application.UseCase.ResourcesUseCase.DeleteResourcesUseCase import DeleteResourcesUseCase as UseCase, Port

class DeleteResourcesController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, id):
        return self.__use_case.delete(id)