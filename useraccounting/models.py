#useraccoun name changed to useraccounting but in cpanel/server it's same as useraccount

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from datetime import datetime

class MyAccountManager(BaseUserManager):
	def create_user(self, username, password=None,**kwargs):
		# if not email:
		# 	raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			#email=self.normalize_email(email),
			username=username,**kwargs
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password):
		user = self.create_user(
			#email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	fullname 				= models.CharField(max_length=50)
	username 				= models.CharField(max_length=30, unique=True)
	password 				= models.CharField(max_length=100)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	is_superadmin 			= models.BooleanField(default=False)
	is_startup 				= models.BooleanField(default=False)
	is_adminstrator			= models.BooleanField(default=False)
	is_sanvriddhi			= models.BooleanField(default=False)
	is_ideanest_check		= models.BooleanField(default=False)
	is_viewer				= models.BooleanField(default=False)
	is_ideanest_viewer		= models.BooleanField(default=False)
	rank					= models.CharField(max_length=100,null=True,blank=True)
	




	USERNAME_FIELD = 'username'

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True



class Admin(models.Model):
	account 				= models.ForeignKey(Account, on_delete=models.CASCADE)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	designation				= models.CharField(max_length=100,null=True,blank=True)
	employee_id				= models.CharField(max_length=100,null=True,blank=True)
	contact_no				= models.CharField(max_length=100,null=True,blank=True)
	identity_proof			= models.CharField(max_length=100,null=True,blank=True)
	cl						= models.CharField(max_length=100,null=True,blank=True)
	sl						= models.CharField(max_length=100,null=True,blank=True)
	admin_img				= models.ImageField(upload_to='images/',null=True,blank=True)
	ranks					= models.CharField(max_length=100,null=True,blank=True)

	

	def __str__(self):
		return self.designation

	def update_admin(self,email,designation,contact_no,cl,sl):
		self.email = email
		self.designation = designation
		self.contact_no = contact_no
		self.cl = cl
		self.sl = sl
		self.save()

class StartupCategory(models.Model):
	startupHub 				= models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):
		return self.startupHub

class StartUp(models.Model):
	account 				= models.ForeignKey(Account, on_delete=models.CASCADE)
	startup_group 			= models.ForeignKey(StartupCategory, on_delete=models.SET_NULL, null=True,blank=True)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	startup_name			= models.CharField(max_length=100,null=True,blank=True)
	legal_entity			= models.CharField(max_length=100,null=True,blank=True)
	founders_designation	= models.CharField(max_length=2000,null=True,blank=True)
	website					= models.CharField(max_length=100,null=True,blank=True)
	city					= models.CharField(max_length=100,null=True,blank=True)
	sector					= models.CharField(max_length=100,null=True,blank=True)
	team_members			= models.CharField(max_length=100,null=True,blank=True)
	location				= models.CharField(max_length=100,null=True,blank=True)
	contact_no				= models.CharField(max_length=100,null=True,blank=True)
	team_head				= models.CharField(max_length=100,null=True,blank=True)

	comp_identification_no  = models.CharField(max_length=100,null=True,blank=True)
	inubatee_level			= models.CharField(max_length=100,null=True,blank=True)
	operational_model		= models.CharField(max_length=100,null=True,blank=True)
	type_of_incubatee      	= models.CharField(max_length=50,null=True,blank=True)
	women_led_startup 		= models.CharField(max_length=10,null=True,blank=True)
	gov_program 			= models.CharField(max_length=100,null=True,blank=True)
	msme_registered			= models.CharField(max_length=10,null=True,blank=True)
	dspp_registered			= models.CharField(max_length=10,null=True,blank=True)
	legal_entity_register   = models.CharField(max_length=100,null=True,blank=True)
	start_date_incubation   = models.CharField(max_length=100,null=True,blank=True)

	startup_img				= models.ImageField(upload_to='images/',null=True,blank=True)
	founder_img				= models.ImageField(upload_to='images/',null=True,blank=True)

	def __str__(self):
		return self.startup_name

	def startupUpdate(self,team_members):
		self.team_members = team_members
		self.save()
    

