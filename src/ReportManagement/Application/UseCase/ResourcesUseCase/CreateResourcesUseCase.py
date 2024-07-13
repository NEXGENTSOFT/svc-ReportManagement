from src.ReportManagement.Domain.Ports.ResourcesPort import ResourcesPort as Port, Resources

class CreateResourcesUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def create(self, report):
        if isinstance(report, list) and all(isinstance(d, dict) for d in report):
            resources = [Resources(**d) for d in report]
            return self.repository.create_resources(resources)
        else:
            raise ValueError("Invalid format for resources")
