from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import widgets, ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, Field

from .models import AlumniSmansaUser


class AlumniSmansaUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
        
        
class AlumniSmansaUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

class AlumniSmansaUserCreationForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Entry Data User',
            'username',
            'mobile_number',
            Field('address', css_class='form-group col-md-6 mb-0'),
            'password',
            ),
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = AlumniSmansaUser
        fields = ('username', 'mobile_number', 'address', 'password')

class AlumniSmansaUserCreateForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))

    def clean_username(self):
        data = self.cleaned_data['username']
        
        # Remember to always return the cleaned data.
        return data

    def clean_mobile_number(self):
        data = self.cleaned_data['mobile_number']
        
        # Remember to always return the cleaned data.
        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        
        # Remember to always return the cleaned data.
        return data

    def clean_bio(self):
        data = self.cleaned_data['bio']
        
        # Remember to always return the cleaned data.
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Entry Data User',
            'username',
            'mobile_number',
            Field('address', css_class='form-group col-md-6 mb-0'),
            Field('bio', css_class='form-group col-md-6 mb-0'),
            'password',
            ),
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = AlumniSmansaUser
        fields = ('username', 'mobile_number', 'address', 'bio', 'password')

class AlumniSmansaUserChangeForm(UserChangeForm):
    class Meta:
        model = AlumniSmansaUser
        fields = ('username', 'mobile_number', 'address', 'bio')

class AlumniSmansaUserVerifyForm(ModelForm):
    CHOICES = [('1', 'Blogger'), ('2', 'Admin')]
    user_mode = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial = '1')

    def clean_user_mode(self):
        data = self.cleaned_data['user_mode']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Verify as member',
            'user_mode',
            ),
            Submit('submit', 'Verify')
        )

    class Meta:
        model = AlumniSmansaUser
        fields = ('user_mode',)

class AlumniSmansaUserForm(forms.Form):
    pass

class AlumniSmansaUserUpdateForm(ModelForm):
    CHOICES = [('1', 'Blogger'), ('2', 'Admin')]
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    user_mode = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, initial = '1')

    def clean_mobile_number(self):
        data = self.cleaned_data['mobile_number']
        
        # Remember to always return the cleaned data.
        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        
        # Remember to always return the cleaned data.
        return data

    def clean_bio(self):
        data = self.cleaned_data['bio']
        
        # Remember to always return the cleaned data.
        return data

    def password_number(self):
        data = self.cleaned_data['password']
        
        # Remember to always return the cleaned data.
        return data

    def clean_user_mode(self):
        data = self.cleaned_data['user_mode']
        
        # Remember to always return the cleaned data.
        return data

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        if self.user.is_superuser:
            self.helper.layout = Layout(
                Fieldset('Update as member',
                'mobile_number',
                Field('address', css_class='form-group col-md-6 mb-0'),
                Field('bio', css_class='form-group col-md-6 mb-0'),
                'password',
                'user_mode',
                ),
                Submit('submit', 'Update')
            )
        else:
            self.helper.layout = Layout(
                Fieldset('Update as member',
                'mobile_number',
                Field('address', css_class='form-group col-md-6 mb-0'),
                Field('bio', css_class='form-group col-md-6 mb-0'),
                'password',
                ),
                Submit('submit', 'Update')
            )

    class Meta:
        model = AlumniSmansaUser
        fields = ('mobile_number', 'address', 'bio', 'user_mode', 'password')

class AlumniSmansaUserAdminForm(forms.Form):
    pass
