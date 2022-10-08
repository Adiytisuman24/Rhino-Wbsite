from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
   # return HttpResponse("This is my homepage(/)")
   return render(request,'home.html')

def about(request):
    #return HttpResponse("This is my aboutpage(/about)")
    return render(request,'about.html')

def Courses(request):
    #return HttpResponse("This is my Coursespage(/Courses)")
    return render(request,'Courses.html')

def Learn(request):
    #return HttpResponse("This is my Learnpage(/Learn)")
    return render(request,'Learn.html')

def Tests(request):
    #return HttpResponse("This is my Testspage(/Tests)")
    return render(request,'Tests.html')    

def Connect(request):
    #return HttpResponse("This is my Connectpage(/Connect)")
    return render(request,'Connect.html')

def base(request):
    #return HttpResponse("This is my basepage(/base)")
    return render(request,'request.html')

def navbar(request):
    #return HttpResponse("This is my navbarpage(/navbar)")
    return render(request,'navbar.html')

def checkout(request):
    #return HttpResponse("This is my checkoutpage(/checkout)")
    return render(request,'checkout.html')
    
def footer(request):
    #return HttpResponse("This is my footerpage(/footer)")        
    return render(request,'footer.html')    