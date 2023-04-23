from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
   
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.info(request, 'Welcome {username}.')
                return redirect('shop:allProdCat')
            else:
                messages.info(request, 'Invalid Credential')
                return redirect('credentials:login')
    else:
        form = AuthenticationForm()
    # if request.method == 'POST':
    #     username = request.POST['user']
    #     passw = request.POST['pass']
    #     user = auth.authenticate(username=username,password=passw)
    #
    #     if user is not None:
    #         auth.login(request,user)
    #         return redirect('/')
    #     else:
    #         messages.info(request,'invalid username or password')
    #         return redirect('login')

    return render(request,'login.html',{'form':form})




def register(request):

    if  request.method=='POST':
        username=request.POST['Username']
        first_name = request.POST['First_name']
        last_name = request.POST['Last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']


        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)

                user.save()
                return redirect('login')

        else:
            messages.info(request,'password not match')
            return redirect('register')


    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')