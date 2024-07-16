from src.ReportManagement.Application.UseCase.DownloadableUseCase.CreateDownloadableUseCase import CreateDownloadableUseCase as UseCase, Port

class CreateDownloadableController:
    def __init__(self, repository):
        self.repository = repository

    def run(self, down_dicts):
        try:
            if not isinstance(down_dicts, list):
                raise ValueError("Data must be a list of dictionaries")

            return self.repository.create_resources(down_dicts)
        except Exception as e:
            return {"error": str(e)}, 500