from google.cloud import storage
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
    #TODO Remove service key path before committing
    storage_client = storage.Client.from_service_account_json("/home/rachit/gdrive/GCP/service-account-key/rachit-kinger-service-key.json")
    myBucket = storage_client.get_bucket(bucket_name)
    blob = myBucket.blob(blob_name)
    blob.upload_from_string(blob_content)
    return print('File name {} uploaded to bucket {}'.format(blob_name,bucket_name))

    
def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    # if request.args and 'message' in request.args:
    #     print("Request.args is ",request.args.get('message'))
    #     return request.args.get('message')
    # elif request_json and 'message' in request_json:
    #     print("Request_json is ", request_json['message'])
    #     return(request_json['message'])
    # elif request_json and 'attributes' in request_json:
    #     print("Request_json is", request_json['attributes'])
    #     return request_json['message']
    # else:
    #     return f'Hello World!'
    print("Request attributes are ",request_json)
    return f'Hello World!'
    