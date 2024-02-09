import boto3

def get_all_security_groups(ec2):
    """ Return a set of all security group IDs """
    security_groups = ec2.describe_security_groups()
    return set(sg['GroupId'] for sg in security_groups['SecurityGroups'])

def get_used_security_groups(ec2):
    """ Return a set of security group IDs used by EC2 instances """
    used_sgs = set()
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            for sg in instance['SecurityGroups']:
                used_sgs.add(sg['GroupId'])
    return used_sgs

def find_unused_security_groups(region_name):
    ec2 = boto3.client('ec2', region_name=region_name)
    all_sgs = get_all_security_groups(ec2)
    used_sgs = get_used_security_groups(ec2)

    unused_sgs = all_sgs - used_sgs
    return unused_sgs

if __name__ == "__main__":
    region = 'us-east-1'  # Replace with your region
    unused_security_groups = find_unused_security_groups(region)
    if unused_security_groups:
        print("Unused Security Groups:")
        for sg_id in unused_security_groups:
            print(sg_id)
    else:
        print("No unused security groups found.")
