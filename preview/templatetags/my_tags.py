from django import template

register = template.Library()


# 自定义装饰器
@register.filter
def my_filter(v1, v2):
    return v1 * v2


# 自定义标签
@register.simple_tag
def my_tag(v1, v2, v3):
    return v1 * v2 * v3
