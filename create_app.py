import os
import sys

# Define the base structure
BASE_STRUCTURE = {
    "adapters": ["orm.py", "repositories.py"],
    "domain": ["models.py"],
    "entrypoints": ["dependencies.py", "router.py", "schemas.py"],
    "interfaces": ["repositories.py", "units_of_work.py"],
    "service_layer": ["service.py", "units_of_work.py"],
    "": ["config.py", "constants.py", "exceptions.py"],  # Root files
}

def create_app_structure(module_name: str):
    # Base directory where the app package will be created
    base_dir = os.path.join("src", module_name)
    os.makedirs(base_dir, exist_ok=True)

    # Create sub-packages and files
    for package, files in BASE_STRUCTURE.items():
        # Create sub-package directory
        package_dir = os.path.join(base_dir, package)
        if package:
            os.makedirs(package_dir, exist_ok=True)
            # Add an __init__.py to make it a package
            init_path = os.path.join(package_dir, "__init__.py")
            with open(init_path, "w") as f:
                f.write(f"# This is the __init__.py file for the {package} package.\n")

        # Create files within the package
        for file in files:
            file_path = os.path.join(package_dir, file)
            with open(file_path, "w") as f:
                # Add basic file content (optional)
                f.write(f"# This is the {file} file in the {package or module_name} module.\n")

    # Add __init__.py to the root module directory
    init_path = os.path.join(base_dir, "__init__.py")
    with open(init_path, "w") as f:
        f.write(f"# This is the __init__.py file for the {module_name} module.\n")

    print(f"Module '{module_name}' created successfully at: {base_dir}")


if __name__ == "__main__":
    # Check if module name is provided
    if len(sys.argv) != 2:
        print("Usage: python create_app.py <module_name>")
        sys.exit(1)

    # Get module name from command-line arguments
    module_name = sys.argv[1]

    # Create the structure
    create_app_structure(module_name)
