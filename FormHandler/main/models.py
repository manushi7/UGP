from django.db import models

# Create your models here.

class UserCredential(models.Model):

	id_user    = models.AutoField(primary_key=True, default=None)
	username   = models.CharField(max_length = 30)
	fname      = models.CharField(max_length = 100, default=None)
	user_email = models.CharField(max_length = 100, default=None)
	password   = models.CharField(max_length = 15)
	
	class Meta:
		db_table = "UserCredentials"

class User(models.Model):

	name          = models.CharField(max_length = 100)
	dob           = models.DateField()
	email         = models.EmailField()
	mobile        = models.BigIntegerField()
	gender        = models.CharField(max_length = 6)
	address       = models.CharField(max_length = 100)
	id_type       = models.CharField(max_length = 25)
	id_number     = models.CharField(primary_key=True,max_length = 15, unique=True)
	issued_do_ill = models.DateField()
	issued_do_hos = models.DateField()
	doc_name      = models.CharField(max_length = 100)
	diagnosis     = models.TextField()
	
	class Meta:
		db_table = "User"

class Billing(models.Model):

	# Billing Details
	id_bill          = models.AutoField(primary_key=True, default=None)   
	id_number        = models.OneToOneField("User", on_delete=models.CASCADE, unique=True)
	payment_option   = models.CharField(max_length=20)
	total_charge     = models.FloatField()
	amt_paid         = models.FloatField()
	bal_due          = models.FloatField()
	billing_pro_info = models.CharField(max_length=100)
	
	# Insured Details
	ins_group_no  = models.IntegerField()
	ins_fname     = models.CharField(max_length = 200)
	ins_gender    = models.CharField(max_length = 7)
	ins_address   = models.CharField(max_length = 100)
	ins_mobile    = models.BigIntegerField()
	ins_plan_prog = models.CharField(max_length = 100)


	class Meta:
		db_table = "Billing"
