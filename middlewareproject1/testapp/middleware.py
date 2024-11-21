class ExecutionFlowMiddleWare(object):
    def __init__(self,get_response):
        print('init method execution.....')
        self.get_response=get_response
    
    def __call__(self,request):
        """if this middleware is the last one it will call the view function that handles the request."""
        print("Preprocessing of request")
        response=self.get_response(request)
        print("Post processing of request")
        return response
    