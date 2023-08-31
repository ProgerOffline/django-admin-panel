# -*- coding: utf-8 -*-

from accounts.models import UserAccount
from django.shortcuts import redirect, render


# Create your views here.
def index_view(request):
    if request.user.is_authenticated:
        return render(
            request=request,
            template_name='adminpanel/base.html',
        )
    return redirect('accounts:login')
