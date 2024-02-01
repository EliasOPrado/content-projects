from .models import Tenant

def get_tenant(request):
    subdomain = request.get_host().split(':')[0].lower().split('.')[0]
    return Tenant.objects.filter(subdomain=subdomain).first()
