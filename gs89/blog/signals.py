from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("-----------------------------")
    print("Log-out Signal... Run Outro..")
    print("Sender:",sender)
    print("Request",request)
    print("User:",user)
    print("User Password:",user.password)
    print(f'kwargs:{kwargs}')

# user_logged_in.connect(login_success,sender=User)


@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("-----------------------------")
    print("Login Failed Signal...")
    print("Sender:",sender)
    print("Request",request)
    print("User:",user)
    print("User Password:",user.password)
    print(f'kwargs:{kwargs}')

# user_logged_out.connect(log_out,sender=User)


@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("-----------------------------")
    print("Login Failed Signal...")
    print("Sender:",sender)
    print("Request",request)
    print("Credentials",credentials)
    print(f'kwargs:{kwargs}')

# user_login_failed.connect(login_failed)