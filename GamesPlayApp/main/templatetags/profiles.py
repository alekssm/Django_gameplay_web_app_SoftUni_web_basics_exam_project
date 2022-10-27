from django import template


from GamesPlayApp.main.models import Profile


register = template.Library()


@register.simple_tag()
def is_profile():
    return Profile.objects.count() > 0
