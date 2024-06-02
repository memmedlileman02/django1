from django import forms
COUNTRY_CHOICES = (
    ('AZ', 'Azerbaijan'),
    ('US', 'United States'),
    ('GB', 'United Kingdom'),
    # Başqa ölkələri də əlavə edə bilerik
)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="İstifadəçi adı")
    soyad = forms.CharField(max_length=50, label="Soyad")
    finkod= forms.CharField(max_length=7)
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, label="Ölkə")
    password = forms.CharField(max_length=10, label="Şifrə", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=10, label="Şifrəni təsdiqlə", widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]
        finkod = self.cleaned_data["finkod"]
        
        
        if password and confirm and password !=confirm:
            raise forms.ValidationError("Şifrələr eyni deyil!!")
        
        if len(finkod) != 7:
            raise forms.ValidationError("Fin kodu 7 simvoldan ibarət olmalıdır!!")
        
        values = {
            "username": username,
            "password": password
        }
        
        return values
    
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="İstifadəçi adı")
    password = forms.CharField(max_length=10, label="Şifrə", widget=forms.PasswordInput)
    
    