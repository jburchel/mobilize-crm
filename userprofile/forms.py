from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_image', 'email_signature',]
        widgets = {
            'profile_image': forms.FileInput(attrs={'accept': 'image/*'}),
            'email_signature': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_image = forms.ImageField(required=False)
    email_signature = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}),
                                      required=False,
                                      help_text="Enter your email signature. Line breaks will be preserved.")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "profile_image", "email_signature")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.email_signature = self.cleaned_data["email_signature"]
        if commit:
            user.save()
        return user