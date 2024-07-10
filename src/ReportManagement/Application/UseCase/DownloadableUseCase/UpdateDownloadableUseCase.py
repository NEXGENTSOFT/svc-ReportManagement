from src.ReportManagement.Domain.Ports.DownloadablePort import DownloadablePort as Port

class UpdateDownloadableUseCase():
    def __init__(self, repository: Port):
        self.repository = repository

    def upda(self, report):
        self.repository.update_downloadable(report['id'], report['title'])
