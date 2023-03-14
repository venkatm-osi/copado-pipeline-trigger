def lambda_handler(event, context):
    import json

    try:
        if event["httpMethod"] != "POST":
            raise Exception("Invalid HTTP method")
        
        apiKey = event["headers"]["X-API-Key"]
        if apiKey != "YOUR_API_KEY":
            raise Exception("Invalid API key")
        
        requestedPipeline = event["message"][0]["keyword"]
        if len(requestedPipeline) == 0:
            raise Exception("No pipeline name provided")
        
        returnCode = start_code_pipeline(requestedPipeline)
        return {
            "statusCode": 200,
            "body": requestedPipeline,
        }
    except KeyError:
        return {
            "statusCode": 400,
            "body": "Missing API key in request headers",
        }
    except Exception as e:
        if str(e) == "Invalid HTTP method":
            return {
                "statusCode": 405,
                "body": "Method not allowed",
            }
        else:
            return {
                "statusCode": 401,
                "body": str(e),
            }

def start_code_pipeline(pipelineName):
    client = codepipeline_client()
    response = client.start_pipeline_execution(name=pipelineName)
    return True

cpclient = None

def codepipeline_client():
    import boto3

    global cpclient
    if not cpclient:
        cpclient = boto3.client("codepipeline")
    return cpclient
]
