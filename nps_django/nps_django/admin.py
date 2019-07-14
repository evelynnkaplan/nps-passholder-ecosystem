from django.contrib import admin

from .models import Pass, Passholder, Park, Visit

class PassholderAdmin(admin.ModelAdmin):
  search_fields = ['first_name', 'last_name']

class PassAdmin(admin.ModelAdmin):
  autocomplete_fields = ['passholder_primary']

  def get_fields(self, request, obj=None):
    if obj is None or (obj.type != 'Standard' and obj.type != 'Military'):
      return ['passholder_primary', 'type', 'expiration_date', 'zip_code', 'email', 'phone_num', 'cost']
    elif obj.type == 'Standard' or obj.type == 'Military':
      return ['passholder_primary', 'passholder_secondary', 'type', 'expiration_date', 'zip_code', 'email', 'phone_num', 'cost']


admin.site.register(Pass, PassAdmin)
admin.site.register(Passholder, PassholderAdmin)
admin.site.register(Park)
admin.site.register(Visit)