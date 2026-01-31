from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username, password)
        u=authenticate(username=username, password=password)
        print(u)
        if u:
            login(request,u)
            return redirect('home')
        else:
            return render(request, 'login_.html', {'status': True})
    return render(request, 'login_.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        print(first_name,last_name,email,username,password, confirm_password)

        if password!=confirm_password:
            return render(request, 'register.html', {'error1': True})
        
        try:
            u=User.objects.get(username=username)
            return render(request, 'register.html', {'status':True})
        except:
            u=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
        )
        u.set_password(password)
        u.save()
        return redirect('login_')
    return render(request, 'register.html')
@login_required(login_url='login_')
def logout_(request):
    logout(request)
    return redirect('login_')
@login_required(login_url='login_')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login_')
def update_profile(request, pk):
    old_data=User.objects.get(id=pk)
    if request.method == 'POST':
        old_data.first_name=request.POST['first_name']
        old_data.last_name=request.POST['last_name']
        old_data.email=request.POST['email']
        old_data.username=request.POST['username']
        old_data.save()
        return redirect('profile')
    return render(request, 'update_profile.html', {'old_data':old_data})

@login_required(login_url='login_')
def reset_password(request):
    u=User.objects.get(username=request.user)
    if request.method == 'POST':
        try:
            old_data=request.POST['old_pass']
            verified=authenticate(username=u.username,password=old_data)
            if verified:
                return render(request, 'reset_password.html', {'verified':True})
            else:
                return render(request, 'reset_password.html', {'not_verified':True})
        except:
            new_pass=request.POST['new_pass']
            u.set_password(new_pass)
            u.save()
            return redirect('login_')
    return render(request, 'reset_password.html')