from django.shortcuts import render

# Create your views here.
def page_count_view(request):
    print(request.COOKIES)
    count=request.session.get('count',0)
    count+=1
    request.session['count']=count
    request.session.set_expiry(120)#if Set session expiry to 0, ending the session when the browser is closed.
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,'testapp/pagecount.html',{'count':count})