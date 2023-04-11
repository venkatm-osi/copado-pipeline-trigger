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
                "message": "Pipeline named '" +requestedPipeline+"' is triggered now",
            }
    except Exception as e:
        return {
            "statusCode": 204,
            "message": "Pipeline named '" +requestedPipeline+ "' does not exist here",
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
