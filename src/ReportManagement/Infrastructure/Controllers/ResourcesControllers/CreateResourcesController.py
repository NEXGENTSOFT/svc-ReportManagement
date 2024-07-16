class CreateResourcesController:
    def __init__(self, repository):
        self.repository = repository

    def run(self, resources_dicts):
        try:
            if not isinstance(resources_dicts, list):
                raise ValueError("Data must be a list of dictionaries")

            return self.repository.create_resources(resources_dicts)
        except Exception as e:
            return {"error": str(e)}, 500