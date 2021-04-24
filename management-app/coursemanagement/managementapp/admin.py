from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy

from .models import User, Syllabus, UserRegistration

# Register your models here.
class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = UserRegistration
        fields = ('email',)


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (ugettext_lazy('Personal info'), {'fields': ('first_name', 'last_name')}),
        (ugettext_lazy('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (ugettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(UserRegistration, MyUserAdmin)

admin.site.register(User)
admin.site.register(Syllabus)