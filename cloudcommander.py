import checkcloud
from prettytable import PrettyTable

# Cloud-specific functionalities are in the respective directories
from azure.azure_account_info import get_azure_account_info
from aws.aws_account_info import get_aws_account_info
from gcp.gcp_account_info import get_gcp_account_info


def display_info_table(cloud_name, info_dict):
    """Function to display cloud account info in a table format"""
    print(f"\n{cloud_name.upper()} Account Information:")
    info_table = PrettyTable()
    info_table.field_names = ["Attribute", "Value"]
    info_table.align["Attribute"] = "l"
    info_table.align["Value"] = "l"
    for key, value in info_dict.items():
        info_table.add_row([key, value])
    print(info_table)

def main():
    available_clouds = []

    # AWS Check and Operations
    if checkcloud.check_aws_setup():
        available_clouds.append('aws')
        # AWS-specific actions can be invoked here
        aws_info = get_aws_account_info()
        display_info_table("AWS", aws_info)

    # Azure Check and Operations
    if checkcloud.check_azure_setup():
        available_clouds.append('azure')
        # Azure-specific actions can be invoked here
        azure_info = get_azure_account_info()
        display_info_table("Azure", azure_info)

    # GCP Check and Operations
    if checkcloud.check_gcp_setup():
        available_clouds.append('gcp')
        # GCP-specific actions can be invoked here
        gcp_info = get_gcp_account_info()
        if gcp_info:
            display_info_table("GCP Info", gcp_info)

    # Display available clouds

    # Print a headline for "available clouds" in highlight color
    print("\nAvailable Clouds:")
    cloud_table = PrettyTable()
    cloud_table.field_names = ["Available Clouds"]
    cloud_table.align["Available Clouds"] = "l"
    for cloud in available_clouds:
        cloud_table.add_row([cloud.upper()])
    print(cloud_table)

if __name__ == "__main__":
    main()
