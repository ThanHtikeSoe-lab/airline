from django.shortcuts import render,redirect
from oweapp.models import Travella,Airlines,Crew,Riskaction,Journeysearch
from django.contrib import messages
def create(request):
    return render(request,'travellar/create.html')

def store(request):
    travellar = Travella()
    travellar.id = request.POST.get('id')
    travellar.flight = request.POST.get('flight')
    travellar.timeframe = request.POST.get('timeframe')
    travellar.name = request.POST.get('name')
    travellar.dob = request.POST.get('dob')
    travellar.nrc = request.POST.get('nrc')
    travellar.gender = request.POST.get('gender')
    travellar.departureport = request.POST.get('departureport')
    travellar.departuredateandtime = request.POST.get('departuredateandtime')
    travellar.arrivalport = request.POST.get('arrivalport')
    travellar.arrivaldateandtime = request.POST.get('arrivaldateandtime')
    travellar.save()
    messages.success(request, "Travellar Added Successfully")
    return redirect('/travellar/index')

def index(request):
    travellar = Travella.objects.raw('SELECT * FROM oweapp_travella ')
    return render(request, 'travellar/index.html', {'travellar': travellar})


def updateview(request,pk):
    travellar=Travella.objects.get(id=pk)
    return render(request,'travellar/edit.html',{'travellar':travellar})

def update(request, pk):
    travellar = Travella.objects.get(id=pk)
    travellar.id = request.POST.get('id')
    travellar.flight = request.POST.get('flight')
    travellar.timeframe = request.POST.get('timeframe')
    travellar.name = request.POST.get('name')
    travellar.dob = request.POST.get('dob')
    travellar.nrc = request.POST.get('nrc')
    travellar.gender = request.POST.get('gender')
    travellar.departureport = request.POST.get('departureport')
    travellar.departuredateandtime = request.POST.get('departuredateandtime')
    travellar.arrivalport = request.POST.get('arrivalport')
    travellar.arrivaldateandtime = request.POST.get('arrivaldateandtime')
    travellar.save()
    messages.success(request, "Travellar Updated Successfully")
    return redirect('/travellar/index/')


def createairlines(request):
    return render(request,'Airlines/create.html')

def storeairlines(request):
    airlines = Airlines()
    airlines.id = request.POST.get('id')
    airlines.operatingdate = request.POST.get('operatingdate')
    airlines.airline = request.POST.get('airline')
    airlines.airlinenumber = request.POST.get('airlinenumber')
    airlines.departureport = request.POST.get('departureport')
    airlines.arrivalport = request.POST.get('arrivalport')
    airlines.departuredateandtime= request.POST.get('departuredateandtime')
    airlines.arrivaldateandtime = request.POST.get('arrivaldateandtime')
    airlines.flightstatus = request.POST.get('flightstatus')
    airlines.delayissues = request.POST.get('delayissues')
    airlines.remarks = request.POST.get('remarks')
    airlines.save()
    messages.success(request, "Airlines Added Successfully")
    return redirect('/Airlines/index')

def indexairlines(request):
    airlines = Airlines.objects.raw('SELECT * FROM oweapp_airlines ')
    return render(request, 'Airlines/index.html', {'airlines': airlines})


def updateviewairlines(request,pk):
    airlines=Airlines.objects.get(id=pk)
    return render(request,'Airlines/edit.html',{'airlines':airlines})

def updateairlines(request, pk):
    airlines= Airlines.objects.get(id=pk)
    airlines.id = request.POST.get('id')
    airlines.operatingdate = request.POST.get('operatingdate')
    airlines.airline = request.POST.get('airline')
    airlines.airlinenumber = request.POST.get('airlinenumber')
    airlines.departureport = request.POST.get('departureport')
    airlines.arrivalport = request.POST.get('arrivalport')
    airlines.departuredateandtime= request.POST.get('departuredateandtime')
    airlines.arrivaldateandtime = request.POST.get('arrivaldateandtime')
    airlines.flightstatus = request.POST.get('flightstatus')
    airlines.delayissues = request.POST.get('delayissues')
    airlines.remarks = request.POST.get('remarks')
    airlines.save()
    messages.success(request, "Airlines Updated Successfully")
    return redirect('/Airlines/index/')

def createcrew(request):
    return render(request,'Crew/create.html')

def storecrew(request):
    crew = Crew()
    crew.id = request.POST.get('id')
    crew.fligt= request.POST.get('fligt')
    crew.servicestatus = request.POST.get('servicestatus')
    crew.name= request.POST.get('name')
    crew.departureport = request.POST.get('departureport')
    crew.arrivalport = request.POST.get('arrivalport')
    crew.departuredateandtime= request.POST.get('departuredateandtime')
    crew.arrivaldateandtime = request.POST.get('arrivaldateandtime')
    crew.save()
    messages.success(request, "Crew Added Successfully")
    return redirect('/Crew/index/')

def indexcrew(request):
    crew = Crew.objects.raw('SELECT * FROM oweapp_crew ')
    return render(request, 'Crew/index.html', {'crew': crew})


