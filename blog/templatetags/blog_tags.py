from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def navactive(request, url):
    if url in request.path:
        return "active"
    return ""
