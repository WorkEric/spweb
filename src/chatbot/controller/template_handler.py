# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""handler file for the template module"""


from ..models import TemplateCategory, TemplateContent


def get_template_info():
    """get all template page information

    template category
    template content
    user information if user login
    """
    categories = TemplateCategory.objects.all()
    contents = TemplateContent.objects.all()
    # test = TemplateCategory(name='test')
    # test.full_clean()
    # test.save()
    return categories, contents
