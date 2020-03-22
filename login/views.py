from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.forms import UserForm,UserProfileInfoForm,AdminRegistrationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from . import models
from .models import LoggedUser
from django.contrib.auth.models import User
# Create your views here.
import  random,string
def key_generate():
    key = ''.join(random.choice(string.ascii_letters)for _ in range(5))
    return (key)


def user_login(request):
    if (request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)



                if request.user.is_superuser:
                    return HttpResponseRedirect(reverse('login:adminloggedin'))
                else:
                    return HttpResponseRedirect(reverse('login:loggedinuser'))
            else:

                return HttpResponse("Account not active")
        else:
                print("Someone tried to login and failed!")
                print("username:{} and password{}".format(username,password))
                return HttpResponse('Invalid Login Credentials. Please Try Again')
    else:
        return render(request,'login/login.html',{})

    return render(request,'login/login.html')
'''
def index(request):
    return render(request,'login/index.html')
'''
def register(request):
    registered = False
    if (request.method == "POST"):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        if (user_form.is_valid() and profile_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)


            user.save()


            profile = profile_form.save(commit = False)
            profile.user = user


            if ('profile_pic' in request.FILES):
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()


            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()



    return render(request,'login/registration.html',{'user_form':user_form,
                                                     'profile_form':profile_form,
                                                     'registered':registered})
#decorator condition to execute the function  below
@login_required
def user_logout( request):
    logout(request)



    return HttpResponseRedirect(reverse('login:index'))


class IndexView(TemplateView):
    #print("VERIFICATION: ")
    template_name = 'login/index.html'

class AdminLoggedView(TemplateView):




    template_name = 'login/adminloggedin.html'
    def get_context_data(self,**kwargs):
        key = key_generate()

        context = super().get_context_data(**kwargs)
        context['injectkey'] = key
        u = models.AdminKey.objects.get(pk = 1)
        u.key = key
        u.save()

        return context
    def post(self,request):
        if(request.method == 'POST'):
            return redirect('login:list_loggedinusers')







class UserLoggedView(TemplateView):
    #context_object_name = 'user_info'
    #model = models.LoggedUser
    template_name = 'login/userloggedin.html'
    def post(self,request):
        if(request.method=='POST'):
            #print("VERIFICATION: ", request.user.username)

            user=request.user
            name=user.first_name + ' ' + user.last_name



            userkey = request.POST.get('securekey')
            print(userkey)
            user_model = models.LoggedUser.objects.get(username=name)
            user_model.enteredkey = userkey
            user_model.save()
            print("userentered key",user_model.enteredkey)
            attendence(request)

            #models.LoggedUser(enteredkey=userkey).save()
            return render(request,self.template_name)


class LoggedinUsers(ListView):
        context_object_name = 'loggedinuserlist'





        template_name='login/Loggedinusers.html'
        model=models.LoggedUser
def attendence(request):

        user = request.user
        u = models.AdminKey.objects.get(pk = 1)



        name=user.first_name + ' ' + user.last_name
        user_model = models.LoggedUser.objects.get(username=name)
        if(u.key ==  user_model.enteredkey):
            user_model.attendence = "Present"
        user_model.save()
        print("in attendence" ,user_model.attendence)

        return request


def adminregister(request):
    registered = False
    if (request.method == "POST"):
        user_form = UserForm(data=request.POST)
        profile_form = AdminRegistrationForm(data = request.POST)
        if (user_form.is_valid() and profile_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.is_superuser = True

            user.save()


            profile = profile_form.save(commit = False)
            profile.user = user


            if ('profile_pic' in request.FILES):
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()


            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = AdminRegistrationForm()



    return render(request,'login/adminregistration.html',{'user_form':user_form,
                                                     'profile_form':profile_form,
                                                     'registered':registered})


        #returns loggedinuser_list
