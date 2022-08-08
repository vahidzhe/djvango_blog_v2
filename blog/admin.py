from django.contrib import admin
from blog import models
from blog.models import KateqoriyaModel,MeqaleModel,SerhModel,ElaqeModel
# Register your models here.

admin.site.register(KateqoriyaModel)





class MeqaleAdmin(admin.ModelAdmin):
    search_fields = ('basliq','yazi')
    list_display = (
        'basliq',
        # 'kateqoriya',
        'yazar',
        'slug',
        'yaranma_tarixi',
        'redakte_tarixi'
    )
admin.site.register(MeqaleModel,MeqaleAdmin)


class SerhAdmin(admin.ModelAdmin):
    search_fields = ('yazar__username',)

    list_display = ('yazar','yaranma_tarixi','redakte_tarixi'
    )
admin.site.register(SerhModel,SerhAdmin)


class ElaqeAdmin(admin.ModelAdmin):
    search_fields = ('ad_soyad','email')

    list_display = ('ad_soyad','email','yaranma_tarixi'
    )
admin.site.register(ElaqeModel,ElaqeAdmin)