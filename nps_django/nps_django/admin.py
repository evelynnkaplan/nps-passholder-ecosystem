from django.contrib import admin

from .models import Pass, Passholder, Park, Visit

class PassholderAdmin(admin.ModelAdmin):
  search_fields = ['first_name', 'last_name']
  list_display = ['first_name', 'last_name', 'passes']

class PassAdmin(admin.ModelAdmin):
  autocomplete_fields = ['passholder_primary']
  list_display = ['passholder_primary', 'zip_code', 'type', 'valid']
  list_filter = ['type']
  search_fields = ['passholder_primary__first_name', 'passholder_primary__last_name']

  def get_fields(self, request, obj=None):
    if obj is None or (obj.type != 'Standard' and obj.type != 'Military'):
      return ['passholder_primary', 'type', 'expiration_date', 'zip_code', 'email', 'phone_num', 'cost']
    elif obj.type == 'Standard' or obj.type == 'Military':
      return ['passholder_primary', 'passholder_secondary', 'type', 'expiration_date', 'zip_code', 'email', 'phone_num', 'cost']

class ParkAdmin(admin.ModelAdmin):
  search_fields = ['name']
  list_filter = ['state']

class VisitAdmin(admin.ModelAdmin):
  autocomplete_fields = ['passholder', 'park']
  list_filter = ['park', 'park__state', 'date']


admin.site.register(Pass, PassAdmin)
admin.site.register(Passholder, PassholderAdmin)
admin.site.register(Park, ParkAdmin)
admin.site.register(Visit, VisitAdmin)