def updateviewcrew(request,pk):
    crew=Crew.objects.get(id=pk)
    return render(request,'Crew/edit.html',{'crew':crew})

def updatecrew(request, pk):
    crew= Crew.objects.get(id=pk)
    crew.id = request.POST.get('id')
    crew.fligt= request.POST.get('fligt')
    crew.servicestatus = request.POST.get('servicestatus')
    crew.name= request.POST.get('name')
    crew.departureport = request.POST.get('departureport')
    crew.arrivalport = request.POST.get('arrivalport')
    crew.departuredateandtime= request.POST.get('departuredateandtime')
    crew.arrivaldateandtime = request.POST.get('arrivaldateandtime')
    crew.save()
    messages.success(request, "Crew Updated Successfully")
    return redirect('/Crew/index/')



def createriskaction(request):
    return render(request,'Riskaction/create.html')

def storeriskaction(request):
    riskaction =Riskaction()
    riskaction.id = request.POST.get('id')
    riskaction.no= request.POST.get('no')
    riskaction.name= request.POST.get('name')
    riskaction.dob = request.POST.get('dob')
    riskaction.father = request.POST.get('father')
    riskaction.passport= request.POST.get('passport')
    riskaction.gender= request.POST.get('gender')
    riskaction.nrc= request.POST.get('nrc')
    riskaction.nationality= request.POST.get('nationality')
    riskaction.status= request.POST.get('status')
    riskaction .save()
    messages.success(request, "Riskaction Added Successfully")
    return redirect('/Riskaction/index')

def indexriskaction(request):
    riskaction= Riskaction.objects.raw('SELECT * FROM oweapp_riskaction ')
    return render(request, 'Riskaction/index.html', {'riskaction': riskaction})


def updateviewriskaction(request,pk):
    riskaction=Riskaction.objects.get(id=pk)
    return render(request,'Riskaction/edit.html',{'riskaction':riskaction})

def updateriskaction(request, pk):
    riskaction= Riskaction.objects.get(id=pk)
    riskaction.id = request.POST.get('id')
    riskaction.no= request.POST.get('no')
    riskaction.name= request.POST.get('name')
    riskaction.dob = request.POST.get('dob')
    riskaction.father = request.POST.get('father')
    riskaction.passport= request.POST.get('passport')
    riskaction.gender= request.POST.get('gender')
    riskaction.nrc= request.POST.get('nrc')
    riskaction.nationality= request.POST.get('nationality')
    riskaction.status= request.POST.get('status')
    riskaction .save()
    messages.success(request, "Riskaction Updated Successfully")
    return redirect('/Riskaction/index/')


def createjourneysearch(request):
    return render(request,'Journeysearch/create.html')

def storejourneysearch(request):
   journeysearch=Journeysearch()
   journeysearch .id = request.POST.get('id')
   journeysearch.no= request.POST.get('no')
   journeysearch.name= request.POST.get('name')
   journeysearch.dob = request.POST.get('dob')
   journeysearch.father = request.POST.get('father')
   journeysearch.passport= request.POST.get('passport')
   journeysearch.gender= request.POST.get('gender')
   journeysearch.flightname= request.POST.get('flightname')
   journeysearch.sector= request.POST.get('sector')
   journeysearch.departuredateandtime= request.POST.get('departuredateandtime')
   journeysearch.arrivaldateandtime= request.POST.get('arrivaldateandtime')
   journeysearch.riskstatus= request.POST.get('riskstatus')
   journeysearch.save()
   messages.success(request,"Journeysearch Added Successfully")
   return redirect('/Journeysearch/index/')

def indexjourneysearch(request):
    journeysearch=Journeysearch.objects.raw('SELECT * FROM oweapp_journeysearch')
    return render(request, 'Journeysearch/index.html', {'journeysearch': journeysearch})


def updateviewjourneysearch(request,pk):
    journeysearch=Journeysearch.objects.get(id=pk)
    return render(request,'Journeysearch/edit.html',{'journeysearch':journeysearch})

def updatejourneysearch(request, pk):
    journeysearch=Journeysearch.objects.get(id=pk)
    journeysearch .id = request.POST.get('id')
    journeysearch.no= request.POST.get('no')
    journeysearch.name= request.POST.get('name')
    journeysearch.dob = request.POST.get('dob')
    journeysearch.father = request.POST.get('father')
    journeysearch.passport= request.POST.get('passport')
    journeysearch.gender= request.POST.get('gender')
    journeysearch.flightname= request.POST.get('flightname')
    journeysearch.sector= request.POST.get('sector')
    journeysearch.departuredateandtime= request.POST.get('departuredateandtime')
    journeysearch.arrivaldateandtime= request.POST.get('arrivaldateandtime')
    journeysearch.riskstatus= request.POST.get('riskstatus')
    journeysearch.save()
    messages.success(request, "Journeysearch Updated Successfully")
    return redirect('/Journeysearch/index/')