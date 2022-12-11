from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main.models import UserCredential, User, Billing

import datetime

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')

    else:
        name = request.POST.get('id')
        password = request.POST.get('password')

        print(name, password)
        uc = UserCredential.objects.filter(username=name, password=password).first()
        print(uc.username, uc.password)
    
        if uc:
            return HttpResponseRedirect('/register')

		
def data_page(request):
    if request:
        return HttpResponse(f"<h1>With Data{request}</h1>") 
    return HttpResponse("<h1>Hello</h1>")

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    
    name = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    full_name = request.POST['fname']

    print(name, password, email, full_name)

    uc = UserCredential(username=name, fname=full_name, user_email=email, password=password)
    uc.save()
    if uc:
        return render(request, 'index.html') 

def register(request):

	if request.method == 'GET':
		return render(request, 'register.html')

	fname = request.POST['fname']
	dob = request.POST['dob']
	email = request.POST['email']
	mobile = request.POST['mobile']
	gender = request.POST['gender']
	address = request.POST['address']
	idtype = request.POST['idtype']
	idnum = request.POST['idnum']
	issued_date_illness = request.POST['issued_date_illness']
	issued_date_hospital = request.POST['issued_date_hospital']
	issued_doctor = request.POST['issued_doctor']
	illness = request.POST['illness']

	dob_dt = datetime.datetime.strptime(dob, '%Y-%m-%d')
	date_dob = datetime.date(dob_dt.year, dob_dt.month, dob_dt.day)

	idi_db = datetime.datetime.strptime(issued_date_illness, '%Y-%m-%d')
	date_idi = datetime.date(idi_db.year, idi_db.month, idi_db.day)

	idh_db = datetime.datetime.strptime(issued_date_hospital, '%Y-%m-%d')
	date_idh = datetime.date(idh_db.year, idh_db.month, idh_db.day)


	usr = User(name          = fname,
			   dob           = date_dob,
			   email         = email,
			   mobile        = mobile,
			   gender        = gender,
			   address       = address,
			   id_type       = idtype,
			   id_number     = idnum,
			   issued_do_ill = date_idi,
			   issued_do_hos = date_idh,
			   doc_name      = issued_doctor,
			   diagnosis     = illness)

	usr.save()
	
	return HttpResponseRedirect('/billing')
    

def billing(request):
	if request.method == 'GET':
		return render(request, 'billing.html')

	
