from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main.models import UserCredential, User, Billing
from main.app import add_details,get_details

import datetime

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')

    else:
        name = request.POST.get('id')
        password = request.POST.get('password')

        uc = UserCredential.objects.filter(username=name, password=password).first()
    
        if uc:
            return HttpResponseRedirect('/register')

        
def data_page(request):
    if request.method == 'GET':
        user_information = User.objects.all()
        UserKey = ['Full Name',
               'Date of Birth',
               'Email Address',
               'Phone Number',
               'Gender',
               'Address',
               'Identity Type',
               'Identity Number',
               'Issued Date of Illness',
               'Issued date of Hospitalization',
               'Issued Doctor',
               'Illness']

        user_dict = dict.fromkeys(UserKey,'')
        BillingKey = ['Identity Number',
                      'Payment Option',
                      'Total Charge',
                      'Amount Paid',
                      'Balance Due',
                      'Billing Program Information',
                      'Insurance Holder\'s Group Number',
                      'Insurance Holder\'s Full Name',
                      'Insurance Holder\'s Gender',
                      'Insurance Holder\'s Address',
                      'Insurance Holder\'s Phone',
                      'Insurance Holder\'s Program'
                      ]

        bill_dict = dict.fromkeys(BillingKey, '')
        full_dict = {'usertype': 'Users Information',
                     'billtype': 'Billing Information',
                     'user_dict': user_dict,
                     'bill_dict': bill_dict,
                     'userinfo': user_information}
        return render(request, 'info.html', full_dict)
    else:

        user_id = request.POST.get('users')
        user_info = User.objects.all()
        for data in user_info:
            if user_id in data.id_number:
                uname = data.name
        
        UserKey = ['Full Name',
               'Date of Birth',
               'Email Address',
               'Phone Number',
               'Gender',
               'Address',
               'Identity Type',
               'Identity Number',
               'Issued Date of Illness',
               'Issued date of Hospitalization',
               'Issued Doctor',
               'Illness']

        user_information = User.objects.filter(id_number=user_id).first()
        user_value = list(user_information.__dict__.values())[1:]

        user_dict = dict(zip(UserKey, user_value))

        BillingKey = ['Identity Number',
                      'Payment Option',
                      'Total Charge',
                      'Amount Paid',
                      'Balance Due',
                      'Billing Program Information',
                      'Insurance Holder\'s Group Number',
                      'Insurance Holder\'s Full Name',
                      'Insurance Holder\'s Gender',
                      'Insurance Holder\'s Address',
                      'Insurance Holder\'s Phone',
                      'Insurance Holder\'s Program'
                      ]

        bill_information = Billing.objects.filter(id_number=user_id).first()
        bill_value = list(bill_information.__dict__.values())[2:]
        blockchain_details = get_details (int(user_id))
        bill_value[2]= blockchain_details[0]
        bill_value[3]= blockchain_details[1]
        bill_value[4]= blockchain_details[2]
        print(bill_value)
        print(get_details (int(user_id)))
        bill_dict = dict(zip(BillingKey, bill_value))
        print(bill_dict)
        full_dict = {'usertype': 'Users Information',
                     'billtype': 'Billing Information',
                     'user_dict': user_dict,
                     'bill_dict': bill_dict,
                     'userinfo': user_info,
                     'user': uname}

        return render(request, 'info.html', full_dict)


    
    

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    
    name = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    full_name = request.POST['fname']

    uc = UserCredential(username=name, fname=full_name, user_email=email, password=password)
    uc.save()
    if uc:
        return HttpResponseRedirect('/')

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

    request.session['id_num'] = idnum
    
    return HttpResponseRedirect(f'/billing')
    

def billing(request):
    
    if request.method == 'GET':
        id_num = request.session['id_num']
        
        details = User.objects.filter(id_number=id_num).first()
        data = {'id_num': id_num,
                'fname': details.name,
                'gender': details.gender,
                'address': details.address,
                'mobile': details.mobile}
        return render(request, 'billing.html', data)

    else:
        user = User.objects.get(id_number=request.session['id_num'])
        id_num = user
        id=request.POST['id_num']
        payment = request.POST['payment']
        total = request.POST['charge']
        amount_paid = request.POST['amountpaid']
        balance_due = request.POST['balancedue']
        billing_prov = request.POST['billinginfo']
        program = request.POST['program']

        name = request.POST['fullname']
        gender = request.POST['gender']
        address = request.POST['address']
        phone = request.POST['phone_num']
        groupid = request.POST['policy_group']
    
        add_details (int(id),int(total),int(amount_paid),int(balance_due))
        print(id,total,amount_paid,balance_due)
    
        bill = Billing(id_number    = id_num,
                   payment_option   = payment,
                   total_charge     = total,
                   amt_paid         = amount_paid,
                   bal_due          = balance_due,
                   billing_pro_info = billing_prov,
                   ins_group_no     = groupid,
                   ins_fname        = name,
                   ins_gender       = gender,
                   ins_address      = address,
                   ins_mobile       = phone,
                   ins_plan_prog    = program)

    
        del request.session['id_num']
        bill.save()
        return HttpResponseRedirect('/')

