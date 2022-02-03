from django import forms
from useraccounting.models import Ideanestchecking

class IdeanestEditForm(forms.ModelForm):

            
    class Meta:
        model = Ideanestchecking
        exclude = ['account']
        fields = ('__all__')
        CHOICES = [
            ('None','None'),
            ('Yes','Yes'),
            ('No','No'),
        ]

        INCUBATEE = [
            ('None','None'),
            ('Physical','Physical'),
            ('Virtual','Virtual'),
        ]

        INCUBATEELEBEL = [
            ('None','None'),
            ('Idation','Idation'),
            ('POC','POC'),
            ('Prototype','Prototype'),
            ('Minimum Vaiable Product','Minimum Viable Product'),
            ('Commercialized','Commercialized'),
        ]

        OPERATIONALMODEL = [
            ('None','None'),
            ('Product Manufacturing','Product Manufacturing'),
            ('Service Delivery','Service Delivery'),
            ('Aggregation Platform','Aggregation Platform'),
            ('Others','Others'),
        ]

        SECTOR = [
            ('Agriculture and Allied Fields','Agriculture and Allied Fields'),
            ('Electricity, New and Renewable energy and Environment sustainability','Electricity, New and Renewable energy and Environment sustainability'),
            ('Education','Education'),
            ('Health and Pharmaceuticals','Health and Pharmaceuticals'),
            ('Water Sanitation and Solid waste management','Water Sanitation and Solid waste management'),
            ('Service','Service'),
            ('Fintech','Fintech'),
            ('E-Commerce','E-Commerce'),
            ('Fintech','Fintech'),
            ('Others','Others'),
        ]

        GOVERNMENT = [
            ('None','None'),
            ('Women Empowerment ','Women Empowerment '),
            ('Make In India','Make In India'),
            ('Swachh Bharat ','Swachh Bharat '),
            ('Startup India','Startup India'),
            ('Beti Bachao Beti padhao','Beti Bachao Beti padhao'),
            
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