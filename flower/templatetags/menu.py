from django import template
from flower.models import Category

register = template.Library()


@register.inclusion_tag('flower/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()
    return {"categories": categories, "menu_class": menu_class}


@register.inclusion_tag('flower/drop_down_menu_search.html')
def show_menu_search(drop_down_list='menu'):
    categories = Category.objects.all()
    return {"categories": categories, "drop_down_list": drop_down_list}


@register.inclusion_tag('flower/footer_menu.html')
def show_footer_menu(footer_ul='menu'):
    categories = Category.objects.all()
    return {"categories": categories, "footer_ul": footer_ul}