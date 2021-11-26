from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import Account,Admin,StartUp,Sanvriddhi,Ideanestcheck,Sessionideanest,Viewerideanest,Submissionideanest
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("dashboard")
        else:
            return redirect('login')
    else:
        values = Account.objects.filter(is_admin=True)
        imp_values = []
        required_val = values[1:]
        for i in required_val:
            imp_values.append(i.admin_set.all()[0])
        return render(request,'index.html',{'values':imp_values})


def logout(request):
    auth.logout(request)
    return redirect('index')

def logout1(request):
    auth.logout(request)
    return redirect('sanvriddhi')

def logout2(request):
    auth.logout(request)
    return redirect('ideanest')

@login_required
def admin_register(request):
    if request.method == 'POST' and request.FILES['admin_img']:
        full_name = request.POST['full_name']
        
        username = request.POST['username']
        password = request.POST['password1']
        
        user = Account.objects.create_user(fullname=full_name,username=username,is_admin=True)
        user.set_password(password)
        user.save() 

        email=request.POST['email']
        designation = request.POST['designation']
        employee_id = request.POST['employee_id']
        contact_no = request.POST['contact']
        identity_proof = request.POST['identity']
        cl = request.POST['cl']
        sl = request.POST['sl']

        admin_img = request.FILES['admin_img']
        

        admin = Admin.objects.create(account=user,designation=designation,email=email,employee_id=employee_id,contact_no=contact_no,identity_proof=identity_proof,cl=cl,sl=sl,admin_img=admin_img) 
        admin.save()
        messages.add_message(request, messages.INFO, 'Employee created successfully.')

        return redirect('dashboard')
    return redirect('dashboard')

@login_required
def startup_register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        password = request.POST['password1']
        
        user = Account.objects.create_user(fullname=full_name,username=username,is_startup=True)
        user.set_password(password)
        user.save() 

        startup_name = request.POST['startup_name']
        email=request.POST['email']
        legal_entity = request.POST['legal_entity']
        founders_designation = request.POST['founders_designation']
        city = request.POST['city']
        website = request.POST['website']
        sector = request.POST['sector']
        team_members = request.POST['team_members']
        location = request.POST['location']
        contact_no = request.POST['contact']

        comp_identification_no = request.POST['comp_identification_no']
        inubatee_level = request.POST['inubatee_level']
        operational_model = request.POST['operational_model']
        type_of_incubatee = request.POST['type_of_incubatee']
        women_led_startup = request.POST['women_led_startup']
        gov_program = request.POST['gov_program']
        msme_registered = request.POST['msme_registered']
        dspp_registered = request.POST['dspp_registered']
        legal_entity_register = request.POST['registrationdate']          
        start_date_incubation = request.POST['joindate']          

        startup_img = request.FILES['startup_img']
        founder_img = request.FILES['founder_img']  

        startup = StartUp.objects.create(account=user,startup_name=startup_name,email=email,legal_entity=legal_entity,founders_designation=founders_designation,city=city,website=website,sector=sector,team_members=team_members,location=location,contact_no=contact_no,comp_identification_no=comp_identification_no,inubatee_level=inubatee_level,operational_model=operational_model,type_of_incubatee=type_of_incubatee,women_led_startup=women_led_startup,gov_program=gov_program,msme_registered=msme_registered,dspp_registered=dspp_registered,legal_entity_register=legal_entity_register,start_date_incubation=start_date_incubation,founder_img=founder_img,startup_img=startup_img,team_head=full_name) 
        startup.save()
        messages.add_message(request, messages.INFO, 'Startup created successfully.')

        return redirect('dashboard')
    return redirect('dashboard') 


