# from django import forms 
# from first_app.models import crud_student



# class stform(forms.ModelForm):
#     class Meta:
#         model = crud_student
#         fields = "__all__"
from django import forms
from first_app.models import Product
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    password =forms.CharField(max_length=20, widget=forms.PasswordInput)
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

