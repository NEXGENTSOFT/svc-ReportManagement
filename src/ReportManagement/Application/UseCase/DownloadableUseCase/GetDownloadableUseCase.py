from src.ReportManagement.Domain.Ports.DownloadablePort import DownloadablePort as Port

class GetDownloadableUseCase:
    def __init__(self, repository: Port):
        self.__repository = repository

    def get(self):
        return self.__repository.get_downloadable()
