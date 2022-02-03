from django import forms
from useraccounting.models import StartUp,Admin,MonitorSheetReport,BlogPost

class StartUpForm(forms.ModelForm):

            
    class Meta:
        model = StartUp
        exclude = ['account']
        fields = ('__all__')
        CHOICES = [
            ('Yes','Yes'),
            ('No','No'),
        ]

        INCUBATEE = [
            ('Physical','Physical'),
            ('Virtual','Virtual'),
        ]

        INCUBATEELEBEL = [
            ('Idation','Idation'),
            ('POC','POC'),
            ('Prototype','Prototype'),
            ('Minimum Vaiable Product','Minimum Viable Product'),
            ('Commercialized','Commercialized'),
        ]

        OPERATIONALMODEL = [
            ('Product Manufacturing','Product Manufacturing'),
            ('Service Delivery','Service Delivery'),
            ('Aggregation Platform','Aggregation Platform'),
            ('Other','Other'),
        ]

        SECTOR = [
            ('Agriculture and Allied Fields','Agriculture and Allied Fields'),
            ('Electricity, New and Renewable energy and Environment sustainability','Electricity, New and Renewable energy and Environment sustainability'),
            ('Education','Education'),
            ('Health and Pharmaceuticals','Health and Pharmaceuticals'),
            ('Water Sanitation and Solid waste management','Water Sanitation and Solid waste management'),
            ('Others','Others'),
        ]

        GOVERNMENT = [
            ('Women Empowerment ','Women Empowerment '),
            ('Make In India','Make In India'),
            ('Swachh Bharat ','Swachh Bharat '),
            ('Startup India','Startup India'),
            ('Beti Bachao Beti padhao','Beti Bachao Beti padhao'),
            ('None the above','None the above'),
        ]

        widgets = {
            'email'                     : forms.EmailInput(attrs={'class':'form-control'}),
            'startup_name'			    : forms.TextInput(attrs={'class':'form-control'}),
            'legal_entity'			    : forms.TextInput(attrs={'class':'form-control'}),
            'founders_designation'	    : forms.TextInput(attrs={'class':'form-control'}),
            'website'					: forms.TextInput(attrs={'class':'form-control'}),
            'city'					    : forms.TextInput(attrs={'class':'form-control'}),
            'sector'					: forms.Select(choices=SECTOR,attrs={'class':'form-control'}),
            'team_members'			    : forms.TextInput(attrs={'class':'form-control'}),
            'location'				    : forms.TextInput(attrs={'class':'form-control'}),
            'contact_no'				: forms.TextInput(attrs={'class':'form-control'}),
            'team_head'				    : forms.TextInput(attrs={'class':'form-control'}),

            'comp_identification_no'	: forms.TextInput(attrs={'class':'form-control'}),
            'inubatee_level'			: forms.Select(choices=INCUBATEELEBEL,attrs={'class':'form-control'}),
            'operational_model'		    : forms.Select(choices=OPERATIONALMODEL,attrs={'class':'form-control'}),
            'type_of_incubatee'		    : forms.Select(choices=INCUBATEE,attrs={'class':'form-control'}),
            'women_led_startup'		    : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'gov_program'				: forms.Select(choices=GOVERNMENT,attrs={'class':'form-control'}),
            'msme_registered'		    : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'dspp_registered'		    : forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'legal_entity_register'		: forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'start_date_incubation'		: forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'startup_img'				: forms.FileInput(),
            'founder_img'				: forms.FileInput(),	
        }


class MonitorSheetEditForm(forms.ModelForm):

            
    class Meta:
        model = MonitorSheetReport
        exclude = ['connect_startup','allow_edit']
        fields = ('__all__')

        widgets = {

            'ips_till_date'					        : forms.TextInput(attrs={'class':'form-control'}),
            'recognisation_till_date'				: forms.TextInput(attrs={'class':'form-control'}),
            'funds_till_date' 					    : forms.TextInput(attrs={'class':'form-control'}),
            'jobs_created_till_date' 				: forms.TextInput(attrs={'class':'form-control'}),
            'sales_till_date' 						: forms.TextInput(attrs={'class':'form-control'}),
            'revenew_till_date'						: forms.TextInput(attrs={'class':'form-control'}),
            'expendicture_till_date'				: forms.TextInput(attrs={'class':'form-control'}),
            
            'ips_last_month'				        : forms.TextInput(attrs={'class':'form-control'}),
            'recognisation_last_month'				: forms.TextInput(attrs={'class':'form-control'}),
            'funds_last_month'					    : forms.TextInput(attrs={'class':'form-control'}),
            'jobs_created_last_month'				: forms.TextInput(attrs={'class':'form-control'}),
            'sales_last_month'					    : forms.TextInput(attrs={'class':'form-control'}),
            'revenew_last_month'			        : forms.TextInput(attrs={'class':'form-control'}),
            'expendicture_last_month'		        : forms.TextInput(attrs={'class':'form-control'}),
            
            'problems'  		                    : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'oppertunities'                         : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'out_reach'                             : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'partnership_mou'                       : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'intervention'				            : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            
            'monitor_meeting'			            : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'action_plan'                           : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'help_required'                         : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
             
        }


# class TractionSheetEditForm(forms.ModelForm):

            
#     class Meta:
#         model = TractionSheet
#         exclude = ['connect_startup','allow_edit']
#         fields = ('__all__')

#         widgets = {
#             'total_order'                       : forms.TextInput(attrs={'class':'form-control'}),
#             'average_packet_size'			    : forms.TextInput(attrs={'class':'form-control'}),
#             'total_revenue_of_month'			: forms.TextInput(attrs={'class':'form-control'}),
#             'total_customers_served'	        : forms.TextInput(attrs={'class':'form-control'}),
#             'total_expense'					    : forms.TextInput(attrs={'class':'form-control'}),
#             'market_outreach'					: forms.TextInput(attrs={'class':'form-control'}),
#             'repeate_customers'					: forms.TextInput(attrs={'class':'form-control'}),
#             'total_revenue'			            : forms.TextInput(attrs={'class':'form-control'}),
#             'direct_job_created'				: forms.TextInput(attrs={'class':'form-control'}),
#             'indirect_job_created'				: forms.TextInput(attrs={'class':'form-control'}),
#             'profit'                            : forms.TextInput(attrs={'class':'form-control'}),
#         }


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        exclude = ['date_of_creation']
        fields = ('__all__')


        widgets = {
            'title'                         : forms.TextInput(attrs={'class':'form-control'}),
            'description'			        : forms.Textarea(attrs={'class':'form-control','rows':"3"}),
            'blog_img'			            : forms.FileInput(attrs={'class':'form-control'}),
        }