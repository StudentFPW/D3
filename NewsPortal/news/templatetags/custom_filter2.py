from django import template

register = template.Library()


@register.filter()
def post_time(date, format_string='%d/%b/%Y'):
    return date.utcnow().strftime(format_string)
