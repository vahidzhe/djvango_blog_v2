from account.models import CustomUserModel
from django.contrib.auth.forms import UserChangeForm

class ProfilRedakteForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUserModel
        fields = ('email','first_name','last_name','avatar')