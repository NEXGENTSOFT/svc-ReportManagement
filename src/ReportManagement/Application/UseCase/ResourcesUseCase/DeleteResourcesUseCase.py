from src.ReportManagement.Domain.Ports.ResourcesPort import ResourcesPort as Port

class DeleteResourcesUseCase:
    def __init__(self, repository: Port):
        self.__repository = repository

    def delete(self, id):
        return self.__repository.delete_resources(id)

