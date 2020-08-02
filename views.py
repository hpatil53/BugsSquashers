
from django.conf import settings                          
from django.http import HttpResponse                      
from .tasks import child_vaccine_broadcast_sms, child_nutrition_broadcast_sms,lady_nutrition_broadcast_sms        
from django.shortcuts import render, redirect



# def vaccine_sms(request):
#     child_vaccine_broadcast_sms.delay()
#     return HttpResponse("messages sent!", 200)

# def child_nutrition_sms(request):
#     child_nutrition_broadcast_sms.delay()
#     return HttpResponse("messages sent!", 200)

# def lady_nutrition_sms(request):
#     lady_nutrition_broadcast_sms.delay()
#     return HttpResponse("messages sent!", 200)






from django.shortcuts import render

# Create your views here.
