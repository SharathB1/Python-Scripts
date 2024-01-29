import boto3

def list_ec2_instances():
    """ List all EC2 instances """
    ec2 = boto3.client('ec2')

    # Call to AWS EC2 to retrieve instance information
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']} - State: {instance['State']['Name']}")

if __name__ == "__main__":
    list_ec2_instances()

