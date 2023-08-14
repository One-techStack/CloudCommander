from azure.identity import DefaultAzureCredential, CredentialUnavailableError
from azure.mgmt.resource import SubscriptionClient
from termcolor import colored
import sys
import io

def get_azure_account_info():
    original_stderr = sys.stderr  # Store the original stderr
    sys.stderr = io.StringIO()  # Redirect stderr

    account_info = {}
    
    try:
        # Setting up authentication and client
        credential = DefaultAzureCredential()
        subscription_client = SubscriptionClient(credential)
        subscription = next(subscription_client.subscriptions.list())
        
        account_info['Subscription Name'] = subscription.display_name
        account_info['Subscription ID'] = subscription.subscription_id
        account_info['Tenant ID'] = subscription.tenant_id
        account_info['User'] = credential.get_token(scopes=["https://management.azure.com/.default"]).token

        return account_info
        
    except Exception as e:  
        print(colored(f"Failed to fetch Azure account information. Reason: {str(e)}", "red"))
        return None

    finally:
        sys.stderr = original_stderr  # Restore the original stderr

if __name__ == "__main__":
    info = get_azure_account_info()
    if info:
        for key, value in info.items():
            print(f"{key}: {value}")

