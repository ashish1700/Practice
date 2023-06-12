from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,LoginForm

# Create your views here.

@login_required(login_url='login')

def HomePage(request):
    return render (request,'home.html')


# def SignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')
       
#         if pass1!=pass2:
#             return HttpResponse("your password and confirm password are not same")

#         else:
#             my_user=User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')
        


#     return render(request, 'signup.html')

def SignupPage(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')

            if pass1 != pass2:
                return HttpResponse("Your password and confirm password are not the same.")
            else:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username  or password is incorrect")

    return render(request,'login.html')

# def LoginPage(request):
#     form = LoginForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             pass1 = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=pass1)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 return HttpResponse("Username or password is incorrect.")

#     context = {'form': form}
#     return render(request, 'login.html', context)
 
def LogoutPage(request):
    logout(request)
    return redirect('login')
