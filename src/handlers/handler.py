import json


def hello(event, context):
    response = {}
    response['body'] = json.dumps({'message': 'Hello World at v0.1!'})

    return response
