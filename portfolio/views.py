from django.shortcuts import render

# Create your views here.
def fontend(request):
    context = {
        'page_obj': 'hello',
    }

    return render(request, 'blog_temp/index.html')