from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in,user_logged_out
# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want

    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='login/media/profile_pics',blank = True    )
    batch = models.CharField(max_length = 256, unique=False,default='None')
    division = models.CharField(max_length=256 ,unique = False,default='None')
    lecture = models.CharField(max_length=256,unique=False,default='None')
    lecturer = models.CharField(max_length=256,unique=False,default='None')
    rollnumber = models.CharField(max_length=10 ,default = '0')
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
'''
class AdminRegistration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Add any additional attributes you want

    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”


    id_no = models.CharField(max_length=20 ,default = '0')
    phone = models.CharField(max_length=10 ,default = '0')
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
'''
class LoggedUser(models.Model):
  username = models.CharField(max_length=30, primary_key=True)
  rollnumber=models.CharField(max_length=7 ,default='0')
  attendence = models.CharField(max_length=30, default = 'Absent')
  enteredkey=models.CharField(max_length=10,default = 'None')
  def __unicode__(self):
    return self.username
class AdminRegistrationModel(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    phone = models.CharField(max_length=10,default = '0')
    id_no = models.CharField(max_length=20,default = 'null')
    profile_pic = models.ImageField(upload_to='login/media/admin',blank = True)


class AdminKey(models.Model):
    refid = models.CharField(max_length=1,default = 'z')
    key = models.CharField(max_length=10,default = 'None')

def login_user(sender, request, user, **kwargs):
    if (user.is_superuser == False):
        name=user.first_name + ' ' + user.last_name
        u=User.objects.get(username = user.username)
        rollnumber=u.userprofileinfo.rollnumber
        print(rollnumber)
        LoggedUser(username=name,rollnumber=rollnumber).save()


def logout_user(sender, request, user, **kwargs):

  try:
    name=user.first_name + ' ' + user.last_name

    u = LoggedUser.objects.get(pk=name)
    u.delete()
  except LoggedUser.DoesNotExist:
    pass

user_logged_in.connect(login_user)
user_logged_out.connect(logout_user)
