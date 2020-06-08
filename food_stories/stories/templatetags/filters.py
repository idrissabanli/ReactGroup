from django.template import Library

register = Library()


# s = 'salam necesen?'
# s.split(' ') => ['salam', 'necesen?']

@register.filter
def split_tag(s, split_char):
    return s.split(split_char)
