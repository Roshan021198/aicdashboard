from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,JsonResponse
from useraccounting.models import Account,Admin,StartUp,TeamMembers,MonitorSheetReport,WorkGenerator,Forward,Return,MoM,BlogPost,Query,LeaveApplication,Attendence,EmpMessage,Sanvriddhi,Session,Submission,Viewer,Ideanestcheck,Sessionideanest,Submissionideanest,Viewerideanest,Sanvriddhiweek,Ideanestweek
#,Ideanest,IdeanestSession,Ideanestsubmission,Ideanestviewer
from .forms import StartUpForm,MonitorSheetEditForm

from django.contrib.auth.models import auth
import random
from django.core.mail import send_mail
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    accounts = Account.objects.all()
    user = request.user
    admins = Admin.objects.all()
    if user.is_superadmin:
        lis = []
        lists = Account.objects.filter(is_admin=True).order_by('rank')
        lists = list(lists)
        for account in lists:
            if account.is_superadmin == False and account.is_adminstrator == False:
                lis.append(account)
        return render(request,'startup.html',{'accounts':accounts,'lists':lis})
    elif user.is_admin:
        value = user.admin_set.all()[0]
        if user.is_adminstrator:
            works = WorkGenerator.objects.all().order_by('-date_of_creation')
            ford_status = WorkGenerator.objects.filter(forwarded=True).order_by('-date_of_creation')
            pending_status = WorkGenerator.objects.filter(status='pending...').order_by('-date_of_creation')
            completed_status = WorkGenerator.objects.filter(status='completed').order_by('-date_of_creation')
            assigned_work = value.forward_set.all().order_by('-date_of_forward')
            from_works = Forward.objects.filter(from_user=request.user.fullname).order_by('-date_of_forward')
            
            forward_notifications = value.forward_set.filter(new_forward=True).order_by('-date_of_forward')
            return_notifications = Return.objects.filter(to=value,new_return=True).order_by('-return_date')
            
            leave_notifications = LeaveApplication.objects.filter(new_leave=True).order_by('-applied_date')

            total_notifications =  len(forward_notifications) + len(return_notifications) + len(leave_notifications)
            
            return_obj = Return.objects.filter(to=value).order_by('-return_date')

            leave_obj = LeaveApplication.objects.all().order_by('-applied_date')
            emp_messages = EmpMessage.objects.all().order_by('-created_date')

            admin_val = Admin.objects.all()
            admin_lists = list(admin_val)
            
            lis = []
            for admin_list in admin_lists:
                if admin_list.account.is_superadmin == False and admin_list.account.is_adminstrator == False:
                    lis.append(admin_list)
            
            for l in lis:
                abc=l.attendence_set.all().order_by('-date')

            today = date.today()
            attendence_obj = Attendence.objects.filter(timeout=None,date=today)

            return render(request,'emp_dashboard.html',{'value':value,'accounts':accounts,'works':works,'assigned_work':assigned_work,'from_works':from_works,'ford_status':ford_status,'pending_status':pending_status,'completed_status':completed_status,'return_obj':return_obj,'forward_notifications':forward_notifications,'return_notifications':return_notifications,'total_notifications':total_notifications,'leave_obj':leave_obj,'leave_notifications':leave_notifications,'admin_lis':lis,'emp_messages':emp_messages,'attendence_obj':attendence_obj})
        else:
            admin_obj = user.admin_set.all()[0]
            works = admin_obj.workgenerator_set.all().order_by('-date_of_creation')
            assigned_work = admin_obj.forward_set.all().order_by('-date_of_forward')
            
            from_works = Forward.objects.filter(from_user=request.user.fullname).order_by('-date_of_forward')
            
            
            pending_status = admin_obj.workgenerator_set.filter(status='pending...').order_by('-date_of_creation')
            completed_status = admin_obj.workgenerator_set.filter(status='completed').order_by('-date_of_creation')
            val = admin_obj.forward_set.filter(to=admin_obj).order_by('-date_of_forward')
            assign_pending_status = []
            for v in val:
                if v.forward_work.status == "pending...":
                    assign_pending_status.append(v)
            assign_completed_status = []
            for v in val:
                if v.forward_work.status == "completed":
                    assign_completed_status.append(v)
            return_obj = Return.objects.filter(to=value).order_by('-return_date')

            work_notifications = admin_obj.workgenerator_set.filter(new_work=True).order_by('-date_of_creation')
            forward_notifications = admin_obj.forward_set.filter(new_forward=True).order_by('-date_of_forward')
            return_notifications = Return.objects.filter(to=value,new_return=True).order_by('-return_date')
            leave_noti = LeaveApplication.objects.filter(reply=True,from_user=admin_obj).order_by('-applied_date')
            total_notifications = len(work_notifications) + len(forward_notifications) + len(return_notifications) + len(leave_noti)

            obj = request.user
            leave_obj = LeaveApplication.objects.filter(from_user_name=obj.fullname).order_by('-applied_date')

            emp_messages = EmpMessage.objects.all().order_by('-created_date')

            timeout_val=None
            timeobj = Attendence.objects.filter(employee=admin_obj)
            today = date.today()
            if timeobj:
                timeout_val = Attendence.objects.filter(employee=admin_obj).order_by('-date')[0]
                if today == timeout_val.date:
                    timeout_val = timeout_val
                else:
                    timeout_val = None
            
            return render(request,'emp_dashboard.html',{'value':value,'accounts':accounts,'works':works,'assigned_work':assigned_work,'from_works':from_works,'pending_status':pending_status,'assign_pending_status':assign_pending_status,'completed_status':completed_status,'assign_completed_status':assign_completed_status,'return_obj':return_obj,'work_notifications':work_notifications,'forward_notifications':forward_notifications,'return_notifications':return_notifications,'total_notifications':total_notifications,'leave_obj':leave_obj,'leave_noti':leave_noti,'timeout_val':timeout_val,'emp_messages':emp_messages,'today':today})        
        
    elif user.is_startup:
        user = request.user
        startup_obj = user.startup_set.all()[0]
        val2 = startup_obj.teammembers_set.all()
        values = startup_obj.monitorsheetreport_set.all().order_by('-date_of_filling')
        # traction_values = startup_obj.tractionsheet_set.all().order_by('-generated_date')
        account = Account.objects.filter(is_superadmin=True)[0]
        sendings = MoM.objects.filter(from_user=user.fullname,to=account).order_by('-date_of_creation')
        receving = MoM.objects.filter(from_user=account.fullname,to=user).order_by('-date_of_creation')
        posts = BlogPost.objects.all().order_by('-date_of_creation')
        
        return render(request,'demo_startup_page.html',{'value':startup_obj,'members':val2,'values':values,'account':account,'sendings':sendings,'receving':receving,'posts':posts})

    elif user.is_sanvriddhi or user.is_viewer:
        if request.user.is_adminstrator or request.user.is_sanvriddhi or request.user.is_viewer:
            sessions = Session.objects.all()
            weeks = Sanvriddhiweek.objects.all()
            if request.user.is_adminstrator or request.user.is_viewer:
                participaints = Account.objects.filter(is_sanvriddhi=True)
                lis = []
                for participaint in participaints:
                    lis.append(participaint.sanvriddhi_set.all()[0])
                return render(request,'sanvriddhi_dashboard.html',{'sessions':sessions,'participaints':lis,'weeks':weeks})
            else:
                account = request.user
                sanvriddhi_account = account.sanvriddhi_set.all()[0]

                attachements = sanvriddhi_account.submission_set.all()
                return render(request,'sanvriddhi_dashboard.html',{'sessions':sessions,'attachements':attachements,'sanvriddhi_account':sanvriddhi_account,'weeks':weeks})
        else:
            return render(request,'error.html')

    elif user.is_ideanest_check or user.is_ideanest_viewer:
        if request.user.is_adminstrator or request.user.is_ideanest_check or request.user.is_ideanest_viewer:
            sessions = Sessionideanest.objects.all()
            weeks = Ideanestweek.objects.all()
            if request.user.is_adminstrator or request.user.is_ideanest_viewer:
                participaints = Account.objects.filter(is_ideanest_check=True)
                lis = []
                for participaint in participaints:
                    lis.append(participaint.ideanestcheck_set.all()[0])
                return render(request,'ideanest_dashboard.html',{'sessions':sessions,'participaints':lis,'weeks':weeks})
            else:
                account = request.user
                ideanest_account = account.ideanestcheck_set.all()[0]

                attachements = ideanest_account.submissionideanest_set.all()
                
                return render(request,'ideanest_dashboard.html',{'sessions':sessions,'attachements':attachements,'ideanest_account':ideanest_account,'weeks':weeks})
        else:
            return render(request,'error.html')

