import boto3

def get_aws_account_info():
    """
    Retrieves general account information for AWS.

    Returns:
        dict: A dictionary containing AWS account details.
    """
    # Initialize the Boto3 client for STS (Security Token Service)
    sts_client = boto3.client('sts')

    # Fetch the account ID
    account_id = sts_client.get_caller_identity()["Account"]

    # You can extend this section to retrieve more detailed information
    # For now, it returns just the account ID.
    account_info = {
        'AccountID': account_id
    }

    return account_info

if __name__ == "__main__":
    aws_info = get_aws_account_info()
    print("AWS Account Info:", aws_info)
