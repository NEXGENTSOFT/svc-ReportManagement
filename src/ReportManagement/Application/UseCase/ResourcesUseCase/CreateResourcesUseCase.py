from src.ReportManagement.Domain.Ports.ResourcesPort import ResourcesPort as Port, Resources

class CreateResourcesUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def create(self, report):
        resources = [Resources(**d) for d in report]
        return self.repository.create_resources(resources)