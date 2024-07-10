from src.ReportManagement.Domain.Ports.ReportsPort import ReportsPort as Port

class UpdateReportsUseCase():
    def __init__(self, repository: Port):
        self.repository = repository

    def upda(self, report):
        self.repository.update_report(report['id'], report['title'])
