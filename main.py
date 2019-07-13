from google.cloud import storage
import json
def upload_to_bucket(bucket_name, blob_name, blob_content):
    """Upload blob content as is into a named bucket

    ------
    Args:
        bucket_name: str, name of an existing bucket on Google Cloud Storage
        blob_name: str, name of the blob. Should be a unique name else the existing blob with that name will be overwritten
        blob_content: str, exact content as it would be written into a file named 'blob_name'
    Returns:
        NoneType
        """
    storage_client = storage.Client()
    myBucket = storage_client.get_bucket(bucket_name)
    blob = myBucket.blob(str(blob_name))
    content = json.dumps(blob_content)
    blob.upload_from_string(content)
    return print('File name {} uploaded to bucket {}'.format(blob_name,bucket_name))

def receive_evolok(request):
    """Responds to any HTTP request. Sends Evolok webhooks to GCS bucket named 'rk-test1'.
    ---
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        str. Status of upload to GCS
    """
    request_json = request.get_json()
    if request_json and 'payload' in request_json:
        blob_name = request_json['payload']['created']
        blob_content = request_json
        bucket_name = "rk-test1"
        result = upload_to_bucket(bucket_name,blob_name,blob_content)
        print(result)
        return result
    else:
        print('Exited function: Unexpected payload structure sent from in webhook')
        return f'Unexpected payload structure in webhook'

def parse_payload(payload):
    """
    Converts payload into a row that can be entered BigQuery table
    :param payload: dict object as converted from flast.Request.get_json()
    :return: json as required by a specific BigQuery table
    """
    #TODO BigQuery table needs to be created
    
    return None
