from google.cloud import storage
# def upload_blob(bucket_name, blob_test, destination_blob_name):
#     """
#     Uploads the json message into GCP bucket called rk-test1
#     """
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)

#     blob.upload_from_string(blob_text)

#     print('File {} uploaded to {}.'.format(
#         source_file_name,
#         destination_blob_name))

# def log_data(request):
#     request_json = request.get_json()
#     BUCKET_NAME = 'rk-test1'
#     BLOB_NAME = 'test-blob'
#     #BLOB_STR = '{"blob": "some json"}'
    

#     upload_blob(BUCKET_NAME, request_json, BLOB_NAME)
#     return f'Success!'
    
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
    print("Request attributes are ",request_json['attributes'])
    return f'Hello World!'
    