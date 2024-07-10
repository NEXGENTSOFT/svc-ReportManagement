from src.ReportManagement.Application.UseCase.ResourcesUseCase.CreateResourcesUseCase import CreateResourcesUseCase as UseCase, Port

class CreateResourcesController:
    def __init__(self, repository: Port):
        self.__use_case = UseCase(repository)

    def run(self, request):
        return self.__use_case.create(request.get_json())