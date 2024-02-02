import boto3
from datetime import datetime, timedelta

def list_ec2_instances(region_name):
    """ List all EC2 instances in the specified region """
    ec2 = boto3.client('ec2', region_name=region_name)
    instances = ec2.describe_instances()
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    return instance_ids

def get_cpu_utilization(instance_id, region_name, period=86400, interval=300):
    """Get the average CPU Utilization for an EC2 instance."""
    cloudwatch = boto3.client('cloudwatch', region_name=region_name)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(seconds=period)

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=interval,
        Statistics=['Average']
    )

    datapoints = response['Datapoints']
    if datapoints:
        average = sum(d['Average'] for d in datapoints) / len(datapoints)
        return average
    return None

if __name__ == "__main__":
    region = 'us-east-1'  # Give your region 'us-west-1'
    instances = list_ec2_instances(region)
    for instance_id in instances:
        avg_cpu = get_cpu_utilization(instance_id, region)
        if avg_cpu is not None:
            print(f"Instance {instance_id}: Average CPU Utilization: {avg_cpu:.2f}%")
        else:
            print(f"Instance {instance_id}: No CPU Utilization data available")
