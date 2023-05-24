from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'نام خود را وارد کنید'}), required=True)
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder': 'ایمیل خود را وارد کنید'}) ,required=True)
    text = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'متن پیام را وارد کنید' }), required=True)