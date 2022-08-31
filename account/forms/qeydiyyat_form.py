from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel

class QeydiyyatForm(UserCreationForm):

    class Meta:
        model = CustomUserModel
        fields = (
                'username',
                'last_name',
                'first_name',
                'email',
                'password1',
                'password2')