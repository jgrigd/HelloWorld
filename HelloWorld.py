# Hello World Activity Handler.
def handler(event, context):
    try:
        print("Event Passed to Function: %s" % event)
        
        # create response text
        response = "Hello!"
        

        return response

    except Exception as e:
        print(" Caught Exception: %s" % e)
        
        return "Caught Error!"