class TeamMembers(models.Model):
	startup  				= models.ForeignKey(StartUp, on_delete=models.CASCADE)
	name 					= models.CharField(max_length=100,null=True,blank=True)
	gender 					= models.CharField(max_length=10,null=True,blank=True)
	email 					= models.CharField(max_length=100,null=True,blank=True)
	contact_no 				= models.CharField(max_length=200,null=True,blank=True)
	designation				= models.CharField(max_length=200,null=True,blank=True)


	def __str__(self):
		return self.startup.startup_name +" " +self.email
	
	def update_team_member(self,email,designation,contact_no):
		self.email = email
		self.designation = designation
		self.contact_no = contact_no
		self.save()





class MonitorSheetReport(models.Model):
	connect_startup			      	= models.ForeignKey(StartUp, on_delete=models.CASCADE)

	ips_till_date					= models.CharField(max_length=100,null=True,blank=True)
	recognisation_till_date			= models.CharField(max_length=100,null=True,blank=True)
	funds_till_date					= models.CharField(max_length=100,null=True,blank=True)
	jobs_created_till_date 			= models.CharField(max_length=100,null=True,blank=True)
	sales_till_date					= models.CharField(max_length=100,null=True,blank=True)
	revenew_till_date				= models.CharField(max_length=100,null=True,blank=True)
	expendicture_till_date			= models.CharField(max_length=100,null=True,blank=True)

	ips_last_month					= models.CharField(max_length=100,null=True,blank=True)
	recognisation_last_month		= models.CharField(max_length=100,null=True,blank=True)
	funds_last_month				= models.CharField(max_length=100,null=True,blank=True)
	jobs_created_last_month 		= models.CharField(max_length=100,null=True,blank=True)
	sales_last_month				= models.CharField(max_length=100,null=True,blank=True)
	revenew_last_month				= models.CharField(max_length=100,null=True,blank=True)
	expendicture_last_month			= models.CharField(max_length=100,null=True,blank=True)

	problems						= models.CharField(max_length=2000,null=True,blank=True)
	oppertunities					= models.CharField(max_length=2000,null=True,blank=True)
	out_reach						= models.CharField(max_length=2000,null=True,blank=True)
	intervention 					= models.CharField(max_length=2000,null=True,blank=True)
	partnership_mou					= models.CharField(max_length=1000,null=True,blank=True)
	
	monitor_meeting					= models.CharField(max_length=1000,null=True,blank=True)
	action_plan						= models.CharField(max_length=2000,null=True,blank=True)
	help_required					= models.CharField(max_length=2000,null=True,blank=True)

	first_atempt					= models.BooleanField(default=True)

	allow_edit 						= models.BooleanField(default=False)
	date_of_filling					= models.DateTimeField(verbose_name='report date_of_filling', auto_now_add=True)


	def __str__(self):
		return self.connect_startup.startup_name

	def allow_edit_option(self):
		self.allow_edit = True
		self.save()
	
	def not_allow_edit_option(self):
		self.allow_edit = False
		self.save()

	def update_date(self):
		self.date_of_filling = timezone.now()
		self.save()
	def update_first_attempt(self):
		self.first_atempt = False
		self.save()






class MoM(models.Model):
	from_user 	 				= models.CharField(max_length=100,null=True,blank=True)
	to                          = models.ForeignKey(Account,null=True,blank=True, on_delete=models.CASCADE)
	date_of_creation			= models.DateTimeField(verbose_name='date of creation', auto_now_add=True)
	title						= models.CharField(max_length=500,null=True,blank=True)
	description					= models.CharField(max_length=1000,null=True,blank=True)
	document                    = models.FileField(upload_to='files',null=True,blank=True)

	def __str__(self):
		return self.title	


