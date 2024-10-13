from django import template

register = template.Library()

# Allows for UI to be different depending on user group
@register.filter
def in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()