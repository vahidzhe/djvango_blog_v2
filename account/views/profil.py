from account.models import CustomUserModel
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

class ProfilDetailView(DetailView):
    template_name = 'pages/profil.html'
    context_object_name = 'profil'
    model = CustomUserModel

    def get_object(self):
        user = get_object_or_404(CustomUserModel,username = self.kwargs.get('username'))
        return user
        