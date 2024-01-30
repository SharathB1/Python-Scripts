import boto3

def manage_ec2_instances(action, region='us-east-1', tag_key=None, tag_value=None):
    ec2 = boto3.resource('ec2', region_name=region)
    filters = [{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}]
    
    if tag_key and tag_value:
        filters.append({'Name': f'tag:{tag_key}', 'Values': [tag_value]})

    print(f"Filters: {filters}")  # Debugging

    instances = ec2.instances.filter(Filters=filters)

    found_instances = False
    for instance in instances:
        found_instances = True
        if action == 'start':
            instance.start()
            print(f"Starting instance: {instance.id}")
        elif action == 'stop':
            instance.stop()
            print(f"Stopping instance: {instance.id}")

    if not found_instances:
        print("No instances found matching the criteria.")

# Example Usage
# manage_ec2_instances('start', tag_key='your_tag_key', tag_value='your_tag_value')
manage_ec2_instances('start')