from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AlumniSmansaUserCreationForm, AlumniSmansaUserChangeForm

alumniSmansaUser = get_user_model()

class AlumniSmansaUserAdmin(UserAdmin):
    add_form = AlumniSmansaUserCreationForm
    form = AlumniSmansaUserChangeForm
    model = alumniSmansaUser
    list_display = ['email', 'username',]


admin.site.register(alumniSmansaUser, AlumniSmansaUserAdmin)

