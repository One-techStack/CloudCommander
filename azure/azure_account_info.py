from azure.identity import DefaultAzureCredential, CredentialUnavailableError
from azure.mgmt.resource import SubscriptionClient
from termcolor import colored
import sys
import io

def get_azure_account_info():
    try:
        # Use the default credential (e.g. env variables, configuration files, etc.)
        credential = DefaultAzureCredential()

        # Create a Subscription client using the provided credential
        subscription_client = SubscriptionClient(credential)

        # Get the first subscription (you can enhance this if there are multiple subscriptions)
        subscription = next(subscription_client.subscriptions.list())
        
        if subscription:
            return {
                "subscription_id": subscription.subscription_id,
                "tenant_id": subscription.tenant_id,
                "subscription_name": subscription.display_name,
                "state": subscription.state
            }
        else:
            return "No Azure subscription found."

    except Exception as e:
        return f"Failed to fetch Azure account information. Reason: {str(e)}"

if __name__ == "__main__":
    print(get_azure_account_info())
