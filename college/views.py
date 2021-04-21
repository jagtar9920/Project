#created by Jagtar SIngh

from django.shortcuts import render,HttpResponse, redirect
from .models import Appointment
from .forms import appointmentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def symptoms(request):
    return render(request, 'symptoms.html')

def prevention(request):
    return render(request, 'prevention.html')

def hospitals(request):
    return render(request, 'hospitals.html')

def displayForm(request):
    form = appointmentForm
    return render(request,'insert.html',{'form':form})

def BookAppointment(request):
    form = appointmentForm(request.POST)
    form.save()
    return redirect('/showAppointment')

def showAppointment(request):
    aptmnt = Appointment.objects.all
    return render (request,'table.html',{'aptmnt':aptmnt})

def edit(request,id):

    aptmnt = Appointment.objects.get(std_id=id)

    return render (request , 'edit.html',{'aptmnt':aptmnt})

def update(request,id):

    aptmnt = Appointment.objects.get(std_id=id)

    form = appointmentForm(request.POST, instance = aptmnt)  

    form.save()

    return redirect('/showAppointment')


def delete(request,id):

    aptmnt = Appointment.objects.get(std_id=id)

    aptmnt.delete()

    return redirect('/showAppointment')


