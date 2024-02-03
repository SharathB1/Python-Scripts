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

if __name__ == "__main__":
    region = 'us-east-1'  # Give your 'region'
    open_sgs = find_open_security_groups(region)
    if open_sgs:
        print("Open Security Groups:")
        for sg_id in open_sgs:
            print(sg_id)
    else:
        print("No open security groups found.")
