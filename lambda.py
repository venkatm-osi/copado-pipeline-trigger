def lambda_handler(event, context):
    import json

    if event["httpMethod"] != "POST":
        return {
            "statusCode": 405,
            "body": "Method not allowed",
        }

    try:
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
        return {
            "statusCode": 401,
            "body": str(e),
        }
