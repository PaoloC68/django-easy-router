# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

class ModelDatabaseRouter(object):
    """
    Allows each model to set its own destiny
    Usage:

    Add recognized model option to django
    import django.db.models.options as options
    options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('in_db',)


    """

    def db_for_read(self, model, **hints):
        """
        Specify target database with field in_db in model's Meta class
        :param model:
        :param hints:
        :return:
        """
        if hasattr(model._meta, 'in_db'):
            return model._meta.in_db
        return None

    def db_for_write(self, model, **hints):
        """
        Specify target database with field in_db in model's Meta class
        :param model:
        :param hints:
        :return:
        """
        if hasattr(model._meta, 'in_db'):
            return model._meta.in_db
        return None

    def allow_syncdb(self, db, model):
        """
        Specify target database with field in_db in model's Meta class
        :param db:
        :param model:
        :return:
        """
        if hasattr(model._meta, 'in_db'):
            if model._meta.in_db == db:
                return True
            else:
                return False
        else:
            # Random models that don't specify a database can only go to 'default'
            if db == 'default':
                return True
            else:
                return False

    def allow_relation(self, obj1, obj2, **hints):
        """
        Specify target database with field in_db in model's Meta class
        We allow relationships only within the same db
        :param obj1:
        :param obj2:
        :param hints:
        :return:
        """
        if hasattr(obj1.model._meta, 'in_db'):
            obj1_db = obj1.model._meta.in_db
        else:
            obj1_db = None

        if hasattr(obj2.model._meta, 'in_db'):
            obj2_db = obj2.model._meta.in_db
        else:
            obj2_db = None
        return obj1_db == obj2_db
