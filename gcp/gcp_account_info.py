# from google.oauth2 import credentials, service_account
# from google.cloud import resourcemanager
# import google.auth

# def get_gcp_account_info():
#     try:
#         # Authenticate and initialize Cloud Resource Manager
#         creds, project_id = google.auth.default()
#         client = resourcemanager.ProjectsClient(credentials=creds)

#         # Fetch account information
#         project = client.get_project(project_id)
#         account_info = {
#             'Project ID': project.project_id,
#             'Project Name': project.name,
#             'Project Number': project.number,
#             'Lifecycle State': project.state.name,
#             'Project Labels': project.labels
#         }

#         return account_info
#     except Exception as e:
#         print(f"Failed to fetch GCP account information. Reason: {e}")
#         return None

# if __name__ == "__main__":
#     info = get_gcp_account_info()
#     print(info)

from google.cloud import resourcemanager
import google.auth

def get_gcp_account_info():
    try:
        # Authenticate with GCP
        creds, project_id = google.auth.default()
        
        # Initialize the Resource Manager Client
        client = resourcemanager.ProjectsClient(credentials=creds)
        
        # Get the project details
        project = client.get_project(project_id)
        
        account_info = {
            'Project ID': project.project_id,
            'Project Name': project.name,
            # 'Project Number': project.number,
            # 'Lifecycle State': project.status,
            'Project Labels': project.labels
        }

        return account_info

    except Exception as e:
        print(f"Failed to fetch GCP account information. Reason: {e}")
        return None

if __name__ == "__main__":
    info = get_gcp_account_info()
    print(info)
