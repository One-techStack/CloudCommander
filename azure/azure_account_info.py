import subprocess
import json

def get_azure_account_info():
    """
    Retrieves general account information for Azure.

    Returns:
        dict: A dictionary containing Azure account details.
    """

    account_info = {}

    # 1. Subscription ID and Name
    try:
        account_data = json.loads(subprocess.check_output(['az', 'account', 'show', '--output', 'json']).decode('utf-8'))
        account_info['Subscription ID'] = account_data['id']
        account_info['Subscription Name'] = account_data['name']
        account_info['Tenant ID'] = account_data['tenantId']
    except:
        account_info['Subscription ID'] = "Failed to retrieve."
        account_info['Subscription Name'] = "Failed to retrieve."
        account_info['Tenant ID'] = "Failed to retrieve."

    # 2. Current Account
    try:
        user = json.loads(subprocess.check_output(['az', 'ad', 'signed-in-user', 'show', '--output', 'json']).decode('utf-8'))
        account_info['Current Account'] = user['userPrincipalName']
    except:
        account_info['Current Account'] = "Failed to retrieve."

    # 3. Default Region
    try:
        config = json.loads(subprocess.check_output(['az', 'configure', '--list-defaults', '--output', 'json']).decode('utf-8'))
        location = next((item['value'] for item in config if item["name"] == "location"), "Not set")
        account_info['Default Region'] = location
    except:
        account_info['Default Region'] = "Failed to retrieve."

    # 4. Resource Groups
    try:
        resource_groups = json.loads(subprocess.check_output(['az', 'group', 'list', '--output', 'json']).decode('utf-8'))
        account_info['Resource Groups'] = "\n".join([rg['name'] for rg in resource_groups])
    except:
        account_info['Resource Groups'] = "Failed to retrieve."

    # 5. Enabled Features (considering features of the Azure subscription)
    try:
        features = json.loads(subprocess.check_output(['az', 'feature', 'list', '--namespace', 'Microsoft.Compute', '--output', 'json']).decode('utf-8'))
        enabled_features = [f['name'] for f in features if f['properties']['state'] == 'Registered']
        account_info['Enabled Features'] = "\n".join(enabled_features)
    except:
        account_info['Enabled Features'] = "Failed to retrieve."

    return account_info

if __name__ == "__main__":
    info = get_azure_account_info()
    for key, value in info.items():
        print(f"{key}: {value}")
