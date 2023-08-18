import sys
import io
import boto3
from azure.identity import DefaultAzureCredential, CredentialUnavailableError
import google.auth
from termcolor import colored

def check_aws_setup():
    original_stderr = sys.stderr  # Store the original stderr
    sys.stderr = io.StringIO()  # Redirect stderr
    # Show a header for AWS:
    print(colored("**** AWS Account Information: ****", "blue"))
    try:
        boto3.client('sts').get_caller_identity()
        print(colored("AWS is properly set up!", "green"))
        return True
    except Exception as e:
        print(colored(f"AWS is not set up on this machine. Reason: {e}", "red"))
        return False
    finally:
        sys.stderr = original_stderr  # Restore the original stderr

def check_azure_setup():
    original_stderr = sys.stderr  # Store the original stderr
    sys.stderr = io.StringIO()  # Redirect stderr
    # Show a header for Azure:
    print(colored("**** Azure Account Information: ****", "blue"))
    try:
        credential = DefaultAzureCredential()
        token = credential.get_token("https://management.azure.com/.default")
        if token:
            print(colored("Azure is properly set up!", "green"))
            return True
    except Exception:  # Not using the 'e' variable to prevent verbose output
        print(colored("Azure is not set up on this machine. Please run 'az login' or set up other Azure credentials.", "red"))
        return False
    finally:
        sys.stderr = original_stderr  # Restore the original stderr

def check_gcp_setup():
    original_stderr = sys.stderr
    sys.stderr = io.StringIO()
    # Show a header for GCP:
    print(colored("**** GCP Account Information: ****", "blue"))
    try:
        google.auth.default()
        print(colored("GCP is properly set up!", "green"))
        return True
    except Exception as e:
        print(colored(f"GCP is not set up on this machine. Reason: {e}", "red"))
        return False
    finally:
        sys.stderr = original_stderr

def check_all_clouds():
    available_clouds = []
    if check_aws_setup():
        available_clouds.append('aws')
    if check_azure_setup():
        available_clouds.append('azure')
    if check_gcp_setup():
        available_clouds.append('gcp')
    return available_clouds

if __name__ == "__main__":
    available = check_all_clouds()
    print("\nAvailable Clouds:", available)
