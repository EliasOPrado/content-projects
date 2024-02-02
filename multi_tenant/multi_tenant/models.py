from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=255)
    subdomain = models.CharField(max_length=255)
    color = models.CharField(max_length=10)

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta: 
        abstract=True
    

class Member(TenantAwareModel):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    