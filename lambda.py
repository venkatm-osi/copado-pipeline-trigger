def lambda_handler(event, context):
    import json

    try:
        requestedPipeline = event["message"][0]["keyword"]
        if len(requestedPipeline) == 0:
            raise Exception("No pipeline name provided")
        else:
            returnCode = start_code_pipeline(requestedPipeline)
            return {
                "statusCode": 200,
                "body": requestedPipeline,
            }
    except Exception as e:
        return {
            "statusCode": 400,
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