class BlogPost(models.Model):
	title   					= models.CharField(max_length=1000,null=True,blank=True)
	description			 		= models.CharField(max_length=5000,null=True,blank=True)
	blog_img					= models.ImageField(upload_to='blog_img/',null=True,blank=True)
	date_of_creation			= models.DateTimeField(verbose_name='date of creation', auto_now_add=True)


	def __str__(self):
		return self.title

	def update_blogPost(self,title,description):
		self.title = title
		self.description = description
		self.date_of_creation = timezone.now()
		self.save()



class WorkGenerator(models.Model):
	from_user					 = models.CharField(max_length=100,null=True,blank=True)
	to                           = models.ForeignKey(Admin,null=True,blank=True, on_delete=models.CASCADE)
	date_of_creation			 = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)	
	title   					 = models.CharField(max_length=1000,null=True,blank=True)
	work_description			 = models.CharField(max_length=2000,null=True,blank=True)
	suggestions					 = models.CharField(max_length=1500,null=True,blank=True)
	remarks						 = models.CharField(max_length=2000,null=True,blank=True)
	status 					 	 = models.CharField(max_length=20,null=True,blank=True)
	document                     = models.FileField(upload_to='files',null=True,blank=True)
	forwarded					 = models.BooleanField(default=False)
	forwarded_from 				 = models.CharField(max_length=200,null=True,blank=True)
	forwarded_to				 = models.CharField(max_length=200,null=True,blank=True)
	date_of_complition			 = models.DateTimeField(blank=True, null=True)
	from_user_pk				 = models.CharField(max_length=500,null=True,blank=True)
	new_work 					 = models.BooleanField(default=True)
	
	end_statement				 = models.CharField(max_length=500,null=True,blank=True)
	end_document				 = models.FileField(upload_to='files',null=True,blank=True)

	alert						 = models.BooleanField(default=False)


	def __str__(self):
		return self.title

	def update_alert(self):
		self.alert = True
		self.save()

	def make_new_work(self):
		self.new_work = True
		self.save()

	def update_work(self,title,work_description,suggestions,remarks):
		self.title = title
		self.work_description = work_description
		self.suggestions = suggestions
		self.remarks = remarks
		self.save()

	def change_status(self,status):
		self.status = status
		self.save()
	def update_end_msg(self,end_statement,end_document=None):
		self.end_statement = end_statement
		self.end_document = end_document
		self.save()
	def update_date(self):
		self.date_of_complition = timezone.now()
		self.save()
	
	def forward(self,from_user,to):
		self.forwarded = True
		self.forwarded_from = from_user
		self.forwarded_to = to
		self.save()
	
	def make_null(self):
		self.to = None
		self.save()

	def update_to(self,to):
		self.to = to
		self.date_of_creation = timezone.now()
		self.save()
	def remove_forward(self):
		self.forwarded = False
		self.save()

class Forward(models.Model):
	from_user				= models.CharField(max_length=100,null=True,blank=True)
	to  					= models.ForeignKey(Admin,null=True,blank=True, on_delete=models.CASCADE)
	forward_work  			= models.ForeignKey(WorkGenerator,null=True,blank=True,default="", on_delete=models.CASCADE)
	suggestions				= models.CharField(max_length=200,null=True,blank=True)
	forwarded			    = models.BooleanField(default=False)
	date_of_forward			= models.DateTimeField(verbose_name='date of forward', auto_now_add=True,null=True,blank=True)
	from_user_pk		    = models.CharField(max_length=500,null=True,blank=True)
	forward_pk				= models.CharField(max_length=100,null=True,blank=True)
	new_forward		    	= models.BooleanField(default=True)
	ford_document			= models.FileField(upload_to='files',null=True,blank=True)

	alert					= models.BooleanField(default=False)

	def update_alert(self):
		self.alert = True
		self.save()

	def forther_forward(self):
		self.forwarded = True
		self.save()
	def remove_forward(self):
		self.forwarded = False
		self.save()

	def make_null(self):
		self.to = None
		self.save()


	def __str__(self):
		return self.from_user +" " +self.forward_work.title

