from github import Github

repo_action = Github("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")

def lambda_handler(event, context):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print("Starting functions\n---------------------------------------------")

    if event["input"] == "Hello":

        return "World"

    else:

        raise
