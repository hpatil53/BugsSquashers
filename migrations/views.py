from django.shortcuts import render, redirect
from .models import Pregnant_details,Child_details,
from django.contrib import messages
from django.db import connection
import mysql.connector
from myapp2.models import HWRegister
import random
import string
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.sessions.models import Session
from rest_framework.decorators import api_view
import json
from django.http.response import JsonResponse
from twilio.rest import Client
import twilio
import twilio.rest
from django.http import HttpResponse 

# Create your views here.
@api_view(['POST'])
def verifyotp(request):
    print("API WORKING")
    jsondata = json.loads(request.body)
    otp = jsondata['otp']
    userPhNo = jsondata['phno']
    print(otp)
    account_sid = 'AC0f63add1f07abcc3391022e9e6b0a770'
    auth_token = '71617382f5ac395c9e963e94785c4389'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Your OTP is "+str(otp),
        from_='+12058803829',
        to='+91' + str(userPhNo)
    )

    #send otp to userphno

    return JsonResponse({'status':200}, safe=False)




def index1(request):
    if request.session.has_key('is_logged') or request.session.has_key('is_hwlogged'):
        if request.session.has_key('is_hwlogged'):
            del request.session['is_hwlogged']
        else:
            del request.session['is_logged']
        return render(request, 'index1.html')
    return render(request, 'index1.html')
###############################################################
def hwlogin(request):
    return render(request,'hwlogin.html')
##############################################################

   
###############################################################

def adminlogin(request):

    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        if u == 'admin' and p == 'admin123':
            request.session['is_logged']=True
        
            return render(request, 'dashboard.html')
        else:
            return render(request, 'adminlogin.html',{'msg': "Invalid Username or password"})
    else:
        return render(request, 'adminlogin.html')
#################################################################
def registrationbase(request):
    if request.session.has_key('is_hwlogged'):
        return render(request, 'registrationbase.html')
    return render(request,'hwlogin.html')

    
    

###################################################################
def registration(request):
    
    if request.method=="POST":
        email = request.POST.get('hwemailid')
        password = request.POST.get('hwpassword')
        user = HWRegister.objects.get(hwemailid = email)
        if email == user.hwemailid and password == user.hwpassword :
            request.session['is_hwlogged']=True
            
            return render(request,'registration.html')
        else:
            context={'msg':'Inavlid username or password'}
            return render(request,'hwlogin.html',context)
    if request.session.has_key('is_hwlogged'):
        return render(request,'registration.html')  

    return render(request,'hwlogin.html')   
        



###################################################################
def v_base(request):

    return render(request, 'v_base.html')
####################################################################
def v_dashboard(request):
    if request.session.has_key('is_hwlogged'):
        return render(request, 'v_dashboard.html')
    return render(request,'index1.html')
####################################################################
def p_registration(request):
    if request.session.has_key('is_hwlogged'):
        if request.method == 'POST':
            p_register = Pregnant_details(p_fname=request.POST.get("p_fname"), p_lname=request.POST.get('p_lname'),
                                p_dob=request.POST.get('p_dob'),
                                p_email_id=request.POST.get('p_email_id'), p_phone_number=request.POST.get('p_phone_number'),
                                p_adhar_number=request.POST.get('p_adhar_number'), 
                                p_address=request.POST.get('p_address'),
                                p_pincode=request.POST.get('p_pincode'), state=request.POST.get('state'),
                                city=request.POST.get('city'),p_how_many_months_pregnant=request.POST.get('p_how_many_months_pregnant'),p_expected_delivery_date=request.POST.get('p_expected_delivery_date'))
            p_register.save()
            return render(request, 'p_registration.html')
        else:
            return render(request, 'p_registration.html')
    return render(request,'index1.html')
######################################################################
def c_registration(request):
    if request.session.has_key('is_hwlogged'):
        if request.method == 'POST':
            c_register = Child_details(c_fname=request.POST.get("c_fname"), c_lname=request.POST.get('c_lname'),
                                c_mname=request.POST.get('c_mname'),
                                c_gender=request.POST.get('c_gender'), c_dob=request.POST.get('c_dob'),
                                c_blood_group=request.POST.get('c_blood_group'), 
                                c_height=request.POST.get('c_height'),
                                c_weight=request.POST.get('c_weight'),c_category=request.POST.get('c_category'),
                                c_email_id=request.POST.get('c_email_id'),c_mobile_num=request.POST.get('c_mobile_num'),
                                c_address=request.POST.get('c_address'),c_pincode=request.POST.get('c_pincode'), 
                                state=request.POST.get('state'),
                                city=request.POST.get('city'),c_adhar_number=request.POST.get('c_adhar_number'))
            c_register.save()
            return render(request, 'c_registration.html')
        else:
            return render(request, 'c_registration.html')
    return render(request,'index1.html')  