class Return(models.Model):
	from_user				= models.CharField(max_length=100,null=True,blank=True)
	to  					= models.ForeignKey(Admin, on_delete=models.CASCADE)
	work		  			= models.ForeignKey(WorkGenerator,default="", on_delete=models.CASCADE)
	message				    = models.CharField(max_length=500,null=True,blank=True)
	return_date				= models.DateTimeField(verbose_name='return date', auto_now_add=True,null=True,blank=True)
	forward_pk				= models.CharField(max_length=100,null=True,blank=True)
	new_return		    	= models.BooleanField(default=True)

	def __str__(self):
		return self.from_user

	def assign_forward_pk(self,forward_pk):
		self.forward_pk = forward_pk
		self.save()


class Query(models.Model):
	name				= models.CharField(max_length=100,null=True,blank=True)
	about				= models.CharField(max_length=100,null=True,blank=True)
	email				= models.CharField(max_length=100,null=True,blank=True)
	message				= models.CharField(max_length=1000,null=True,blank=True)
	submitted_date		= models.DateTimeField(verbose_name='submitted date', auto_now_add=True,null=True,blank=True)

	def __str__(self):
		return self.email

class Gallery(models.Model):
	gallery_img 		= models.FileField(upload_to='gallery',null=True,blank=True)

class LeaveApplication(models.Model):
	from_user 			= models.ForeignKey(Admin,null=True,blank=True, on_delete=models.CASCADE)
	from_user_name 		= models.CharField(max_length=100,null=True,blank=True) 
	to 					= models.CharField(max_length=100,null=True,blank=True) 
	subject 			= models.CharField(max_length=100,null=True,blank=True)
	body				= models.CharField(max_length=1000,null=True,blank=True)
	status				= models.CharField(max_length=100,null=True,blank=True)
	applied_date		= models.DateTimeField(verbose_name='applied date', auto_now_add=True,null=True,blank=True)
	message				= models.CharField(max_length=1000,null=True,blank=True)
	cl_or_sl			= models.CharField(max_length=100,null=True,blank=True)

	new_leave		    = models.BooleanField(default=True)
	reply			    = models.BooleanField(default=False)

	days 				= models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.from_user.account.fullname

	def update_message(self,message):
		self.message = message
		self.save()
	
	def update_status(self,status):
		self.status = status
		self.save()

class Attendence(models.Model):
	employee			= models.ForeignKey(Admin,null=True,blank=True, on_delete=models.CASCADE)
	date				= models.DateField(verbose_name='date', auto_now_add=True,null=True,blank=True)
	timein				= models.TimeField(verbose_name='timein', auto_now_add=True,null=True,blank=True)
	timeout				= models.TimeField(verbose_name='timeout',null=True,blank=True)
	total_time			= models.CharField(max_length=50,null=True,blank=True)

	time_status		    = models.BooleanField(default=True)

	def update_timeout(self):
		self.timeout = datetime.now()
		self.time_status = True
		self.save()
	
	def update_total_time(self,total):
		self.total_time = total
		self.save()

class EmpMessage(models.Model):
	message 			= models.CharField(max_length=1500,null=True,blank=True)
	created_date		= models.DateTimeField(verbose_name='created date', auto_now_add=True,null=True,blank=True)

	def __str__(self):
		return self.created_date


