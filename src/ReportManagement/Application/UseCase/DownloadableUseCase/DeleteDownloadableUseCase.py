from src.ReportManagement.Domain.Ports.DownloadablePort import DownloadablePort as Port

class DeleteDownloadableUseCase:
    def __init__(self, repository: Port):
        self.__repository = repository

    def delete(self, id):
        return self.__repository.delete_downloadable(id)

