from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Account,Admin,StartUp,TeamMembers,WorkGenerator,Forward,Return,MoM,BlogPost,Query,Gallery,LeaveApplication,Attendence,EmpMessage,MonitorSheetReport,Sanvriddhi,Session,Submission,Viewer,Ideanestchecking,Sessionideanesting,Viewerideanesting,Submissionideanesting,Sanvriddhiweek,Sanvriddhifeedback,Ideanestweek,Ideanestfeedback,StartupCategory
# Register your models here.
admin.site.register(Account)
admin.site.register(Admin)
admin.site.register(StartUp)
admin.site.register(TeamMembers)
admin.site.register(MonitorSheetReport)
admin.site.register(WorkGenerator)
admin.site.register(Forward)
admin.site.register(Return)
admin.site.register(MoM)
admin.site.register(BlogPost)
admin.site.register(Query)
admin.site.register(Gallery)
admin.site.register(LeaveApplication)
admin.site.register(Attendence)
admin.site.register(EmpMessage)

admin.site.register(Sanvriddhi)
admin.site.register(Session)
admin.site.register(Submission)
admin.site.register(Viewer)

admin.site.register(Ideanestchecking)
admin.site.register(Sessionideanesting)
admin.site.register(Submissionideanesting)
admin.site.register(Viewerideanesting)

admin.site.register(Sanvriddhiweek)
admin.site.register(Sanvriddhifeedback)

admin.site.register(Ideanestweek)
admin.site.register(Ideanestfeedback)



admin.site.register(StartupCategory)