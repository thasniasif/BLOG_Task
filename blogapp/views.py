from django.shortcuts import render,loader,HttpResponse
from .models import Post

# Create your views here.
def index(request):
    p=Post.objects.order_by('-date')
    for i in p:
        l=i.content
        i.content_slice=l[0:200]+'......'
        # print(i.content_slice)
        i.save()
        # print(l[:5])
    # q=Post.objects.get()

    context={
        'p' : p,

    }

    template = loader.get_template('index.html')



    return HttpResponse(template.render(context,request))

def next_page(request,id):
    p=Post.objects.filter(id=id)
    # for i in p:
    #     print(i.title)

    return render(request,'next_page.html',{'p' : p})


