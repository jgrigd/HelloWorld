# Hello World Activity Handler.
def handler(event, context):
    try:
        print("Event Passed to Function: %s" % event)
        
        # create response text

        if 'name' in event and event['name']:
            response = "Hello " + event['name'] + "!"
        else:
            response = "Hello there friend!"
        

        return response

    except Exception as e:
        print(" Caught Exception: %s" % e)
        
        return "Caught Error!"
