from  django.contrib.auth import get_user_model
from  django.contrib.auth.forms import UserCreationForm, UserChangeForm

class AlumniSmansaUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
        
        
class AlumniSmansaUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
