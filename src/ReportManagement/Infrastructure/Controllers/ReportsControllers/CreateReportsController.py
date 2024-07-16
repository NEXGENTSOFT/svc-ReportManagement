from src.ReportManagement.Application.UseCase.ReportsUseCase.CreateReportsUseCase import CreateReportsUseCase as UseCase, Port


class CreateReportsController:
    def __init__(self, repository):
        self.repository = repository

    def run(self, reports_dicts):
        try:
            # Asegúrate de que resources_dicts sea una lista de diccionarios
            if not isinstance(reports_dicts, list):
                raise ValueError("Data must be a list of dictionaries")

            # Llamar al método del repositorio
            return self.repository.create_resources(reports_dicts)
        except Exception as e:
            return {"error": str(e)}, 500