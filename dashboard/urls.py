from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('admin_form/',views.admin_form,name='admin_form'),
    path('startup_form/',views.startup_form,name='startup_form'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('profile/<int:pk>/edit_startup/',views.startup_profile_edit,name='startup_profile_edit'),
    
    path('edit_emp_form',views.edit_emp_form,name='edit_emp_form'),
    path('profile/delete_employee/',views.delete_employee,name='delete_employee'),
    path('edit_emp_form',views.edit_emp_form,name='edit_emp_form'),
    path('userprofile/<int:pk>/',views.userprofile,name='userprofile'),
    path('add_new_team_member',views.add_new_team_member,name='add_new_team_member'),
    
    path('delete_team_member',views.delete_team_member,name='delete_team_member'),
    path('edit_team_member',views.edit_team_member,name='edit_team_member'),

    path('monitor_form/',views.monitor_form,name='monitor_form'),
    path('monitor_report/<int:pk>/',views.monitor_report,name='monitor_report'),
    
    path('allowedit/<int:pk>',views.allowedit,name='allowedit'),
    path('monitor_sheet_edit/<int:pk>',views.monitor_sheet_edit,name='monitor_sheet_edit'),

    # path('traction_form/',views.traction_form,name='traction_form'),
    # path('traction_report/<int:pk>/',views.traction_report,name='traction_report'),
    # path('allow_traction_edit/<int:pk>',views.allow_traction_edit,name='allow_traction_edit'),
    # path('edit_traction_sheet/<int:pk>',views.edit_traction_sheet,name='edit_traction_sheet'),

    path('send_mom',views.send_mom,name='send_mom'),
    path('blogPost',views.blogPost,name='blogPost'),
    path('newBlogPost',views.newBlogPost,name='newBlogPost'),


    path('visit_startup/',views.visit_startup,name='visit_startup'),
    path('generate_work/',views.generate_work,name='generate_work'),
    path('edit_work/',views.edit_work,name='edit_work'),

    path('start/<int:pk>/',views.start,name='start'),
    path('completed/',views.completed,name='completed'),

    path('forward_work/',views.forward_work,name='forward_work'),
    path('return_work/',views.return_work,name='return_work'),
    path('reassign/',views.reassign,name='reassign'),
    path('return_start/<int:pk>/',views.return_start,name='return_start'),

    path('delete_work/<int:pk>',views.delete_work,name='delete_work'),
    

    path('new_work_clicked',views.new_work_clicked,name='new_work_clicked'),
    path('count_values',views.count_values,name='count_values'),
    path('forward_work_clicked',views.forward_work_clicked,name='forward_work_clicked'),
    path('return_work_clicked',views.return_work_clicked,name='return_work_clicked'),

    path('verify_uname',views.verify_uname,name='verify_uname'),

    path('uname_pwd_check',views.uname_pwd_check,name='uname_pwd_check'),

    path('forget_username',views.forget_username,name='forget_username'),

    path('forget_email_sending',views.forget_email_sending,name='forget_email_sending'),

    path('set_password',views.set_password,name='set_password'),
    path('delete_blogPost',views.delete_blogPost,name='delete_blogPost'),
    path('edit_blogPost',views.edit_blogPost,name='edit_blogPost'),
    path('queries',views.queries,name='queries'),
    path('delete_query',views.delete_query,name='delete_query'),

    path('return_work_status',views.return_work_status,name='return_work_status'),    
    path('forward_work_status',views.forward_work_status,name='forward_work_status'),
    path('new_work_status',views.new_work_status,name='new_work_status'),

    path('alert/<int:pk>',views.alert,name='alert'),
    path('forward_alert/<int:pk>',views.forward_alert,name='forward_alert'),

    path('apply_leave',views.apply_leave,name='apply_leave'),
    path('accept_or_reject',views.accept_or_reject,name='accept_or_reject'),

    path('leave_app_status',views.leave_app_status,name='leave_app_status'),
    path('leave_app_clicked',views.leave_app_clicked,name='leave_app_clicked'),

    path('timein',views.timein,name='timein'),
    path('timeout/<int:pk>',views.timeout,name='timeout'),

    path('employee_message',views.employee_message,name='employee_message'),
    path('timeoutall',views.timeoutall,name='timeoutall'),

    path('test/',views.test,name='test')






]
