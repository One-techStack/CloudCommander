import google.cloud
from google.cloud import resourcemanager
from google.auth.exceptions import DefaultCredentialsError

def get_gcp_account_info():
    """
    Retrieves general account information for GCP.

    Returns:
        dict: A dictionary containing GCP account details.
    """
    client = resourcemanager.ProjectsClient()

    project_details = []
    for project in client.list_projects():
        project_details.append({
            'project_id': project.project_id,
            'project_name': project.name,
            'labels': project.labels,
            'status': project.status
        })

    # Currently, this script returns a list of projects in the GCP account.
    # You can extend this to gather more details.
    account_info = {
        'projects': project_details
    }

    return account_info

if __name__ == "__main__":
    try:
        gcp_info = get_gcp_account_info()
        print("GCP Account Info:", gcp_info)
    except DefaultCredentialsError:
        print("GCP is not set up on this machine.")
