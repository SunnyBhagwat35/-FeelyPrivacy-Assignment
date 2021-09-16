from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .decorators import onlyStaff
from schedule.form import appointment
from .models import Schedule
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect') 

    context = {}
    return render(request, 'login.html', context) 


def logoutUser(request):
    if request.user == 'AnonymousUser':
        user = ''
        messages.info(request, f'{user} Your account has been logged out!')
    else:
        user = request.user.username
        messages.info(request, f'{user}, Your account has been logged out!')

    logout(request)
    return redirect( 'login')


@login_required(login_url="login")
def home(request):
    sdata = Schedule.objects.all()
    if request.method == "POST":
        if request.user.is_emp:
            obj = Schedule.objects.get(id=request.POST.get('slot'))
            if not obj.booked:
                obj.booked = True
                obj.save()
                messages.info(request, 'Your appointment is booked.')
                return redirect('home')
            else:
                messages.info(request, 'Already booked.')
                

    data = {}
    for d in sdata:
        d.time.date()
        data[str(d.time.date())] = {'morning': [], 'afternoon': [], 'evening': []}

    for i in sdata:
        if i.time.hour < 12:
            data[str(i.time.date())]['morning'].append(i)
        elif i.time.hour < 18:
            data[str(i.time.date())]['afternoon'].append(i)
        else:
            data[str(i.time.date())]['evening'].append(i)


    context = {'data':data}
    # for k,v in data.items():
    #     print(k)
    return render(request, 'home.html', context)


@onlyStaff
def addApointment(request):
    form = appointment()
    if request.method == 'POST':
        form = appointment(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('addApointment')

    context = {'form':form}
    return render(request, 'addAppointment.html', context)
