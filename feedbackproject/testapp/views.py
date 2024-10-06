from django.shortcuts import render
from testapp.forms import FeedBackForm
# Create your views here.

# def feedback_view(request):
#     submitted=False
#     name=''
#     if request.method=='POST':
#         form=FeedBackForm(request.POST)
#         if form.is_valid():
#             print('Form Validation Successfull Printing feedback Information')
#             print('#'*30)
#             print('Name:',form.cleaned_data['name'])
#             print('RollNo:',form.cleaned_data['rollno'])
#             print('MailId:',form.cleaned_data['email'])
#             print('Feedback:',form.cleaned_data['feedback'])
#             submitted=True
#             name=form.cleaned_data['name']
#         else:
#             print('DATA INVALID ERROR!!!')
#     form=FeedBackForm()
#     return render(request,'testapp/feedback.html',{'form':form,'submitted':submitted,'name':name})
def feedback_view(request):
    form=FeedBackForm()
    submitted=False
    name=''
    if request.method=='POST':
        form=FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Successfull Printing feedback Information')
            print('#'*30)
            print('Name:',form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('MailId:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted=True
            name=form.cleaned_data['name']
        else:
            print('DATA INVALID ERROR!!!')
    # form=FeedBackForm()
    return render(request,'testapp/feedback.html',{'form':form,'submitted':submitted,'name':name})

