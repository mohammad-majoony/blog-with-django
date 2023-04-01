from django import template
from ..models import * 

register = template.Library()

# just a tes
@register.simple_tag
def title():
  return 'بلاگ'

@register.inclusion_tag('base/partials/category_nav.html')
def category_nav_menu():
  categorys = Category.objects.filter(status=True)
  context = {
    'categorys' : categorys,
  }
  return context