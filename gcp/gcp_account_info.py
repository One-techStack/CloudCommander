from google.cloud import resourcemanager
from google.oauth2 import service_account

def get_gcp_account_info():
    try:
        # get the project id
        def default():
            with open('') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('project'):
                        project_id = line.split('=')[1].strip()
                        return project_id
                else:
                    return None
                
        project_id = default()
        
        # Authenticate with GCP using your service account key file
        # Initialize the Resource Manager Client
        client = resourcemanager.ProjectsClient(credentials=credentials)
        
        # Get the project details
        project = client.get_project(project_id)
        
        account_info = {
            'Project ID': project.project_id,
            'Project Name': project.name
        }

        return account_info

    except Exception as e:
        print(f"Failed to fetch GCP account information. Reason: {e}")
        return None

if __name__ == "__main__":
    info = get_gcp_account_info()
    print(info)