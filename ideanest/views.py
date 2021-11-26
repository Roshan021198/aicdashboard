from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import auth
import random
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,Http404,JsonResponse
from useraccounting.models import Account,Ideanestcheck,Sessionideanest,Submissionideanest,Viewerideanest,Ideanestweek
#,Ideanest,IdeanestSession,Ideanestsubmission,Ideanestviewer
from .forms import IdeanestEditForm
import datetime
import xlwt

# Create your views here.
def ideanest(request):
    return render(request,'ideanest.html')


def ideanest_form(request):
    return render(request,'ideanest_iframe.html')



def ideanest_nomination(request):
    return render(request,'ideanest_nomination.html')

def ideanest_dashboard(request):
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
    

def create_ideanest_session(request):
    if request.method == 'POST':
        week = request.POST['weekselect']
        session_name = request.POST['session_name']
        session_details = request.POST['session_details']
        session_date = request.POST['session_date']
        time = request.POST['time']
        time_out = request.POST['time_out']
        pm_am1 = request.POST['pm_am1']
        pm_am2 = request.POST['pm_am2']
        meeting_link = request.POST['meeting_link']
        submission_link = request.POST['submission_link']
        if request.FILES.get('pre_read') and request.FILES.get('assignment'):
            assignment = request.FILES['assignment']
            pre_read = request.FILES['pre_read']
        elif request.FILES.get('assignment'):
            assignment = request.FILES['assignment']
            pre_read = None
        elif request.FILES.get('pre_read'):
            assignment = None
            pre_read = request.FILES['pre_read']
        else:
            pre_read = None
            assignment = None

        week = Ideanestweek.objects.filter(week_no=week)[0]

        session_obj = Sessionideanest.objects.create(week=week,session_name=session_name,session_details=session_details,session_date=session_date,time=time,time_out=time_out,pm_am1=pm_am1,pm_am2=pm_am2,meeting_link=meeting_link,pre_read=pre_read,assignment=assignment,submission_link=submission_link)
        messages.add_message(request, messages.INFO, 'Ideanest Created Successfully')
        return redirect(ideanest_dashboard)

def ideanest_submission(request):
    user = request.user
    ideanest_user = user.ideanestcheck_set.all()[0]
    if request.method == 'POST':
        session_topic = request.POST['session_topic']
        if len(request.FILES) != 0:
            attachment = request.FILES['attachment']
        else:
            attachment = None
        
        submit_obj = Submissionideanest.objects.create(connect_sanvriddhi=ideanest_user,session_topic=session_topic,attachment=attachment)
        return redirect(ideanest_dashboard)


@login_required
def ideanest_edit_form(request,pk):
    
    content = get_object_or_404(Ideanestcheck,pk=pk)
    
    if request.method == 'POST':
        form = IdeanestEditForm(request.POST,request.FILES,instance=content)
        
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            messages.add_message(request, messages.INFO, 'Edited successfully.')
            return redirect(ideanest_dashboard)
    else:
        form = IdeanestEditForm(instance=content)
        
    return render(request,'ideanest_edit_form.html',{'form':form})


def ideanest_excel(request):
    responce = HttpResponse(content_type='application/ms-excel')
    responce['content-Disposition'] = 'attachment; filename=Ideanest' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Ideanestcheck')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.bold = True
    columns = ['startup name','contact no','Email','legal Entity','Founder','Founders designation','website','city','sector','team_members','location','Company Identification Number','Current level of Incubatee','Operational Model','Type of Incubatee','Women Led Startup','Startup working towards any of the flagship government programmes','MSME registered','DIPP registered','Date of Registration of the legal entity of the startup','Start Date of the Incubation','startup_img','founder_img']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style = xlwt.XFStyle()
    
    rows = Ideanestcheck.objects.values_list('startup_name','contact_no','email','legal_entity','team_head','founders_designation','website','city','sector','team_members','location','comp_identification_no','inubatee_level','operational_model','type_of_incubatee','women_led_startup','gov_program','msme_registered','dspp_registered','legal_entity_register','start_date_incubation','startup_img','founder_img')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)

    wb.save(responce)
    return responce

def ideanest_recording(request):
    if request.method == 'POST':
        sessionname = request.POST['sessionname']
        recording_link = request.POST['recording_link']
        recording_pw = request.POST['recording_pw']

        obj = get_object_or_404(Sessionideanest,pk=int(sessionname))

        obj.update_session(recording_link=recording_link,recording_pw=recording_pw)
        return redirect(ideanest_dashboard)
    return redirect(ideanest_dashboard)