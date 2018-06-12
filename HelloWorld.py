# Hello World Activity Handler.
def handler(event, context):
    try:
        print("Event Passed to Function: %s" % event)
        
        # create response text
        response = "Hello Friend!"
        if 'FirstName' in event and event['FirstName']:
            response = "Hello " + event['FirstName']
        if 'LastName' in event and event['LastName']:
            response += " " + event['LastName']

        return response

    except Exception as e:
        print(" Caught Exception: %s" % e)
        
        return "Caught Error!"
