from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from .models import Startup_app_form,Enterpreneur_form,upload,logo
from django.contrib import messages
import datetime
import xlwt

def anantya(request):
    partners = logo.objects.all()
    return render(request,'application.html',{'partners':partners})

def startup_form_app(request):
    down = upload.objects.all()[0]
    return render(request,'startup_application_form.html',{'down':down})

def entrepreneur_form(request):
    return render(request,'entrepreneur_form.html')

def entrepreneurform(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        district = request.POST['district']
        company_name = request.POST['company_name']
        designation = request.POST['designation']
        sector = request.POST['sector']
        date_incorporation = request.POST['date_incorporation']
        location = request.POST['location']
        turnover = request.POST['turnover']
        journey = request.POST['journey']
        achievements = request.POST['achievements']
        awards = request.POST['awards']
        impact = request.POST['impact']
        vision = request.POST['vision']
        nomination = request.POST['nomination']
        
        
        post = Enterpreneur_form.objects.create(name=name,contact=contact,email=email,district=district,company_name=company_name,designation=designation,sector=sector,date_incorporation=date_incorporation,location=location,turnover=turnover,journey=journey,achievements=achievements,awards=awards,impact=impact,vision=vision,nomination=nomination)
        post.save()
        messages.add_message(request, messages.INFO, 'Form submited successfully.')
        return redirect('entrepreneur_form')
    return render(request,'entrepreneur_form.html')

def startupform(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        district = request.POST['district']
        company_name = request.POST['company_name']
        designation = request.POST['designation']
        sector = request.POST['sector']
        date_incorporation = request.POST['date_incorporation']
        problem_solving = request.POST['problem_solving']
        solution = request.POST['solution']
        uniqueness = request.POST['uniqueness']
        advantages = request.POST['advantages']
        operation_stage = request.POST['operation_stage']
        revenue = request.POST['revenue']
        if len(request.FILES) != 0:
            startup_img = request.FILES['startup_img']
        else:
            startup_img = "awardimg/blank.png"
        vid_link = request.POST['vid_link']
        pitch_startup = request.POST['pitch_startup']


        if pitch_startup == 'Yes':
            folder_file = request.FILES['folder_file']
            post = Startup_app_form.objects.create(name=name,contact=contact,email=email,district=district,company_name=company_name,designation=designation,sector=sector,date_incorporation=date_incorporation,problem_solving=problem_solving,solution=solution,uniqueness=uniqueness,advantages=advantages,operation_stage=operation_stage,revenue=revenue,startup_img=startup_img,vid_link=vid_link,pitch_startup=pitch_startup,folder_file=folder_file)
            post.save()
            messages.add_message(request, messages.INFO, 'Form submited successfully.')
            return redirect('startup_form_app') 
        else:
            post = Startup_app_form.objects.create(name=name,contact=contact,email=email,district=district,company_name=company_name,designation=designation,sector=sector,date_incorporation=date_incorporation,problem_solving=problem_solving,solution=solution,uniqueness=uniqueness,advantages=advantages,operation_stage=operation_stage,revenue=revenue,startup_img=startup_img,vid_link=vid_link,pitch_startup=pitch_startup)
            post.save()
            messages.add_message(request, messages.INFO, 'Form submited successfully.')
            return redirect('startup_form_app') 
    return render(request,'startup_application_form.html')


def details(request):
    ent_val = Enterpreneur_form.objects.all()
    str_val = Startup_app_form.objects.all()
    ent_len = len(ent_val)
    str_len = len(str_val)
    return render(request,'application_details.html',{'ent_len':ent_len,'str_len':str_len,'ent_val':ent_val,'str_val':str_val})

def eligibility(request):
    return render(request,'eligibility.html')



def entrepreneur_excel(request):
    responce = HttpResponse(content_type='application/ms-excel')
    responce['content-Disposition'] = 'attachment; filename=Enterpreneur_form' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Enterpreneur_form')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.bold = True
    columns = ['name','contact','email','district','company_name','designation','sector','date Of Incorporation','location','turnover','journey','achievemenents','awards','impact','vision','nominations']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style = xlwt.XFStyle()
    
    rows = Enterpreneur_form.objects.values_list('name','contact','email','district','company_name','designation','sector','date_incorporation','location','turnover','journey','achievements','awards','impact','vision','nomination')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)

    wb.save(responce)
    return responce



def startup_excel(request):
    responce = HttpResponse(content_type='application/ms-excel')
    responce['content-Disposition'] = 'attachment; filename=Startup_app_form' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Startup_app_form')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.bold = True
    columns = ['name','contact','email','district','company_name','designation','sector','date Of Incorporation','problem_solving','solution','uniqueness','advantages','operation_stage','revenue','startup_img','vid_link','pitch_startup','folder_file']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    
    font_style = xlwt.XFStyle()
    
    rows = Startup_app_form.objects.values_list('name','contact','email','district','company_name','designation','sector','date_incorporation','problem_solving','solution','uniqueness','advantages','operation_stage','revenue','startup_img','vid_link','pitch_startup','folder_file')

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)

    wb.save(responce)
    return responce