from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
from twilio.rest import Client
from myapp.models import Vaccine_trx,Nutrition_trx_child ,Nutrition_trx_women    #(models kaa app name )
import datetime


@shared_task

def child_vaccine_broadcast_sms():

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    dateid =Vaccine_trx.objects.all()
    
    list_number =[]
    for item in dateid: 
       #27 -1 = 28 -26 =2  ### 
        a = item.next_vaccine_date - datetime.date.today() 
        print(item.next_vaccine_date)
        print(datetime.date.today())
        print(a.days)
        
        b = datetime.date.today()-item.next_vaccine_date
        print(b.days)
        if a.days <= 2:## todays messaging
        # 27 -25 =2 #27- 26=1
             client.messages.create(to= '+919699078422',
                                    from_=settings.TWILIO_NUMBER ,
                                    body="You have an upcoming appointment"
                                    )

        elif b.days < 2 :  #missed
        ## 29-27=1  27-27=0
            client.messages.create(to='+918169595773',
                                   from_=settings.TWILIO_NUMBER ,
                                   body="You have missed an appointment "
                                   )

        else:
            return "errors"

    return 'Done child vaccine'    



@shared_task
def every_month_1st_date() :
    #all taken rows set to false
    child_n = Nutrition_trx_child.objects.all()
    women_n = Nutrition_trx_women.objects.all()
    for item in child_n:
        item.taken_c = False
        return item.save()

    for item in women_n:
        item.taken_w = False
        return item.save()

    return 'Done'



'''
Column in database
taken-- true or false
'''
@shared_task
def child_run_every_monday():
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    child_n = Nutrition_trx_child.objects.all()
    
    for item in child_n:
        if(item.taken_c == True ):
        
            return 'already taken ' 
        else:
            client.messages.create(to='+91'+ str(item.pc_phone_number),
                                   from_c=settings.TWILIO_NUMBER ,
                                   body="Current month nurtition have been assigned. Please take as soon as poosible!"
            )
            return 'Done Monday child'    

    return 'Done'                              

@shared_task   
def women_run_every_monday():
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    
    women_n = Nutrition_trx_women.objects.all()
    for item in women_n:
        if(item.taken_w == True):
        
            return 'already taken ' 
        else:
            client.messages.create(to= '+91'+ str( item.pw_phone_number),
                                   from_=settings.TWILIO_NUMBER ,
                                   body="Current month nurtition have been assigned. Please take as soon as poosible!"
                                   )
            return 'Done Monday women'


    return 'Done'            
#####'
#1. Every MOnday Scheduler Run Hoga
#2. Counter jo track karega month ko
#3. agar mmonth complete hua toh reset
#4. ek column rahega jissme track hoga ki usne nutrition liya ya nahi

