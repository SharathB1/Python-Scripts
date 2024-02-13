from google.cloud import storage

def list_buckets(project_id):
    """Lists all buckets in a given project."""
    storage_client = storage.Client(project=project_id)
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

# Example usage
list_buckets('your-project-id')
