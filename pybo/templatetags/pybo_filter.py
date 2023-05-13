from django import template

register = template.Library()


# 템플릿 필터 생성
@register.filter
def sub(value, arg):
    return value - arg
