from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about-us.html')

def services(request):
    return render(request, 'home/service.html')

def contact(request):
    return render(request, 'home/contact-us.html')

# def blog(request):
#     return render(request, 'home/blog.html')