from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QBESavedQueriesConfig(AppConfig):
    name = 'django_qbe.savedqueries'
    verbose_name = _("Query by Example")
