from django.http import HttpResponse
class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        response =self.get_response(request)
        return response
    
    def process_exception(self,request,exception):
        return HttpResponse(f'<h1>Currrently we are facing some technical problem...Please try after some time.</h1><br/><p>The raised exception is {exception.__class__.__name__} because of :{exception}</p>')