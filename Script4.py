import os

bases_de_datos = []

def create_file(file_path):
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)
    try:
        with open(file_path, 'x'):
            pass
        print(f"Ready: '{file_path}'")
    except FileExistsError:
        print(f"El archivo '{file_path}' ya existe.")

def create_crud_files(entity_name, folder_path, suffix, file_extension):
    crud_operations = ['Create', 'Get', 'Update', 'Delete']
    for operation in crud_operations:
        file_name = f'{operation}{entity_name}{suffix}{file_extension}'
        create_file(os.path.join(folder_path, file_name))

def create_entity_and_ports(domain_path, entity_name, file_extension):
    # Crear entidad
    entity_file = os.path.join(domain_path, 'Entity', f'{entity_name}{file_extension}')
    create_file(entity_file)

    # Crear puerto
    port_file = os.path.join(domain_path, 'Ports', f'{entity_name}Port{file_extension}')
    create_file(port_file)

def create_application_usecase(application_path, entity_name, file_extension):
    usecase_folder = os.path.join(application_path, f'{entity_name}UseCase')
    os.makedirs(usecase_folder, exist_ok=True)
    create_crud_files(entity_name, usecase_folder, "UseCase", file_extension)

def create_controller_usecase(infrastructure_path, entity_name, file_extension):
    controller_folder = os.path.join(infrastructure_path, 'Controllers', f'{entity_name}Controllers')
    os.makedirs(controller_folder, exist_ok=True)
    create_crud_files(entity_name, controller_folder, "Controller", file_extension)

def create_model_and_repository(infrastructure_path, entity_name, file_extension):
    for db in bases_de_datos:  # Usar bases de datos proporcionadas por el usuario
        model_folder = os.path.join(infrastructure_path, 'Models', db)
        os.makedirs(model_folder, exist_ok=True)
        model_file = os.path.join(model_folder, f'{db}{entity_name}Model{file_extension}')
        create_file(model_file)

        repository_folder = os.path.join(infrastructure_path, 'Repository', db)
        os.makedirs(repository_folder, exist_ok=True)
        repository_file = os.path.join(repository_folder, f'{db}{entity_name}Repository{file_extension}')
        create_file(repository_file)

def create_routes(infrastructure_path, entity_name, file_extension):
    routes_folder = os.path.join(infrastructure_path, 'Routes')
    os.makedirs(routes_folder, exist_ok=True)
    route_file = os.path.join(routes_folder, f'{entity_name}Route{file_extension}')
    create_file(route_file)

def Domain(project_route, name_micro, entities, file_extension):
    domain_path = os.path.join(project_route, 'Domain')
    os.makedirs(domain_path, exist_ok=True)

    for entity_name in entities:
        create_entity_and_ports(domain_path, entity_name, file_extension)
        create_application_usecase(os.path.join(project_route, 'Application', 'UseCase'), entity_name, file_extension)
        create_controller_usecase(os.path.join(project_route, 'Infrastructure'), entity_name, file_extension)
        create_model_and_repository(os.path.join(project_route, 'Infrastructure'), entity_name, file_extension)
        create_routes(os.path.join(project_route, 'Infrastructure'), entity_name, file_extension)

def project(base_ruta, file_extension):
    name_micro = input("\nNombre del Micro: ")
    entities = input("\nIngrese los nombres de las entidades separadas por comas: ").split(',')
    project_path = os.path.join(base_ruta, name_micro)
    os.makedirs(project_path, exist_ok=True)
    print(f'src/{name_micro}')
    Domain(project_path, name_micro, [entity.strip() for entity in entities], file_extension)

def database(file_extension):
    global bases_de_datos
    src_path = os.path.join(os.getcwd(), 'src')
    os.makedirs(src_path, exist_ok=True)

    if file_extension == '.py':
        database_path = os.path.join(src_path, 'Database')
        os.makedirs(database_path, exist_ok=True)
        bases_de_datos = input("\nIngrese las bases de datos separadas por comas (e.g., MySQL,PostgreSQL): ").split(',')

        for db in bases_de_datos:
            db_path = os.path.join(database_path, db)
            os.makedirs(db_path, exist_ok=True)
            connection_file = os.path.join(db_path, 'connection.py')
            create_file(connection_file)

    project(src_path, file_extension)
def main():
    file_type = input('\nElige P para Python o J para Java: ').upper()
    file_extension = '.py' if file_type == 'P' else '.java' if file_type == 'J' else None
    if file_extension:
        database(file_extension)
    else:
        print("Opción inválida, saliendo.")

if __name__ == "__main__":
    main()