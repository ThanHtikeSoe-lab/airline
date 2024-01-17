from django.db import models

# Create your models here.
class Airlines(models.Model):
    id=models.CharField(primary_key=True,max_length=100)
    operatingdate=models.CharField(max_length=100)
    airline=models.CharField(max_length=100)
    airlinenumber=models.IntegerField() 
    departureport=models.CharField(max_length=100)
    arrivalport=models.CharField(max_length=100)
    departuredateandtime=models.CharField(max_length=100)
    arrivaldateandtime=models.CharField(max_length=100)
    flightstatus=models.CharField(max_length=100) 
    delayissues=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100) 



class Travella(models.Model):
    id=models.CharField(primary_key=True,max_length=100)
    flight=models.CharField(max_length=100)
    timeframe=models.CharField(max_length=100)
    name =models.CharField(max_length=100)
    dob=models.DateField()
    nrc=models.CharField(max_length=100)
    gender =models.CharField(max_length=100)
    departureport =models.CharField(max_length=100)
    departuredateandtime=models.CharField(max_length=100)
    arrivalport=models.CharField(max_length=100)
    arrivaldateandtime=models.CharField(max_length=100)

    
              
status_choice=(('approved','APPROVED'),('pending','PENDING'),
               ('rejected','REJECTED'))
class Riskaction(models.Model):
    id=models.CharField(primary_key=True,max_length=100)
    no=models.IntegerField() 
    name=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    father=models.CharField(max_length=100) 
    passport=models.CharField(max_length=100) 
    gender=models.CharField(max_length=100)
    nrc=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100) 
    status =models.CharField(max_length=100)
  

riskstatus_choice=(('approved','APPROVED'),('pending','PENDING'),
               ('rejected','REJECTED'))


class Crew(models.Model ):
      id=models.CharField(primary_key=True,max_length=100)
      fligt=models.CharField(max_length=100)
      servicestatus=models.CharField(max_length=100) 
      name=models.CharField(max_length=100)
      departureport=models.CharField(max_length=100)
      arrivalport=models.CharField(max_length=100)
      departuredateandtime=models.CharField(max_length=100)
      arrivaldateandtime=models.CharField(max_length=100)
     
     
        
      
riskstatus_choice=(('approved','APPROVED'),('pending','PENDING'),
               ('rejected','REJECTED'))


class Journeysearch(models.Model):
     id=models.CharField(primary_key=True,max_length=100)
     no=models.IntegerField()
     name=models.CharField(max_length=100)
     dob=models.CharField(max_length=100)
     father= models.CharField(max_length=100)
     passport =models.CharField(max_length=100)
     gender =models.CharField(max_length=100)
     flightname =models.CharField(max_length=100)
     sector =models.CharField(max_length=100)
     departuredateandtime=models.CharField(max_length=100)
     arrivaldateandtime =models.CharField(max_length=100)
     riskstatus =models.CharField(max_length=100)
    
    

    