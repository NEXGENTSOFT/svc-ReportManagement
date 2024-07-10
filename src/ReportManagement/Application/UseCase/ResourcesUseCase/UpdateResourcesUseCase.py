from src.ReportManagement.Domain.Ports.ResourcesPort import ResourcesPort as Port

class UpdateResourcesUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def upda(self, report):
        self.repository.update_resources(report['id'], report['title'])
