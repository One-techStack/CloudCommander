# CloudCommander

## Overview
**CloudCommander** is a command-line tool designed for fetching and displaying virtual machine instance data across multiple cloud platforms: AWS, Azure, and Google Cloud Platform (GCP).

## Features

- Fetch virtual machine instance details such as instance ID and status.
- Supports AWS EC2, Azure VM, and Google Cloud Compute Engine.
- Unified command-line interface for multi-cloud management.

## Prerequisites

- Python 3.x
- Pip (for installing required libraries)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CloudCommander.git
    ```

2. Navigate to the project directory and install the required libraries:
    ```bash
    cd CloudCommander
    pip install -r requirements.txt
    ```

## Configuration

To communicate with each cloud platform, **CloudCommander** relies on SDKs and API client libraries. Ensure you've set up authentication credentials for:

- **AWS**: Configure your credentials using the AWS CLI or by setting up `~/.aws/credentials`.

- **Azure**: Authenticate using the `DefaultAzureCredential` class which searches for available credentials within your environment.

- **GCP**: Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable pointing to your service account key JSON file.

## Usage

Execute the script:
```bash
python cloud_commander.py
```

The output will display the ID and status of instances for each cloud provider.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the proposed changes.

## License

Apache 2.0
