from django import template
from flower.models import Category

register = template.Library()


@register.inclusion_tag('flower/drop_down.html')
def show_drop_down_menu(drop_down_list='drop_down_menu'):
    categories = Category.objects.all()
    return {"categories": categories, "drop_down_list": drop_down_list}
