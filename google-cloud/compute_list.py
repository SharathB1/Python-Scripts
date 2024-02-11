from google.cloud import compute_v1

def list_instances(project_id, zone):
    compute_client = compute_v1.InstancesClient()
    instances = compute_client.list(project=project_id, zone=zone)

    print("Instances in project {} and zone {}:".format(project_id, zone))
    for instance in instances:
        print(f"- {instance.name} (ID: {instance.id})")

# Example usage
list_instances('your-project-id', 'us-central1-a')
