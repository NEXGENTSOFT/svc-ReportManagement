from src.ReportManagement.Domain.Ports.ReportsPort import ReportsPort as Port, Report

class CreateReportsUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def create(self, report):
        if isinstance(report, list) and all(isinstance(d, dict) for d in report):
            reports = [Report(**d) for d in report]
            return self.repository.create_report(reports)
        else:
            raise ValueError("Invalid format for report")