@login_required
def visit_startup(request):
    accounts = Account.objects.all()
    lis = []
    lists = Account.objects.filter(is_admin=True).order_by('rank')
    lists = list(lists)
    for account in lists:
        if account.is_superadmin == False and account.is_adminstrator == False:
            lis.append(account)
    return render(request,'startup.html',{'accounts':accounts,'lists':lis})

@login_required   
def admin_form(request):
    if request.user.is_superadmin:
        return render(request,'admin_form.html')
    else:
        return render(request,'error.html')
        
@login_required
def startup_form(request):
    return render(request,'startup_form.html')

@login_required
def profile(request,pk): 
    details = get_object_or_404(Account, pk=pk)
    startup_obj = details.startup_set.all()[0]
    val2 = startup_obj.teammembers_set.all()
    values = startup_obj.monitorsheetreport_set.order_by('-date_of_filling')
    # traction_values = startup_obj.tractionsheet_set.all()
    sendings = MoM.objects.filter(from_user=request.user.fullname,to=details).order_by('-date_of_creation')
    receving = MoM.objects.filter(from_user=details.fullname,to=request.user).order_by('-date_of_creation')

    return render(request,'demo_startup_page.html',{'value':startup_obj,'members':val2,'values':values,'sendings':sendings,'receving':receving})

@login_required
def startup_profile_edit(request,pk):
    
    content = get_object_or_404(StartUp,pk=pk)
    
    if request.method == 'POST':
        form = StartUpForm(request.POST,request.FILES,instance=content)
        
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            messages.add_message(request, messages.INFO, 'Edited successfully.')
            return redirect(dashboard)
    else:
        form = StartUpForm(instance=content)
        
    return render(request,'startup_edit_form.html',{'form':form})

@login_required
def delete_employee(request):
    if request.method == 'POST':
        getpk = request.POST['foo']
        
        details = get_object_or_404(Admin,pk=int(getpk))
        main_account = details.account
        
        main_account.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('dashboard')


