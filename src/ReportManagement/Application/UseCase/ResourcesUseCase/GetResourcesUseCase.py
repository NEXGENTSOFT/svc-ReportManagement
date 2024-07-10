from src.ReportManagement.Domain.Ports.ResourcesPort import ResourcesPort as Port

class GetResourcesUseCase:
    def __init__(self, repository: Port):
        self.__repository = repository

    def get(self):
        return self.__repository.get_resources()
