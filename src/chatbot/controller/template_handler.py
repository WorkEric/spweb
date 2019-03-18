# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""handler file for the template module"""


from ..models import TemplateCategory, TemplateContent


def get_template_info():
    """get all template page information

    template category
    template content
    user information if user login

    Ex: before save do validation on the model
    test = TemplateCategory(name='ddd', data_type='education')
    test.full_clean()
    test.save()
    """
    categories = TemplateCategory.objects.all().order_by('created_at')
    contents = TemplateContent.objects.all()
    return categories, contents
