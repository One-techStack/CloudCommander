import os

def install_dependencies():
    """
    Installs required dependencies for CloudCommander.
    """
    print("Installing dependencies for CloudCommander...")

    # AWS dependencies
    os.system("pip install boto3")

    # Azure dependencies
    os.system("pip install azure-identity azure-mgmt-resource")

    # GCP dependencies
    os.system("pip install google-auth google-cloud-core google-cloud-resource-manager")

    print("\nDependencies installation completed!")

if __name__ == "__main__":
    install_dependencies()
