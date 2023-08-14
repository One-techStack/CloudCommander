import checkcloud

# Cloud-specific functionalities are in the respective directories
from azure.azure_account_info import get_azure_account_info
from aws.aws_account_info import get_aws_account_info
# from gcp.gcp_account_info import get_gcp_account_info


def main():
    available_clouds = []

    # AWS Check and Operations
    if checkcloud.check_aws_setup():
        available_clouds.append('aws')
        # AWS-specific actions can be invoked here
        aws_info = get_aws_account_info()
        print("AWS Info:", aws_info)

    # Azure Check and Operations
    if checkcloud.check_azure_setup():
        available_clouds.append('azure')
        # Azure-specific actions can be invoked here
        azure_info = get_azure_account_info()
        print("Azure Info:", azure_info)

    # GCP Check and Operations
    if checkcloud.check_gcp_setup():
        available_clouds.append('gcp')
        # GCP-specific actions can be invoked here
        # Example:
        # gcp_info = get_gcp_account_info()
        # print("GCP Info:", gcp_info)

    print("\nAvailable Clouds:", available_clouds)

    # The rest of your main CloudCommander functionality can continue here...

if __name__ == "__main__":
    main()

