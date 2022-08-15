from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from .models import User

def showformdata(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print(nm)
            print(em)
            print(pw)
            # reg = User(name=nm,firstname=fn,email=em,password=pw)
            # reg.save()
        else:
            print('Invalid')
    else:
        fm = StudentRegistration()
    return render(request,'enroll/userregistration.html',{'form':fm})

def studentdetails(request,my_id):
    return render(request,'enroll/student.html',{'id': my_id})