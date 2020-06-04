from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.helper import FormHelper

class CustomUserCreationForm(UserCreationForm):

    helper = FormHelper()

    helper.layout = Layout(
    Fieldset('password1', type="hidden"))
    

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


