from src.ReportManagement.Domain.Ports.ReportsPort import ReportsPort as Port, Report

class CreateReportsUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def create(self, report):
        reports = [Report(**d) for d in report]
        return self.repository.create_report(reports)