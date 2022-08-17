from atexit import register
from django import template
from blog.models import KateqoriyaModel

register = template.Library()


@register.simple_tag
def kateqoriya_list():
    kateqoriyalar = KateqoriyaModel.objects.all()
    return kateqoriyalar
    