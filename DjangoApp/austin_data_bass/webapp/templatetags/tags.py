from django import template

register = template.Library()

@register.simple_tag #Used to allow pagination to work with filters/queries
def url_replace(request, field, value):

    dict_ = request.GET.copy()

    dict_[field] = value

    return dict_.urlencode()