# -*- coding: utf-8 -*-
from django import template


register = template.Library()


@register.filter
def stars(value, max=5):
    the_list = []
    for i in range(value):
        the_list.append('★')
    for i in range(max - value):
        the_list.append('☆')
    return the_list
