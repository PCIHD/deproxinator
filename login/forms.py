from django import forms
from login.models import UserProfileInfo,AdminRegistrationModel
from django.contrib.auth.models import User
#import user model for userprofileinfo by PCIHD
division_choices = [('division','Select'),('cse1','Cse1'),('cse2','Cse2'),('cse3','Cse3'),('cse4','Cse4')]
batch_choices = [('division','Select'),('A','A'),('B','B'),('C','C')]

class UserForm(forms.ModelForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter your E-mail Id','onblur=this.placeholder':'Enter your first name','onfocus=this.placeholder':''}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Create a Password','onblur=this.placeholder':'Enter your first name','onfocus=this.placeholder':''}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'input-container','placeholder':'Enter your first name','onblur=this.placeholder':'Enter your first name','onfocus=this.placeholder':''}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your last name','onblur=this.placeholder':'Enter your first name','onfocus=this.placeholder':''}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Create an username','onblur=this.placeholder':'Enter your first name','onfocus=this.placeholder':''}))




    class Meta():
            model = User
            fields = ('first_name','last_name','username','email','password')

        #    username = forms.CharField(help_text='none')
            help_texts = {
                    'username': None
                    }

class UserProfileInfoForm(forms.ModelForm):

    division=forms.CharField(widget=forms.Select(choices = division_choices ,attrs={'input': 'text'}))
    batch=forms.CharField(widget=forms.Select(choices = batch_choices ,attrs={'input': 'text'}))
    division.widget.attrs.update({'class': 'special'})
    batch.widget.attrs.update({'class': 'special1'})
    rollnumber=forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Enter your Roll Number','onblur=this.placeholder':'Enter your first name','onfocus=this.placeholder':''}))
    class Meta():
        model = UserProfileInfo
        fields = ('rollnumber','division','batch','profile_pic')



class Adminloggedinform(forms.ModelForm):
    genkey = forms.CharField(max_length= 5)

class AdminRegistrationForm(forms.ModelForm):
        phone=forms.CharField(max_length=10,widget=forms.NumberInput(attrs={'class': 'special2','placeholder':'Enter your Mobile Number','onblur=this.placeholder':'Enter your Mobile Number','onfocus=this.placeholder':''}))
        id_no=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'special3','placeholder':'Enter your Id Number','onblur=this.placeholder':'Enter your Mobile Number','onfocus=this.placeholder':''}))
        id_no.widget.attrs.update({'class': 'special3'})
        class Meta():
            model = AdminRegistrationModel
            fields = ('phone','id_no','profile_pic')
