from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import Contract
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = [
            "full_name",
            "email",
            "phone_number",
            "address",
            "project_name",
            "company_name",
            "description",
            "project_length",
            "contingencies",
            "price",
            "payment_schedule",
            "permits",
        ]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username':UsernameField}