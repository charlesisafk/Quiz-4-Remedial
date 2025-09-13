from django import forms

from accounts.models import Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}))
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name
    def clean_bio(self):
        bio = self.cleaned_data['bio']
        return bio
    def clean_profile_picture(self):
        profile_picture = self.cleaned_data['profile_picture']
        return profile_picture
