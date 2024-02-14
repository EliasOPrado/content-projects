from django.shortcuts import render
from .models import Member
from .utils import get_tenant

# Create your views here.
def home(request):
    tenant = get_tenant(request)
    members = Member.objects.filter(tenant=tenant)
    context = {"tenant":tenant, "members":members}
    return render(request, 'home.html', context)