@login_required
def edit_emp_form(request):

    if request.method == "POST":
        pk = request.POST['pk_val']
        designation = request.POST['designation']
        email = request.POST['email']
        contact = request.POST['contact']
        cl = request.POST['cl']
        sl = request.POST['sl']

        account = Admin.objects.get(pk=pk)

        if designation:
            designation = designation
        else:
            designation = ' '
        
        if email:
            email = email
        else:
            email = ' '

        if contact:
            contact = contact
        else:
            contact = ' '

        if cl:
            cl = cl
        else:
            cl = ' '

        if sl:
            sl = sl
        else:
            sl = ' '

        account.update_admin(email = email,designation = designation,contact_no = contact,cl=cl,sl=sl)
        messages.add_message(request, messages.INFO, 'Edited successfully.')
    return redirect('dashboard')
    
#user profile
@login_required
def userprofile(request,pk):
    details = get_object_or_404(Account,pk=pk)
    val = details.admin_set.all()
    return render(request,'user_profile.html',{'value':val[0]})
    
@login_required
def add_new_team_member(request):
    if request.method == 'POST':
        user = request.user
        startup_obj = user.startup_set.all()[0]
        name = request.POST['name']
        gender = request.POST['gender']
        email = request.POST['email']
        contact_no = request.POST['contact']
        designation = request.POST['designation']

        team_member = TeamMembers.objects.create(startup=startup_obj,name=name,gender=gender,email=email,contact_no=contact_no,designation=designation)
        team_member.save()
        messages.add_message(request, messages.INFO, 'One team member added successfully.')
        return redirect('profile',pk=user.pk)
        
@login_required
def delete_team_member(request):
    if request.method == 'POST':
        user = request.user
        getpk = request.POST['foo']
        
        details = get_object_or_404(TeamMembers,pk=int(getpk))
        details.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('profile',pk=user.pk)

@login_required
def edit_team_member(request):

    if request.method == "POST":
        user = request.user
        pk = request.POST['pk_val']
        designation = request.POST['designation']
        email = request.POST['email']
        contact = request.POST['contact']
        
        account = TeamMembers.objects.get(pk=pk)

        if designation:
            designation = designation
        else:
            designation = ' '
        
        if email:
            email = email
        else:
            email = ' '

        if contact:
            contact = contact
        else:
            contact = ' '

        account.update_team_member(email = email,designation = designation,contact_no = contact)
        messages.add_message(request, messages.INFO, 'Edited successfully.')
    return redirect('profile',pk=user.pk)


def monitor_report(request,pk):
    monitor_sheet_obj = MonitorSheetReport.objects.get(pk=pk)
    return render(request,'monitor_report.html',{'monitor_report':monitor_sheet_obj})

@login_required
def allowedit(request,pk):
    monitor_report_obj = MonitorSheetReport.objects.get(pk=pk)
    monitor_report_obj.allow_edit_option()
    return redirect(monitor_report,pk=pk)


@login_required
def monitor_sheet_edit(request,pk):
    content = get_object_or_404(MonitorSheetReport,pk=pk)
    
    if request.method == 'POST':
        form = MonitorSheetEditForm(request.POST,instance=content)
        
        if form.is_valid():
            content = form.save(commit=False)
            content.not_allow_edit_option()
            content.update_date()
            content.save()
            messages.add_message(request, messages.INFO, 'Monitor report edited successfully.')
            return redirect(dashboard)
    else:
        form = MonitorSheetEditForm(instance=content)
        
    return render(request,'edit_monitor_sheet.html',{'form':form,'content':content})

