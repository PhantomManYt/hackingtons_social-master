from django import template
register = template.Library()

from home.models import Post

@register.simple_tag
def search():