##########################################################################
def p_update(request):
    if request.session.has_key('is_hwlogged'):
        if request.method == 'POST':
            pstaff = Pregnant_details.objects.get(pk = request.POST.get('p_id'))
            pstaff.p_fname = request.POST.get('p_fname')
            pstaff.p_lname = request.POST.get('p_lname')
            pstaff.p_dob = request.POST.get('p_dob')
            pstaff.p_email_id = request.POST.get('p_email_id')
            pstaff.p_phone_number = request.POST.get('p_phone_number')
            pstaff.p_adhar_number = request.POST.get('p_adhar_number')
            pstaff.p_address = request.POST.get('p_address')
            pstaff.p_pincode = request.POST.get('p_pincode')
            pstaff.state = request.POST.get('state')
            pstaff.city = request.POST.get('city')
            pstaff.p_how_many_months_pregnant = request.POST.get('p_how_many_months_pregnant')
            pstaff.p_expected_delivery_date = request.POST.get('p_expected_delivery_date')

            pstaff.save()
            pregnant = Pregnant_details.objects.all()
            context = {
                "data": pregnant
            }
            return render(request, 'p_update.html', context)
        else:
            pregnant = Pregnant_details.objects.all()
            context = {
                "data": pregnant
            }
            return render(request, 'p_update.html', context)
    return render(request,'index1.html')
####################################################################



#####################################################################

def chartTest(request):
    if request.method == 'POST':
        c_id=request.POST['c_id']
        childRS= Child_details.objects.get(c_id=c_id)
        c_dob=childRS.c_dob
       
        
        with connection.cursor() as cursor:
            query="SELECT vm_id,group_id, v_name, '"+str(c_dob)+"' + INTERVAL days_after_birth day as nxt_dt from vaccine_master"
            #RS=connection.cursor().execute(query)
            cursor.execute(query)
            resultSet = cursor.fetchall()
            print(resultSet)
        # c_id=request.POST['c_id']
        # childDetailRS=Vaccine_master.objects.filter(vm_id,group_id,v_name,days_after_birth)
        # print(childDetailRS)
        # dob="2020-01-01"
        
        context = {
            'child': childRS,
            "data": resultSet
        }
        return render(request, 'chartTest.html', context)
    else:
        return render(request, 'chartTest.html')

        
        

#####################################################################
#####################################################################
def v_missed(request):
    return render(request, 'v_missed.html')
######################################################################
def v_complete(request):
    return render(request, 'v_complete.html')
######################################################################
def c_update(request):
    if request.session.has_key('is_hwlogged'):
        if request.method == 'POST':
            cstaff = Child_details.objects.get(pk = request.POST.get('c_id'))
            cstaff.c_fname = request.POST.get('c_fname')
            cstaff.c_lname = request.POST.get('c_lname')
            cstaff.c_mname = request.POST.get('c_mname')
            cstaff.c_gender= request.POST.get('c_gender')
            cstaff.c_dob = request.POST.get('c_dob')
            cstaff.c_blood_group = request.POST.get('c_blood_group')
            cstaff.c_height = request.POST.get('c_height')
            cstaff.c_weight = request.POST.get('c_weight')
            cstaff.c_category = request.POST.get('c_category')
            cstaff.c_email_id = request.POST.get('c_email_id')
            cstaff.c_mobile_num = request.POST.get('c_mobile_num')
            cstaff.c_address = request.POST.get('c_address')
            cstaff.c_pincode = request.POST.get('c_pincode')
            cstaff.state = request.POST.get('state')
            cstaff.city = request.POST.get('city')
            cstaff.c_adhar_number = request.POST.get('c_adhar_number')
            cstaff.save()
            child = Child_details.objects.all()
            context = {
                "data": child
            }
            return render(request, 'c_update.html', context)
        else:
            child = Child_details.objects.all()
            context = {
                "data": child
            }
            return render(request, 'c_update.html', context)
    return render(request,'index1.html')
###################################################################
def p_details(request):
    pregnant = Pregnant_details.objects.all()
    context = {
        "data": pregnant
    }
    return render(request, 'p_details.html', context)
####################################################################
def delete_p_details(request, p_id):
    iid = Pregnant_details.objects.get(pk = p_id)
    iid.delete()
    pregnant = Pregnant_details.objects.all()
    context = {
            "data": pregnant
        }
    return render(request, 'p_update.html', context)
####################################################################
def edit_p_details(request, p_id):
    iid = Pregnant_details.objects.get(pk = p_id)
    return render(request, 'edit_p_details.html', {"data" : iid})
###################################################################
def delete_c_details(request, c_id):
    iid = Pregnant_details.objects.get(pk = c_id)
    iid.delete()
    child = Child_details.objects.all()
    context = {
            "data": child
        }
    return render(request, 'c_update.html', context)
#####################################################################
def edit_c_details(request, c_id):
    iid = Child_details.objects.get(pk = c_id)
    return render(request, 'edit_c_details.html', {"data" : iid})

####################################################################
def n_base(request):
    return render(request, 'n_base.html')
##################################################################
def n_dashboard(request):
    if request.session.has_key('is_hwlogged'):
        return render(request, 'n_dashboard.html')
    return render(request,'index1.html')
##################################################################
def checkin_nutrition(request):
    if request.session.has_key('is_hwlogged'):
        return render(request, 'checkin_nutrition.html')
    return render(request,'index1.html')
##################################################################
def n_upcoming(request):
    return render(request, 'n_upcoming.html')
##################################################################
def n_missed(request):
    return render(request, 'n_missed.html')
##################################################################
def n_complete(request):
    return render(request, 'n_complete.html')
###################################################################

    

###################################################################
def childnutrition(request):
    return render(request, 'childnutrition.html')
#####################################################################
def womennutrition(request):
    return render(request, 'womennutrition.html')
#####################################################################





    #############################################################

