from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.http.response import HttpResponse

def onlyStaff(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_manager or request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('chal nikal')

    return wrapper_func