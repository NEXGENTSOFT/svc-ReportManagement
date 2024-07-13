from src.ReportManagement.Domain.Ports.DownloadablePort import DownloadablePort as Port, Downloadable

class CreateDownloadableUseCase:
    def __init__(self, repository: Port):
        self.repository = repository

    def create(self, report):
        if isinstance(report, list) and all(isinstance(d, dict) for d in report):
            downloadable = [Downloadable(**d) for d in report]
            return self.repository.create_downloadable(downloadable)
        else:
            raise ValueError("Invalid format for downloadable")
