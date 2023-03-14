def lambda_handler(event, context):
    import json

    requestedPipeline = event["message"][0]["keyword"]

    #start the pipeline
    if len(requestedPipeline)>0:
        # Codepipeline name is foldername-job.
        # We can read the configuration from S3 as well.
        returnCode = start_code_pipeline(requestedPipeline)

    return {
        "statusCode": 200,
        "body": requestedPipeline,
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
