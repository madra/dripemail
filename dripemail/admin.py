'''admin configurations'''
from django.contrib import admin
from django.contrib.auth.models import *
# remove registration
from .models import Dripbox


class DripboxAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else True


admin.site.register(Dripbox, DripboxAdmin)
