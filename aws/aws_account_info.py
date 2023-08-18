import boto3

def get_aws_account_info():
    """Retrieves general account information for AWS."""

    # Initialize the AWS SDK clients for the services we're interested in
    sts = boto3.client('sts')
    iam = boto3.client('iam')
    organizations = boto3.client('organizations')
    ce = boto3.client('ce')

    # Dictionary to store the information
    account_info = {}

    # 1. Account ID
    account_info['Account ID'] = sts.get_caller_identity()['Account']

    # 2. Account Alias
    try:
        aliases = iam.list_account_aliases()['AccountAliases']
        account_info['Account Alias'] = aliases[0] if aliases else "No alias set"
    except:
        account_info['Account Alias'] = "Failed to retrieve."

    # 3. IAM User
    try:
        user_info = sts.get_caller_identity()
        account_info['IAM User ARN'] = user_info['Arn']
    except:
        account_info['IAM User ARN'] = "Failed to retrieve."

    # 4. IAM User's attached policies
    try:
        user_name = user_info['Arn'].split('/')[-1]
        policies = iam.list_attached_user_policies(UserName=user_name)['AttachedPolicies']
        policy_names = [policy['PolicyName'] for policy in policies]
        account_info['IAM User Policies'] = "\n".join(policy_names)
    except:
        account_info['IAM User Policies'] = "Failed to retrieve."

    # 5. Default Region (using boto3's default region)
    try:
        account_info['Default Region'] = boto3.DEFAULT_SESSION.region_name
    except:
        account_info['Default Region'] = "Failed to retrieve."

    # 6. Enabled Services (using AWS Service Last Accessed feature)
    try:
        entities = iam.get_service_last_accessed_details(Arn=user_info['Arn'])['ServicesLastAccessed']
        accessed_services = [entity['ServiceName'] for entity in entities]
        account_info['Accessed Services'] = "\n".join(accessed_services)
    except:
        account_info['Accessed Services'] = "Failed to retrieve."

    # 7. Billing Information
    try:
        results = ce.get_cost_and_usage(
            TimePeriod={
                'Start': '2023-08-01',
                'End': '2023-08-14'
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost']
        )
        cost = results['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
        account_info['Estimated Charges This Month ($)'] = "{:.2f}".format(float(cost))
    except:
        account_info['Estimated Charges This Month ($)'] = "Failed to retrieve."

    return account_info

if __name__ == "__main__":
    info = get_aws_account_info()
    for key, value in info.items():
        print(f"{key}: {value}")
