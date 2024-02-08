import boto3

def find_open_security_groups(region_name):
    ec2 = boto3.client('ec2', region_name=region_name)
    security_groups = ec2.describe_security_groups()

    open_security_groups = []
    for sg in security_groups['SecurityGroups']:
        for rule in sg['IpPermissions']:
            for ip_range in rule.get('IpRanges', []):
                if ip_range.get('CidrIp') == '0.0.0.0/0':
                    open_security_groups.append(sg['GroupId'])
                    break
            for ipv6_range in rule.get('Ipv6Ranges', []):
                if ipv6_range.get('CidrIpv6') == '::/0':
                    open_security_groups.append(sg['GroupId'])
                    break

    return open_security_groups

def delete_security_groups(security_group_ids, region_name):
    ec2 = boto3.client('ec2', region_name=region_name)
    for sg_id in security_group_ids:
        try:
            ec2.delete_security_group(GroupId=sg_id)
            print(f"Deleted security group {sg_id}")
        except boto3.exceptions.Boto3Error as e:
            print(f"Could not delete security group {sg_id}: {e}")

if __name__ == "__main__":
    region = 'us-east-1'  # Give your region
    open_sgs = find_open_security_groups(region)
    if open_sgs:
        print("Deleting open security groups:")
        delete_security_groups(open_sgs, region)
    else:
        print("No open security groups found to delete.")
