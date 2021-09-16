from schedule.form import CreateUserAdminForm, changeUserAdminForm
from django.contrib import admin
from schedule import models
# Register your models here.

admin.site.register(models.Schedule)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    add_form = CreateUserAdminForm
    change_form = changeUserAdminForm
    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super(UserAdmin, self).get_form(request, obj, **kwargs)