class Sanvriddhi(models.Model):
	account 				= models.ForeignKey(Account, on_delete=models.CASCADE)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	startup_name			= models.CharField(max_length=100,null=True,blank=True)
	legal_entity			= models.CharField(max_length=100,null=True,blank=True)
	founders_designation	= models.CharField(max_length=2000,null=True,blank=True)
	website					= models.CharField(max_length=100,null=True,blank=True)
	city					= models.CharField(max_length=100,null=True,blank=True)
	sector					= models.CharField(max_length=100,null=True,blank=True)
	team_members			= models.CharField(max_length=100,null=True,blank=True)
	location				= models.CharField(max_length=100,null=True,blank=True)
	contact_no				= models.CharField(max_length=100,null=True,blank=True)
	team_head				= models.CharField(max_length=100,null=True,blank=True)

	comp_identification_no  = models.CharField(max_length=100,null=True,blank=True)
	inubatee_level			= models.CharField(max_length=100,null=True,blank=True)
	operational_model		= models.CharField(max_length=100,null=True,blank=True)
	type_of_incubatee      	= models.CharField(max_length=50,null=True,blank=True)
	women_led_startup 		= models.CharField(max_length=10,null=True,blank=True)
	gov_program 			= models.CharField(max_length=100,null=True,blank=True)
	msme_registered			= models.CharField(max_length=10,null=True,blank=True)
	dspp_registered			= models.CharField(max_length=10,null=True,blank=True)
	legal_entity_register   = models.CharField(max_length=100,null=True,blank=True)
	start_date_incubation   = models.CharField(max_length=100,null=True,blank=True)

	startup_img				= models.ImageField(upload_to='images/',null=True,blank=True)
	founder_img				= models.ImageField(upload_to='images/',null=True,blank=True)
	# ranks					= models.CharField(max_length=100,null=True,blank=True)

	

	def __str__(self):
		return self.email

class Sanvriddhiweek(models.Model):
	week_no 			= models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.week_no

class Sanvriddhifeedback(models.Model):
	week				= models.ForeignKey(Sanvriddhiweek, on_delete=models.CASCADE, default=1)
	feedback 			= models.CharField(max_length=1000,null=True,blank=True)

	def __str__(self):
		return self.feedback

class Session(models.Model):
	week				= models.ForeignKey(Sanvriddhiweek, on_delete=models.CASCADE, default=1)
	session_name		= models.CharField(max_length=100,null=True,blank=True)
	session_details     = models.CharField(max_length=1000,null=True,blank=True)
	session_date		= models.DateTimeField(verbose_name='date')
	time				= models.CharField(max_length=20,null=True,blank=True)
	time_out			= models.CharField(max_length=20,null=True,blank=True)
	pm_am1				= models.CharField(max_length=20,null=True,blank=True)
	pm_am2				= models.CharField(max_length=20,null=True,blank=True)
	meeting_link		= models.CharField(max_length=1000,null=True,blank=True)
	pre_read			= models.FileField(upload_to='files',null=True,blank=True)
	submission_link		= models.CharField(max_length=1000,null=True,blank=True)
	assignment			= models.FileField(upload_to='files',null=True,blank=True)
	#completed			= models.BooleanField(default=Falsese)
	completed			= models.BooleanField(default=False)
	recording_link		= models.CharField(max_length=1000,null=True,blank=True)
	recording_pw		= models.CharField(max_length=500,null=True,blank=True)

	def __str__(self):
		return self.session_name

	def update_session(self,recording_link,recording_pw):
		self.recording_link = recording_link
		self.recording_pw	= recording_pw
		self.save()


class Submission(models.Model):
	connect_sanvriddhi	= models.ForeignKey(Sanvriddhi, on_delete=models.CASCADE)
	session_topic		= models.CharField(max_length=100,null=True,blank=True)
	attachment			= models.FileField(upload_to='files',null=True,blank=True)
	submitted_date		= models.DateTimeField(verbose_name='date submitted', auto_now_add=True)


class Viewer(models.Model):
	account 				= models.ForeignKey(Account, on_delete=models.CASCADE)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	contact_no				= models.CharField(max_length=100,null=True,blank=True)
	viewer_img				= models.ImageField(upload_to='images/',null=True,blank=True)

	def __str__(self):
		return self.email