@login_required
def sanvriddhi_register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        password = request.POST['password1']
        
        user = Account.objects.create_user(fullname=full_name,username=username,is_sanvriddhi=True)
        user.set_password(password)
        user.save() 

        startup_name = request.POST['startup_name']
        email=request.POST['email']
        legal_entity = request.POST['legal_entity']
        founders_designation = request.POST['founders_designation']
        city = request.POST['city']
        website = request.POST['website']

        sector = request.POST['sector']

        team_members = request.POST['team_members']
        location = request.POST['location']
        contact_no = request.POST['contact']

        comp_identification_no = request.POST['comp_identification_no']
        inubatee_level = request.POST['inubatee_level']
        operational_model = request.POST['operational_model']
        type_of_incubatee = request.POST['type_of_incubatee']
        women_led_startup = request.POST['women_led_startup']
        gov_program = request.POST['gov_program']
        msme_registered = request.POST['msme_registered']
        dspp_registered = request.POST['dspp_registered']
        legal_entity_register = request.POST['registrationdate']          
        start_date_incubation = request.POST['joindate']
        if len(request.FILES) != 0:
            startup_img = request.FILES['startup_img']
            founder_img = request.FILES['founder_img']
        else:
            startup_img = "awardimg/blank.png"
            founder_img = "awardimg/blank.png"          

          
        admin = Sanvriddhi.objects.create(account=user,startup_name=startup_name,email=email,legal_entity=legal_entity,founders_designation=founders_designation,city=city,website=website,sector=sector,team_members=team_members,location=location,contact_no=contact_no,comp_identification_no=comp_identification_no,inubatee_level=inubatee_level,operational_model=operational_model,type_of_incubatee=type_of_incubatee,women_led_startup=women_led_startup,gov_program=gov_program,msme_registered=msme_registered,dspp_registered=dspp_registered,legal_entity_register=legal_entity_register,start_date_incubation=start_date_incubation,founder_img=founder_img,startup_img=startup_img,team_head=full_name) 
        admin.save()
        messages.add_message(request, messages.INFO, 'Sanvriddhi Startup account created successfully.')

        return redirect('dashboard')
    return redirect('dashboard')


@login_required
def ideanest_register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        password = request.POST['password1']
        
        user = Account.objects.create_user(fullname=full_name,username=username,is_ideanest_check=True)
        user.set_password(password)
        user.save() 

        startup_name = request.POST['startup_name']
        email=request.POST['email']
        legal_entity = request.POST['legal_entity']
        founders_designation = request.POST['founders_designation']
        city = request.POST['city']
        website = request.POST['website']

        sector = request.POST['sector']

        team_members = request.POST['team_members']
        location = request.POST['location']
        contact_no = request.POST['contact']

        comp_identification_no = request.POST['comp_identification_no']
        inubatee_level = request.POST['inubatee_level']
        operational_model = request.POST['operational_model']
        type_of_incubatee = request.POST['type_of_incubatee']
        women_led_startup = request.POST['women_led_startup']
        gov_program = request.POST['gov_program']
        msme_registered = request.POST['msme_registered']
        dspp_registered = request.POST['dspp_registered']
        legal_entity_register = request.POST['registrationdate']          
        start_date_incubation = request.POST['joindate']
        if len(request.FILES) != 0:
            startup_img = request.FILES['startup_img']
            founder_img = request.FILES['founder_img']
        else:
            startup_img = "awardimg/blank.png"
            founder_img = "awardimg/blank.png"          

          
        admin = Ideanestcheck.objects.create(account=user,startup_name=startup_name,email=email,legal_entity=legal_entity,founders_designation=founders_designation,city=city,website=website,sector=sector,team_members=team_members,location=location,contact_no=contact_no,comp_identification_no=comp_identification_no,inubatee_level=inubatee_level,operational_model=operational_model,type_of_incubatee=type_of_incubatee,women_led_startup=women_led_startup,gov_program=gov_program,msme_registered=msme_registered,dspp_registered=dspp_registered,legal_entity_register=legal_entity_register,start_date_incubation=start_date_incubation,founder_img=founder_img,startup_img=startup_img,team_head=full_name) 
        admin.save()
        messages.add_message(request, messages.INFO, 'Ideanest Startup account created successfully.')

        return redirect('dashboard')
    return redirect('dashboard')