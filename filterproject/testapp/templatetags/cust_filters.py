from django import template
register=template.Library()

@register.filter(name='ffu')
def first_five_upper(value):
    result=value[:5].upper()
    return result
#only 5 charcters with uppercase it will return
# register.filter('first_five_upper',first_five_upper)
# register.filter('ffu',first_five_upper)


def first_n_upper(value,n):
    result=value[:n].upper()
    return result

register.filter('fnu',first_n_upper)


def first_m_n_upper(value,s):
    numbers=s.split(',')
    result=value[int(numbers[0]):int(numbers[1])].upper()
    return result
#here we can't send multiple arguments at 1 time
register.filter('fmn',first_m_n_upper)