class Ideanestchecking(models.Model):
	account 				= models.ForeignKey(Account, on_delete=models.CASCADE)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	startup_name			= models.CharField(max_length=100,null=True,blank=True)
	legal_entity			= models.CharField(max_length=100,null=True,blank=True)
	founders_designation	= models.CharField(max_length=2000,null=True,blank=True)
	website					= models.CharField(max_length=100,null=True,blank=True)
	city					= models.CharField(max_length=100,null=True,blank=True)
	sector					= models.CharField(max_length=100,null=True,blank=True)
	team_members			= models.CharField(max_length=100,null=True,blank=True)
	location				= models.CharField(max_length=100,null=True,blank=True)
	contact_no				= models.CharField(max_length=100,null=True,blank=True)
	team_head				= models.CharField(max_length=100,null=True,blank=True)

	comp_identification_no  = models.CharField(max_length=100,null=True,blank=True)
	inubatee_level			= models.CharField(max_length=100,null=True,blank=True)
	operational_model		= models.CharField(max_length=100,null=True,blank=True)
	type_of_incubatee      	= models.CharField(max_length=50,null=True,blank=True)
	women_led_startup 		= models.CharField(max_length=10,null=True,blank=True)
	gov_program 			= models.CharField(max_length=100,null=True,blank=True)
	msme_registered			= models.CharField(max_length=10,null=True,blank=True)
	dspp_registered			= models.CharField(max_length=10,null=True,blank=True)
	legal_entity_register   = models.CharField(max_length=100,null=True,blank=True)
	start_date_incubation   = models.CharField(max_length=100,null=True,blank=True)

	startup_img				= models.ImageField(upload_to='images/',null=True,blank=True)
	founder_img				= models.ImageField(upload_to='images/',null=True,blank=True)
	# ranks					= models.CharField(max_length=100,null=True,blank=True)

	

	def __str__(self):
		return self.email

class Ideanestweek(models.Model):
	week_no 			= models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.week_no
		

class Ideanestfeedback(models.Model):
	week				= models.ForeignKey(Ideanestweek, on_delete=models.CASCADE)
	feedback 			= models.CharField(max_length=1000,null=True,blank=True)

	def __str__(self):
		return self.feedback



class Sessionideanesting(models.Model):
	week 				=models.ForeignKey(Ideanestweek, on_delete=models.CASCADE)
	session_name		= models.CharField(max_length=100,null=True,blank=True)
	session_details     = models.CharField(max_length=1000,null=True,blank=True)
	session_date		= models.DateTimeField(verbose_name='date')
	time				= models.CharField(max_length=20,null=True,blank=True)
	time_out			= models.CharField(max_length=20,null=True,blank=True)
	pm_am1				= models.CharField(max_length=20,null=True,blank=True)
	pm_am2				= models.CharField(max_length=20,null=True,blank=True)
	meeting_link		= models.CharField(max_length=1000,null=True,blank=True)
	pre_read			= models.FileField(upload_to='files',null=True,blank=True)
	submission_link		= models.CharField(max_length=1000,null=True,blank=True)
	assignment			= models.FileField(upload_to='files',null=True,blank=True)
	#completed			= models.BooleanField(default=Falsese)
	completed			= models.BooleanField(default=False)
	recording_link		= models.CharField(max_length=1000,null=True,blank=True)
	recording_pw		= models.CharField(max_length=500,null=True,blank=True)
	

	def __str__(self):
		return self.session_name

	def update_session(self,recording_link,recording_pw):
		self.recording_link = recording_link
		self.recording_pw	= recording_pw
		self.save()

class Submissionideanesting(models.Model):
	connect_sanvriddhi	= models.ForeignKey(Ideanestchecking, on_delete=models.CASCADE)
	session_topic		= models.CharField(max_length=100,null=True,blank=True)
	attachment			= models.FileField(upload_to='files',null=True,blank=True)
	submitted_date		= models.DateTimeField(verbose_name='date submitted', auto_now_add=True)




class Viewerideanesting(models.Model):
	account 				= models.ForeignKey(Account, on_delete=models.CASCADE)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	contact_no				= models.CharField(max_length=100,null=True,blank=True)
	viewer_img				= models.ImageField(upload_to='images/',null=True,blank=True)

	def __str__(self):
		return self.email


