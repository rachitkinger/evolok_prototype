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
    print("received request to upload {}".format(blob_content))
    storage_client = storage.Client()
    print("storage client executed")
    myBucket = storage_client.get_bucket(bucket_name)
    print("bucket name registered")
    blob = myBucket.blob(str(blob_name))
    print("blob registered")
    print("blob content type is")
    print(type(blob_content))
    content = json.dumps(blob_content)
    print("blob content convert into json dump")
    print(type(content))
    blob.upload_from_string(content)
    print('blob uploaded')
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
    print("request json successful")
    if request_json and 'payload' in request_json:
        print("entered if statement")
        blob_name = request_json['payload']['created']
        print("blob name is {}".format(blob_name))
        blob_content = request_json
        print("blob_content is {}".format(blob_content))
        print("blob content type is")
        print(type(blob_content))
        bucket_name = "rk-test1"
        print("Sending request for upload")
        result = upload_to_bucket(bucket_name,blob_name,blob_content)
        print(result)
        return result
    else:
        print('Error: Unexpected content in webhook')
        return f'Unexpected content in webhook'