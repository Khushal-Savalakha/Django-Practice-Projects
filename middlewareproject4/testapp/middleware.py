from django.http import HttpResponse
class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        print('This line is printed by Middleware-1 before processing request')
        response =self.get_response(request)
        print('This Line printed by Middleware-1 after processing request')
        return response
    
    def process_exception(self,request,exception):
        return HttpResponse(f'<h1>1] Currrently we are facing some technical problem...Please try after some time.</h1><br/><p>The raised exception is {exception.__class__.__name__} because of :{exception}</p>')

class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        print('This line is printed by Middleware-2 before processing request')
        response =self.get_response(request)
        print('This Line printed by Middleware-2 after processing request')
        return response
    
    def process_exception(self,request,exception):
        return HttpResponse(f'<h1>2] Currrently we are facing some technical problem...Please try after some time.</h1><br/><p>The raised exception is {exception.__class__.__name__} because of :{exception}</p>')

class ThreeMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        print('This line is printed by Middleware-3 before processing request')
        response =self.get_response(request)
        print('This Line printed by Middleware-3 after processing request')
        return response
    
    def process_exception(self,request,exception):
        return HttpResponse(f'<h1>Currrently we are facing some technical problem...Please try after some time.</h1><br/><p>The raised exception is {exception.__class__.__name__} because of :{exception}</p>')