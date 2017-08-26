from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig

__author__ = 'ruben'


class CoreAppConfig(AppConfig):
    name = 'djstripe'
    verbose_name = _('Stripe')
