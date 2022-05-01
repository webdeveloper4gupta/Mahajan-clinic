
from django.shortcuts import render,HttpResponse
from .models import doctor,patient
from .forms import patientform
from django.contrib import messages
from hospital import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,"home.html")

def patients(request):
    forms=patientform()
    if request.method=="POST":
        n1=request.POST.get('name')
        n2=request.POST.get('email')
        n3=request.POST.get('phno')
        n4=request.POST.get('Disease')
        n5=request.POST.get('Description')
        n6=request.POST.get('password')
        try:
            if patient.objects.get(password=n6):
                messages.error(request,"please try another password")
                return render(request,"patient.html",{'forms':forms})
               
                
        except:
            pat=patient(name=n1,email=n2,phno=n3,Disease=n4,Description=n5,password=n6)
            pat.save()

           
           
        # here i set email
        
            subject="Welcome to mahajan clinic"
            message="hello"+pat.name+"I hope you are doing well "+ " "+"Your request for appoint mnet with {{n4}} specialist has been setup."+" "+"please visit in time"+" "+"Thank you"
            from_email=settings.EMAIL_HOST_USER
            to_email=[pat.email]
            send_mail(subject,message,from_email,to_email,fail_silently=True)

            return render(request,"details1.html",{"name":n1})
    return render(request,"patient.html",{'forms':forms})
def doctors(request):
    if request.method=="POST":
        n1=request.POST.get('email')
        n2=request.POST.get('password')
        
        try:
            if doctor.objects.get(email=n1,password=n2):
                n=patient.objects.all()
                n10=doctor.objects.get(email=n1,password=n2)
                
                return render(request,"data.html",{'patient':n,'doctor':n10})
        except:
            messages.error(request,message="invalid credentials")
    return render(request,"details.html")

def admin(request):
    if request.method=="POST":
        n1=request.POST.get('name')
        n2=request.POST.get('email')
        
        try:
            if User.objects.get(username=n1,email=n2):        
                n=doctor.objects.all()
                return render(request,"administrator.html",{"doctor":n,})
        except:

            messages.error(request,message="invalid credentials")
            
    return render(request,"adminpanel.html")

def appoint(request):
    if request.method=="POST":
        n1=request.POST.get('password')
        if n1:
            try :
                if patient.objects.get(password=n1):

                    user=patient.objects.get(password=n1)
                    return render(request,'appointment1.html',{"cand":user})
            except:
                 messages.error(request,"invalid credentials")

        else:
            messages.error(request,"invalid credentials")
    return render(request,'appointment.html')

def remove_cand(request,cand_id=0):
     if cand_id:
        try:
            cand_to_be_removed=patient.objects.get(id=cand_id)
            cand_to_be_removed.delete()
            # here i setup email
            subject="Welcome to mahajan clinic online service"
            message="hello"+cand_to_be_removed.name+" I Hope you are doing well"+" "+"As your request your appointment has been cancelled " +" "+"Thank you"
            from_email=settings.EMAIL_HOST_USER
            to_email=[cand_to_be_removed.email]
            send_mail(subject,message,from_email,to_email,fail_silently=True)
            return render(request,"remove.html")
        except:
            return HttpResponse("NNOT EXIST USER")
