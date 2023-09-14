from django.shortcuts import render,redirect
from hospitalapp.models import Doctor,Patient

def Login(request):
    return render(request,'login.html',{})
def Logincheck(request):
    user=request.POST['username']
    password=request.POST['password']
    if user=='Pardhiv' and password=='Pachu':
        return render(request,'admin.html',{})
    elif user!='Pardhiv':
        doctor=Doctor.objects.get(username=user)
        if doctor.password==password:
            pats=Patient.objects.all()
            context= {
            'pats':pats
            }
            return render(request=request,template_name='doctor.html',context=context)
        else:
            return render(request,'admin.html',{})
    else:
        return render(request,'admin.html',{})
def Admin(request):
    return render(request,'admin.html',{})
def AddDoctor(request):
    return render(request,'adddoc.html',{})
def DelDoctor(request,doc_id):
    doctor=Doctor.objects.filter(pk=doc_id)
    doctor.delete()
    return redirect('alldoc')
def AllDoctor(request):
    drs=Doctor.objects.all()
    context= {
        'drs':drs
    }
    return render(request=request,template_name='alldoc.html',context=context)
def savedoc(request):
    if request.method=="POST":
        name=request.POST['name']
        did=request.POST['did']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        ph=request.POST['ph']
        password=request.POST['password']
        username=request.POST['username']
        print("Name: ",name)
        print("Address: ",address)
        print("Email: ",email)
        print("department: ",department)
        doctor=Doctor(name=name,address=address,email=email,department=department,dphno=ph,did=did,username=username,password=password)
        doctor.save()
    return redirect('alldoc')
def savepat(request):
    if request.method=="POST":
        name=request.POST['name']
        pid=request.POST['pid']
        address=request.POST['address']
        cause=request.POST['cause']
        ph=request.POST['pphno']
        print("Name: ",name)
        print("Address: ",address)
        print("cause: ",cause)
        patient=Patient(name=name,address=address,cause=cause,pphno=ph,pid=pid)
        patient.save()
    return redirect('allpat')
def AddPatient(request):
    return render(request,'addpat.html',{})
def DelPatient(request,pat_id):
    patient=Patient.objects.filter(pk=pat_id)
    patient.delete()
    return redirect('allpat')
def AllPatient(request):
    pats=Patient.objects.all()
    context= {
        'pats':pats
    }
    return render(request=request,template_name='allpat.html',context=context)
def AllPatientdoc(request):
    pats=Patient.objects.all()
    context= {
        'pats':pats
    }
    return render(request=request,template_name='doctor.html',context=context)
def singlepat(request,pat_id):
    patient=Patient.objects.get(pk=pat_id)
    context={
        'pat':patient
    }
    return render(request=request,template_name='singlepat.html',context=context)
def singlepatdoc(request,pat_id):
    patient=Patient.objects.get(pk=pat_id)
    context={
        'pat':patient
    }
    return render(request=request,template_name='singlepatdoc.html',context=context)
def singledoc(request,doc_id):
    doctor=Doctor.objects.get(pk=doc_id)
    context={
        'doc':doctor
    }
    return render(request=request,template_name='singledoc.html',context=context)
def updatedoc(request,doc_id):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        department=request.POST['department']
        did=request.POST['did']
        password=request.POST['password']
        username=request.POST['username']
        print("Name: ",name)
        print("Address: ",address)
        print("Email: ",email)
        doctor=Doctor.objects.get(pk=doc_id)
        doctor.name=name
        doctor.department=department
        doctor.address=address
        doctor.email=email
        doctor.username=username
        doctor.password=password
        doctor.did=did
        doctor.save()
    return redirect('alldoc')
def updatepat(request,pat_id):
    if request.method=="POST":
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        cause=request.POST['cause']
        pid=request.POST['pid']
        print("Name: ",name)
        print("Address: ",address)
        print("Email: ",email)
        patient=Patient.objects.get(pk=pat_id)
        patient.name=name
        patient.cause=cause
        patient.address=address
        patient.pid=pid
        patient.save()
    return redirect('all')
def singlepat(request,pat_id):
    patient=Patient.objects.get(pk=pat_id)
    context={
        'pat':patient
    }
    return render(request=request,template_name='singlepatdoc.html',context=context)