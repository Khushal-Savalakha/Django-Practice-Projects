from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        # self.get_response=get_response
        pass
    
    def __call__(self,request):
        return HttpResponse('<h1>Currently Applicaion underMaintenance ..Please try after 2 days</h1>')