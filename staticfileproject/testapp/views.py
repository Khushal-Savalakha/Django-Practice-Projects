from django.shortcuts import render

# Create your views here.
def show_images(request):
    return render(request,'show_image.html')


def index_views(request):
    return render(request,'index.html')

def movie_review(request):
    head_msg='Movies Information'
    sub_msg1='RRR ready to release'
    sub_msg2='Background support must be required to get change'
    sub_msg3='Indian cine industry struggling like anything with covid'
    sub_msg4='Biggest benefit of covid for industry:OTT'
    sub_msg5='Written by SKJ'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'sub_msg4':sub_msg4,'sub_msg5':sub_msg5}
    return render(request,'demo.html',my_dict)
