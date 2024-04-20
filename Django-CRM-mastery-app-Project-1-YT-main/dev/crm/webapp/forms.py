from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

class CreateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


# - Update a record

class UpdateRecordForm(forms.ModelForm):

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
# forms.py



# forms.py
from django import forms
from .models import Interaction


from django import forms
from .models import Interaction, Customer

from django import forms
from .models import Interaction, Customer

from django import forms
from .models import Interaction

class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['customer', 'interaction_type', 'date_time', 'notes']
        widgets = {
            'customer': forms.TextInput(attrs={'placeholder': 'Enter customer name'}),
        }

    def clean_customer(self):
        customer_name = self.cleaned_data.get('customer')
        if not customer_name:
            return customer_name  # If customer name is empty, return it as is
        return customer_name.strip()  # Strip any leading or trailing whitespace from the customer name
