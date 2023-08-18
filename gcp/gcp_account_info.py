import subprocess
import json

# GCP libraries
from google.cloud import storage
from google.cloud import bigquery

def get_gcp_account_info():
    """
    Retrieves general account information for GCP.

    Returns:
        dict: A dictionary containing GCP account details.
    """

    # Initialize the dictionary to hold account information
    account_info = {}

    # 1. Current Authenticated User
    try:
        auth_info = json.loads(subprocess.check_output(['gcloud', 'auth', 'list', '--format=json']).decode('utf-8'))
        account_info['authenticated_user'] = auth_info[0]['account'] if auth_info else "Not Authenticated"
    except:
        account_info['authenticated_user'] = "Failed to retrieve."

    # 2. Default Project
    try:
        config_info = json.loads(subprocess.check_output(['gcloud', 'config', 'list', '--format=json']).decode('utf-8'))
        account_info['default_project'] = config_info['core']['project'] if 'core' in config_info and 'project' in config_info['core'] else "Not set"
    except:
        account_info['default_project'] = "Failed to retrieve."

    # 3. List of Configurations
    try:
        configurations = subprocess.check_output(['gcloud', 'config', 'configurations', 'list', '--format=value(name)']).decode('utf-8').splitlines()
        account_info['configurations'] = configurations
    except:
        account_info['configurations'] = "Failed to retrieve."

    # 4. Activated Services
    try:
        services = json.loads(subprocess.check_output(['gcloud', 'services', 'list', '--enabled', '--format=json']).decode('utf-8'))
        account_info['enabled_services'] = [service['config']['name'] for service in services]
    except:
        account_info['enabled_services'] = "Failed to retrieve."

    # 5. Billing Information (only checks if the default project is associated with a billing account)
    try:
        billing_info = json.loads(subprocess.check_output(['gcloud', 'alpha', 'billing', 'projects', 'describe', account_info['default_project'], '--format=json']).decode('utf-8'))
        account_info['billing'] = "Associated with a billing account" if 'billingAccountName' in billing_info else "Not associated with a billing account"
    except:
        account_info['billing'] = "Failed to retrieve."

    return account_info

if __name__ == "__main__":
    info = get_gcp_account_info()
    for key, value in info.items():
        print(f"{key}: {value}")

