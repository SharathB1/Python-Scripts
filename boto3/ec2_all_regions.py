import boto3

def list_ec2_instances(region_name):
    """ List all EC2 instances in a specific region """
    ec2 = boto3.client('ec2', region_name=region_name)

    try:
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"Region: {region_name} - Instance ID: {instance['InstanceId']} - State: {instance['State']['Name']}")
    except Exception as e:
        print(f"Error retrieving instances in region {region_name}: {e}")

def list_all_regions():
    """ Return a list of all AWS regions """
    ec2 = boto3.client('ec2')
    regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
    return regions

if __name__ == "__main__":
    regions = list_all_regions()
    for region in regions:
        list_ec2_instances(region)
