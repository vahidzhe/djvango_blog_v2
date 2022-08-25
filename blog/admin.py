from django.contrib import admin
from blog import models
from blog.models import KateqoriyaModel, MeqaleModel, SerhModel, ElaqeModel
# Register your models here.

admin.site.register(KateqoriyaModel)


@admin.register(MeqaleModel)
class MeqaleAdmin(admin.ModelAdmin):
    search_fields = ('basliq', 'yazi')
    list_display = (
        'basliq',
        # 'kateqoriya',
        'yazar',
        'slug',
        'yaranma_tarixi',
        'redakte_tarixi'
    )

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
        
    #     if request.user.is_superuser:
    #         return qs  

    #     if request.user.get_group_permissions():
            
    #         return qs.filter(yazar=request.user) 


@admin.register(SerhModel)
class SerhAdmin(admin.ModelAdmin):
    search_fields = ('yazar__username',)

    list_display = ('yazar', 'yaranma_tarixi', 'redakte_tarixi'
                    )


@admin.register(ElaqeModel)
class ElaqeAdmin(admin.ModelAdmin):
    search_fields = ('ad_soyad', 'email')

    list_display = ('ad_soyad', 'email', 'yaranma_tarixi'
                    )
