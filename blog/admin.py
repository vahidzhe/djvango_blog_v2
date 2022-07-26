from django.contrib import admin
from blog.models import KateqoriyaModel,MeqaleModel
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
