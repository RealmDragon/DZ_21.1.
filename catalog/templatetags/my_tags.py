from django import template

# переменная в которой используем Library
register = template.Library()


# описываем шаблонный фильтр в декораторе, в котором вызываем filter
@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return None