@login_required
def monitor_form(request):
    user = request.user
    startup_obj = user.startup_set.all()[0]
    empty = len(list(startup_obj.monitorsheetreport_set.all()))
    empty_or_not = str(empty)
    if request.method == 'POST':

        if empty >0:
            ips_last_month = request.POST['ips_last_month']
            recognisation_last_month = request.POST['recognisation_last_month']
            funds_last_month = request.POST['funds_last_month']
            jobs_created_last_month = request.POST['jobs_created_last_month']
            sales_last_month = request.POST['sales_last_month']
            revenew_last_month = request.POST['revenew_last_month']
            expendicture_last_month = request.POST['expendicture_last_month']
            
            problems = request.POST['problems']
            oppertunities = request.POST['oppertunities']
            out_reach = request.POST['out_reach']
            partnership_mou = request.POST['partnership_mou']
            intervention = request.POST['intervention']
            
            
            monitor_meeting = request.POST['monitor_meeting']
            action_plan = request.POST['action_plan']
            help_required = request.POST['help_required']

            monitor_report = MonitorSheetReport.objects.create(connect_startup=startup_obj,ips_last_month=ips_last_month,recognisation_last_month=recognisation_last_month,funds_last_month=funds_last_month,
                                                            jobs_created_last_month=jobs_created_last_month,sales_last_month=sales_last_month,revenew_last_month=revenew_last_month,
                                                            expendicture_last_month=expendicture_last_month,problems=problems,oppertunities=oppertunities,out_reach=out_reach,partnership_mou=partnership_mou,
                                                            intervention=intervention,monitor_meeting=monitor_meeting,action_plan=action_plan,help_required=help_required)
            monitor_report.update_first_attempt()
        else:
            ips_till_date = request.POST['ips_till_date']
            recognisation_till_date = request.POST['recognisation_till_date']
            funds_till_date = request.POST['funds_till_date']
            jobs_created_till_date = request.POST['jobs_created_till_date']
            sales_till_date = request.POST['sales_till_date']
            revenew_till_date = request.POST['revenew_till_date']
            expendicture_till_date = request.POST['expendicture_till_date']

            ips_last_month = request.POST['ips_last_month']
            recognisation_last_month = request.POST['recognisation_last_month']
            funds_last_month = request.POST['funds_last_month']
            jobs_created_last_month = request.POST['jobs_created_last_month']
            sales_last_month = request.POST['sales_last_month']
            revenew_last_month = request.POST['revenew_last_month']
            expendicture_last_month = request.POST['expendicture_last_month']
            
            problems = request.POST['problems']
            oppertunities = request.POST['oppertunities']
            out_reach = request.POST['out_reach']
            partnership_mou = request.POST['partnership_mou']
            intervention = request.POST['intervention']
            
            
            monitor_meeting = request.POST['monitor_meeting']
            action_plan = request.POST['action_plan']
            help_required = request.POST['help_required']

            monitor_report = MonitorSheetReport.objects.create(connect_startup=startup_obj,ips_till_date=ips_till_date,recognisation_till_date=recognisation_till_date,funds_till_date=funds_till_date,
                                                            jobs_created_till_date=jobs_created_till_date,sales_till_date=sales_till_date,revenew_till_date=revenew_till_date,
                                                            expendicture_till_date=expendicture_till_date,ips_last_month=ips_last_month,recognisation_last_month=recognisation_last_month,funds_last_month=funds_last_month,
                                                            jobs_created_last_month=jobs_created_last_month,sales_last_month=sales_last_month,revenew_last_month=revenew_last_month,
                                                            expendicture_last_month=expendicture_last_month,problems=problems,oppertunities=oppertunities,out_reach=out_reach,partnership_mou=partnership_mou,
                                                            intervention=intervention,monitor_meeting=monitor_meeting,action_plan=action_plan,help_required=help_required)
        monitor_report.save()
        super_admin = Account.objects.filter(is_superadmin=True)[0]
        obj = super_admin.admin_set.all()[0]
        send_mail(
                'Monitor Report',
                'Monitor report submitted by '+startup_obj.startup_name,
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Monitor Form submitted successfully.')
        return redirect('dashboard')
    else:
        return render(request,'monitor_form.html',{'empty_or_not':empty_or_not})

@login_required
def send_mom(request):
    
    if request.method == 'POST' or request.FILES['document']:
        
        from_user = request.POST['from']
        to = request.POST['to']
        title = request.POST['title']
        description = request.POST['description']
        document = request.FILES['document']

        from_obj = Account.objects.get(pk=int(from_user))
        to_obj = Account.objects.get(pk=int(to))
        

        mom_obj = MoM.objects.create(from_user=from_obj.fullname,to=to_obj,title=title,description=description,document=document)
        mom_obj.save()

        

        if request.user.is_superadmin:
            obj = to_obj.startup_set.all()[0]
            send_mail(
                'Minute of Meeting',
                'You receved a MoM by AIC-NITF',
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
            messages.add_message(request, messages.INFO, 'M-o-M sended successfully.')
            return redirect(profile,int(to))
        else:
            name = from_obj.startup_set.all()[0]
            obj = to_obj.admin_set.all()[0]
            send_mail(
                'Minute of Meeting',
                'MoM submitted by '+name.startup_name,
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
            messages.add_message(request, messages.INFO, 'M-o-M sended successfully.')
            return redirect(dashboard)
    else:
        if request.user.is_superadmin:
            return redirect(profile,int(to))
        else:
            return redirect(dashboard)

# @login_required
# def traction_form(request):
#     if request.method == 'POST':
#         user = request.user
#         startup_obj = user.startup_set.all()[0]

#         total_order     = request.POST['total_order']
#         average_packet_size   = request.POST['average_packet_size']
#         total_revenue_of_month  = request.POST['total_revenue_of_month']
#         total_customers_served  = request.POST['total_customers_served']
#         total_expense     = request.POST['total_expense']
#         market_outreach   = request.POST['market_outreach']
#         repeate_customers    = request.POST['repeate_customers']
#         total_revenue     = request.POST['total_revenue']
#         direct_job_created   = request.POST['direct_job_created']
#         indirect_job_created   = request.POST['indirect_job_created']
#         profit = request.POST['profit']

#         traction_report = TractionSheet.objects.create(connect_startup=startup_obj,total_order=total_order,average_packet_size=average_packet_size,total_revenue_of_month=total_revenue_of_month,total_customers_served=total_customers_served,total_expense=total_expense,market_outreach=market_outreach,repeate_customers=repeate_customers,total_revenue=total_revenue,direct_job_created=direct_job_created,indirect_job_created=indirect_job_created,profit=profit)
#         super_admin = Account.objects.filter(is_superadmin=True)[0]
#         obj = super_admin.admin_set.all()[0]
#         send_mail(
#                 'Traction Report',
#                 'Traction report submitted by '+startup_obj.startup_name,
#                 'support@aicnalanda.com',
#                 [obj.email],
#                 fail_silently=False,
#             )
#         messages.add_message(request, messages.INFO, 'Traction form submitted successfully.')
#         return redirect('dashboard')
    
#     else:
#         return render(request,'traction_form.html')


# def traction_report(request,pk):
#     traction_sheet_obj = TractionSheet.objects.get(pk=pk)
    
#     return render(request,'traction_report.html',{'traction_report':traction_sheet_obj})

# @login_required
# def allow_traction_edit(request,pk):
#     traction_report_obj = TractionSheet.objects.get(pk=pk)
#     traction_report_obj.allow_edit_option()
#     return redirect(traction_report,pk=pk)


@login_required
# def edit_traction_sheet(request,pk):
#     content = get_object_or_404(TractionSheet,pk=pk)
    
#     if request.method == 'POST':
#         form = TractionSheetEditForm(request.POST,instance=content)
        
#         if form.is_valid():
#             content = form.save(commit=False)
#             content.not_allow_edit_option()
#             content.update_date()
#             content.save()
#             messages.add_message(request, messages.INFO, 'Traction report edited successfully.')
#             return redirect(dashboard)
#     else:
#         form = TractionSheetEditForm(instance=content)
        
#     return render(request,'edit_traction_sheet.html',{'form':form})


def blogPost(request):
    posts = BlogPost.objects.all().order_by('-date_of_creation')
    return render(request,'blogPost.html',{'posts':posts})

@login_required
def newBlogPost(request):
    
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        blog_img = request.FILES['blog_img']
        
        post = BlogPost.objects.create(title=title,description=description,blog_img=blog_img)
        post.save()
        messages.add_message(request, messages.INFO, 'Blog posted successfully.')
        return redirect('blogPost')
    

    return redirect('blogPost')

@login_required
def delete_blogPost(request):
    if request.method == 'POST':
        getpk = request.POST['foo']
        details = get_object_or_404(BlogPost,pk=int(getpk))
        details.delete()
        messages.add_message(request, messages.INFO, 'Blog deleted')
    return redirect('blogPost')

@login_required
def edit_blogPost(request):

    if request.method == "POST":
        getpk = request.POST['pk_val']
        title = request.POST['title']
        description = request.POST['description']
        details = get_object_or_404(BlogPost,pk=int(getpk))
        if title:
            title = title
        else:
            title = ' '
        
        if description:
            description = description
        else:
            description = ' '

        details.update_blogPost(title = title,description = description)
    return redirect('blogPost')

def queries(request):
    values = Query.objects.all().order_by('-submitted_date')
    return render(request,'query.html',{'values':values})

@login_required
def delete_query(request):
    if request.method == 'POST':
        getpk = request.POST['foo']
        details = get_object_or_404(Query,pk=int(getpk))
        details.delete()
    return redirect('queries')


@login_required
def generate_work(request):
    
    if request.method == 'POST':
        
        from_user = request.POST['from']
        to = request.POST['to']
        title = request.POST['title']
        work_description = request.POST['work_description']
        suggestions = request.POST['suggestions']
        remarks = request.POST['remarks']
        checkbox = request.POST.get('upload_checkbox',None)
        if checkbox: 
            document = request.FILES['document']
        
        from_obj = Account.objects.get(pk=int(from_user))
        
        obj = Admin.objects.get(pk=int(to))
        
        if checkbox:
            work = WorkGenerator.objects.create(from_user=from_obj.fullname,to=obj,title=title,work_description=work_description,suggestions=suggestions,remarks=remarks,document=document,from_user_pk=from_user)
        else:
            work = WorkGenerator.objects.create(from_user=from_obj.fullname,to=obj,title=title,work_description=work_description,suggestions=suggestions,remarks=remarks,from_user_pk=from_user)
        work.change_status(status="Not Started..")

        send_mail(
                'My Work',
                'You got a new work . Please go checkout at www.aicnitf.in .',
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Work Generated successfully.')
        return redirect('dashboard')
    return redirect('index')

@login_required
def edit_work(request):
    if request.method == "POST":
        pk = request.POST['pk_val']
        title = request.POST['title']
        work_description = request.POST['work_description']
        suggestions = request.POST['suggestions']
        remarks = request.POST['remarks']

        work_obj = WorkGenerator.objects.get(pk=pk)

        if title:
            title = title
        else:
            title = ' '
        
        if work_description:
            work_description = work_description
        else:
            work_description = ' '

        if suggestions:
            suggestions = suggestions
        else:
            suggestions = ' '
        
        if remarks:
            remarks = remarks
        else:
            remarks = ' '

        work_obj.update_work(title = title,work_description = work_description,suggestions = suggestions,remarks=remarks)
        messages.add_message(request, messages.INFO, 'Work Edited successfully.')
    return redirect('dashboard')


@login_required
def start(request,pk):
    work_obj = WorkGenerator.objects.get(pk=pk)
    work_obj.change_status(status="pending...")
    return redirect('dashboard')

@login_required
def completed(request):
    if request.method == 'POST':
        pk = request.POST['complete_pk']
        ford_pk = request.POST['ford_complete_pk']
        end_statement = request.POST['end_statement']
        checkbox = request.POST.get('upload_checkbox',None)
        if checkbox: 
            end_document = request.FILES['end_document']
        
        if checkbox:
            if ford_pk:
                obj = Forward.objects.get(pk=int(ford_pk))
                obj.forward_work.update_end_msg(end_statement=end_statement +" (work completed by " +obj.to.account.fullname +")",end_document=end_document)
                obj.forward_work.change_status(status="completed")
                obj.forward_work.update_date()
                return redirect('dashboard')
            else:
                work_obj = WorkGenerator.objects.get(pk=int(pk))
                work_obj.update_end_msg(end_statement=end_statement+" work completed by " +work_obj.to.account.fullname,end_document=end_document)
                work_obj.change_status(status="completed")
                work_obj.update_date()
                return redirect('dashboard')
        else:
            if ford_pk:
                obj = Forward.objects.get(pk=int(ford_pk))
                obj.forward_work.update_end_msg(end_statement=end_statement +" (work completed by " +obj.to.account.fullname +")")
                obj.forward_work.change_status(status="completed")
                obj.forward_work.update_date()
                return redirect('dashboard')
            else:
                work_obj = WorkGenerator.objects.get(pk=int(pk))
                work_obj.update_end_msg(end_statement=end_statement+" (work completed by " +work_obj.to.account.fullname +")")
                work_obj.change_status(status="completed")
                work_obj.update_date()
                return redirect('dashboard')
    return redirect('dashboard')

@login_required
def forward_work(request):
    if request.method == 'POST':
        from_user = request.POST['from']
        to = request.POST['to']
        pk = request.POST['pk_val']
        forward_pk = request.POST['pk_val2']
        suggestions = request.POST['suggestions']
        checkbox = request.POST.get('upload_checkbox',None)
        if checkbox: 
            ford_document = request.FILES['ford_document']

        from_obj = Account.objects.get(pk=int(from_user))
        
        obj = Admin.objects.get(pk=int(to))
        
        work_obj = WorkGenerator.objects.get(pk=int(pk))
        
        if checkbox:
            work = Forward.objects.create(from_user=from_obj.fullname,to=obj,forward_work=work_obj,suggestions=suggestions,from_user_pk=from_user,forward_pk=forward_pk,ford_document=ford_document)
        else:
            work = Forward.objects.create(from_user=from_obj.fullname,to=obj,forward_work=work_obj,suggestions=suggestions,from_user_pk=from_user,forward_pk=forward_pk)

        status_obj = WorkGenerator.objects.get(pk=int(pk))
        
        # if status_obj.status == "returned":
        #     ret_obj = Return.objects.get(pk=int(forward_pk))
        #     ret_obj.delete()

        if status_obj.forwarded == False:
            status_obj.forward(from_obj.fullname,obj.account.fullname)
        else:
            for_obj = Forward.objects.get(pk=int(forward_pk))
            for_obj.forther_forward() 
        status_obj.change_status(status="forwarded->")
        work.save()

        fm_ob = from_obj.admin_set.all()[0]
        send_mail(
                'Forwarded Work',
                'you got a work by work ' +from_obj.fullname ,
                fm_ob,
                [obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Work Forwarded successfully.')
        return redirect('dashboard')

@login_required
def return_work(request):
    if request.method == 'POST':
        from_user = request.POST['from']
        to = request.POST['to']
        work_pk = request.POST['work_pk']
        suggestions = request.POST['suggestions']
        ford_work_pk = request.POST['ford_work_pk']
        
        
        from_obj = Account.objects.get(pk=int(from_user))
        
        obj = Account.objects.get(pk=int(to))
        to_obj = obj.admin_set.all()[0]
        
        work_obj = WorkGenerator.objects.get(pk=int(work_pk))
        

        return_obj = Return.objects.create(from_user=from_obj.fullname,to=to_obj,work=work_obj,message=suggestions)

        if work_obj.forwarded:
            ford_obj = Forward.objects.get(pk=int(ford_work_pk))
            
            return_obj.assign_forward_pk(forward_pk=ford_obj.forward_pk)
            if ford_obj.forward_pk:
                old_ford_obj = Forward.objects.get(pk=ford_obj.forward_pk)
                old_ford_obj.remove_forward()
            else:
                work_obj.remove_forward()
            ford_obj.delete()
        else:
            work_obj.make_null()
        work_obj.change_status(status="returned")
        return_obj.save()
        fm_ob = from_obj.admin_set.all()[0] 
        send_mail(
                'Return Work',
                'you receved a return work',
                fm_ob,
                [to_obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Work Returned successfully.')
        return redirect('dashboard')

@login_required
def reassign(request):
    
    if request.method == 'POST':
        from_user = request.POST['from']
        to = request.POST['to']
        work_pk = request.POST['pk_val']
        rk_val = request.POST['rk_val']
        
        
        obj = Admin.objects.get(pk=int(to))
        
        work_obj = WorkGenerator.objects.get(pk=int(work_pk))
        
        ret = Return.objects.get(pk=int(rk_val))
        
        work_obj.update_to(to=obj)
        work_obj.make_new_work()
        work_obj.change_status(status="Not Started..")
        ret.delete()
        send_mail(
                'My Work',
                'You got a new work . Please go checkout at www.aicnitf.in .',
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Work Reassigned successfully.')
        return redirect('dashboard')

@login_required
def return_start(request,pk):
    ret_obj = Return.objects.get(pk=pk)
    if ret_obj.forward_pk:
        ford_obj = Forward.objects.get(pk=int(ret_obj.forward_pk))
        ford_obj.forward_work.change_status(status="pending...")
        ford_obj.remove_forward()
    else:
        work_obj = ret_obj.work
        work_obj.change_status(status="pending...")
        work_obj.remove_forward()
    ret_obj.delete()
    return redirect('dashboard')

@login_required
def delete_work(request,pk):
    ret_obj = Return.objects.get(pk=pk)
    if request.user.is_adminstrator and ret_obj.work.forwarded == False:
        ret_obj.work.delete()
    else:
        ret_obj.delete()
    return redirect('dashboard')



@login_required
def new_work_clicked(request):
    pk = request.GET.get('pk',None)
    work = WorkGenerator.objects.get(pk=pk)

    work.new_work = False
    work.alert = False
    work.save()
    data = {
        'new_work':work.new_work,
        'alert':work.alert
    }
    return JsonResponse(data)

@login_required
def forward_work_clicked(request):
    pk = request.GET.get('pk',None)
    
    work = Forward.objects.get(pk=pk)
    
    work.new_forward = False
    work.alert = False
    work.save()
    data = {
        'new_work':work.new_forward,
        'alert':work.alert
    }
    return JsonResponse(data)
@login_required
def return_work_clicked(request):
    pk = request.GET.get('pk',None)
    work = Return.objects.get(pk=pk)
    
    work.new_return = False
    work.save()
    data = {
        'new_work':work.new_return
    }
    return JsonResponse(data)

@login_required
def leave_app_clicked(request):
    pk = request.GET.get('pk',None)
    leave = LeaveApplication.objects.get(pk=pk)
    
    leave.new_leave = False
    leave.reply = False
    leave.save()
    data = {
        'new_leave':leave.new_leave,
        'reply':leave.reply
    }
    return JsonResponse(data)

def return_work_status(request):
    pk = request.GET.get('pk',None)
    work = Return.objects.get(pk=pk)
    data = {
        'new_work':work.new_return
    }
    return JsonResponse(data) 

def new_work_status(request):
    pk = request.GET.get('pk',None)
    work = WorkGenerator.objects.get(pk=pk)
    data = {
        'new_work':work.new_work,
        'alert':work.alert
    }
    return JsonResponse(data)

def forward_work_status(request):
    pk = request.GET.get('pk',None)
    work = Forward.objects.get(pk=pk)
    data = {
        'new_work':work.new_forward,
        'alert':work.alert
    }
    return JsonResponse(data)

def leave_app_status(request):
    pk = request.GET.get('pk',None)
    leave = LeaveApplication.objects.get(pk=pk)
    data = {
        'new_leave':leave.new_leave,
        'reply':leave.reply,
    }
    return JsonResponse(data)

def alert(request,pk):
    work_obj = WorkGenerator.objects.get(pk=pk)
    work_obj.update_alert()
    send_mail(
                'Alert Message',
                'you got a Reminder from (Adminstrator) complete your work in given time.' ,
                'support@aicnalanda.com',
                [work_obj.to.email],
                fail_silently=False,
            )
    messages.add_message(request, messages.INFO, 'Reminder sended successfully.')
    return redirect('dashboard')

def forward_alert(request,pk):
    ford_work_obj = Forward.objects.get(pk=pk)
    ford_work_obj.update_alert()
    send_mail(
                'Alert Message',
                'you got a Reminder from ' +ford_work_obj.from_user +' complete your work in given time.' ,
                'support@aicnalanda.com',
                [ford_work_obj.to.email],
                fail_silently=False,
            )
    messages.add_message(request, messages.INFO, 'Reminder sended successfully.')
    return redirect('dashboard')




def count_values(request):
    returns = Return.objects.filter(work__new_work = True)
    
    data = {
        'returns':len(returns)
    }
    return JsonResponse(data)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/document")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def verify_uname(request):
    uname = request.GET.get('uname',None)
    data = {
        'exist': Account.objects.filter(username = uname).exists(),
    }
    return JsonResponse(data)

def uname_pwd_check(request):
    uname = request.GET.get('uname',None)
    pwd = request.GET.get('pwd',None)
    user = auth.authenticate(request,username=uname,password=pwd)
    exist = False
    if user is not None:
        exist = True
    
    else:
        exist = False

    
    data = {
        'exist':exist
    }
    return JsonResponse(data)

def forget_username(request):
    uname = request.GET.get('uname',None)
    user = Account.objects.filter(username=uname).first()
    if user is not None:
        if user.is_admin:
            admin = user.admin_set.first()
            email = admin.email
        if user.is_startup:
            startup = user.startup_set.first()
            email = startup.email
        if user.is_sanvriddhi:
            sanvriddhi = user.sanvriddhi_set.first()
            email = sanvriddhi.email
        if user.is_viewer:
            viewer = user.viewer_set.first()
            email = viewer.email
        if user.is_ideanest_check:
            ideanest = user.ideanestcheck_set.first()
            email = ideanest.email
        if user.is_ideanest_viewer:
            viewer = user.viewerideanest_set.first()
            email = viewer.email
    else:
        email = None
    data = {
        'is_exist': Account.objects.filter(username=uname).exists(),
        'email':email
    }
    

    return JsonResponse(data)


def forget_email_sending(request):
    email = request.GET.get('email',None)
    num_list = ['1','2','3','4','5','6','7','8','9']
    otp = random.sample(num_list,4)
    str_otp = ''.join(otp)
    
    send_mail(
    'Password Reset OTP',
    'Your one time password to reset AICNITF account is :{0}'.format(str_otp),
    'support@aicnalanda.com',
    [email],
    fail_silently=False,
    )
    data = {
        'correct_otp':str_otp
    }
    return JsonResponse(data)


def set_password(request):
    password = request.GET.get('password',None)
    uname = request.GET.get('username',None)
    user = Account.objects.get(username=uname)
   
    user.set_password(password)
    user.save()
    data = {
        'uname':uname
    }
    return JsonResponse(data)


def apply_leave(request):
    if request.method == 'POST':
        # subject = request.POST['subject']
        body = request.POST['body']
        from_user_pk = request.POST['from_value']
        cl_or_sl = request.POST['cl_or_sl']
        days = request.POST['days']
        
        from_user_obj = get_object_or_404(Account,pk=from_user_pk)
        from_user = from_user_obj.admin_set.all()[0]
        to_obj = Account.objects.filter(is_adminstrator = True)[0]
        to = to_obj.fullname
        leave_obj = LeaveApplication.objects.create(from_user=from_user,from_user_name=from_user.account.fullname,to=to,body=body,status="pending",cl_or_sl=cl_or_sl,days=days) 
        leave_obj.save()

        user_obj = request.user
        user = user_obj.admin_set.all()[0]
        if leave_obj.cl_or_sl == "CL":
            leave_obj.subject = "CASUAL LEAVE"
            leave_obj.save()
            user.cl = int(user.cl) - int(days)
            user.save()
        else:
            leave_obj.subject = "SICK LEAVE"
            leave_obj.save()
            user.sl = int(user.sl) - int(days)
            user.save()
        messages.add_message(request, messages.INFO, 'Successfully sended.')
        return redirect(dashboard)

def accept_or_reject(request):
    if request.method == 'POST':
        message = request.POST['message']
        leave_pk = request.POST['leave_pk']
        status_value = request.POST['status_value']

        obj = LeaveApplication.objects.get(pk=int(leave_pk))
        obj.reply = True
        if status_value == "Accepted":
            obj.update_message(message)
            obj.update_status(status_value)
        else:
            obj.update_message(message)
            obj.update_status(status_value)
            if obj.cl_or_sl == "CL":
                obj.from_user.cl = int(obj.from_user.cl) + int(obj.days)
                obj.from_user.save()
            else:
                obj.from_user.sl = int(obj.from_user.sl) + int(obj.days)
                obj.from_user.save()
        messages.add_message(request, messages.INFO, 'Successfully sended.')

        return redirect(dashboard)


def timein(request):
    user_obj = request.user
    user = user_obj.admin_set.all()[0]
    time = Attendence.objects.create(employee=user)
    time.time_status = False
    time.save()
    messages.add_message(request, messages.INFO, 'Time IN')
    return redirect(dashboard)

def timeout(request,pk):
    obj = get_object_or_404(Attendence,pk=int(pk))
    obj.update_timeout()
    h1 = int(obj.timein.strftime("%H"))
    m1 = int(obj.timein.strftime("%M"))
    s1 = int(obj.timein.strftime("%S"))


    h2 = int(obj.timeout.strftime("%H"))
    m2 = int(obj.timeout.strftime("%M"))
    s2 = int(obj.timeout.strftime("%S"))

    H = M = S = 0

    if s2>=s1:
        S = s2 - s1
    else:
        S = (60+s2) - s1
        m2 = m2 - 1
    if m2>=m1:
        M = m2 - m1
    else:
        M = (60+m2) - m1
        h2 = h2 - 1

    if h2>=h1:
        H = h2 - h1
    else:
        H = 0
    total = str(H) +":" +str(M) +":" +str(S)

    obj.update_total_time(total)             
    messages.add_message(request, messages.INFO, 'Time OUT')
    return redirect(dashboard)


def timeoutall(request):
    today = date.today()
    obj_list = Attendence.objects.filter(timeout=None,date=today)
   
    for lis in obj_list:
        lis.update_timeout()
        h1 = int(lis.timein.strftime("%H"))
        m1 = int(lis.timein.strftime("%M"))
        s1 = int(lis.timein.strftime("%S"))

        h2 = int(lis.timeout.strftime("%H"))
        m2 = int(lis.timeout.strftime("%M"))
        s2 = int(lis.timeout.strftime("%S"))

        H = M = S = 0
        if s2>=s1:
            S = s2 - s1
        else:
            S = (60+s2) - s1
            m2 = m2 - 1
        if m2>=m1:
            M = m2 - m1
        else:
            M = (60+m2) - m1
            h2 = h2 - 1

        if h2>=h1:
            H = h2 - h1
        else:
            H = 0
        total1 = str(H) +":" +str(M) +":" +str(S)

        lis.update_total_time(total1)
    messages.add_message(request, messages.INFO, 'All Employees Time OUT')
    return redirect(dashboard)


def employee_message(request):
    if request.method == 'POST':
        message = request.POST['message']

        mess = EmpMessage.objects.create(message=message)

        admin_val = Admin.objects.all()
        
        lis = []
        for admin_list in admin_val:
            if admin_list.account.is_superadmin == False and admin_list.account.is_adminstrator == False:
                lis.append(admin_list.email)

        send_mail(
                'Message From Administrator',
                message,
                'support@aicnalanda.com',
                lis,
                fail_silently=False,
            )
    messages.add_message(request, messages.INFO, 'Message send to all Employees')
    return redirect(dashboard)
    


def test(request):
    print("------------------")
    return render(request,'new_dashboard/admin/admin-base.html')
