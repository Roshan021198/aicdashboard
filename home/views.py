from django.shortcuts import render,redirect
from useraccounting.models import Account,Admin,StartUp,Query,Gallery,Admin,StartUp,Sanvriddhi,Viewer
from django.contrib import messages

# Create your views here.
def index(request):
    values = Account.objects.filter(is_admin=True).order_by('rank')
    imp_values = []
    required_val = values[1:]
    for i in required_val:
        imp_values.append(i.admin_set.all()[0])
    gal_val = Gallery.objects.all()
    user = request.user

    if request.user.is_authenticated:
        if user.is_admin:
            profile_img_obj = user.admin_set.all()[0]
        elif user.is_startup:
            profile_img_obj = user.startup_set.all()[0]
        elif user.is_sanvriddhi:
            profile_img_obj = user.sanvriddhi_set.all()[0]
        elif user.is_viewer:
            profile_img_obj = user.viewer_set.all()[0]
        elif user.is_ideanest_check:
            profile_img_obj = user.sanvriddhi_set.all()[0]
        elif user.is_ideanest_viewer:
            profile_img_obj = user.viewer_set.all()[0]
    else:
        profile_img_obj = None
        
    return render(request,'index.html',{'values':imp_values,'gal_val':gal_val,'profile_img_obj':profile_img_obj})    
    #return render(request,'index.html')


def query_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        about = request.POST['about']
        email = request.POST['email']
        message = request.POST['message']
    
        query = Query.objects.create(name=name,about=about,email=email,message=message)
        messages.add_message(request, messages.INFO, 'Query Submitted.')
        return redirect(index)
    return redirect(index)



def SWEA(request):
    return render(request,'SWEA.html')


def callForApplication(request):
    return render(request,'callforapplication.html')

def CFA(request):
    return render(request,'CFA.html')

def test123(request):
    print("------------------")
    return render(request,'new_dashboard/admin/test.html')
