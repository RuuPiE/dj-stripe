# -*- coding: utf-8 -*-
"""
.. module:: djstripe.management.commands.djstripe_sync_customers.

   :synopsis: dj-stripe - sync_customer command.

.. moduleauthor:: @kavdev, @pydanny, @shvechikov

"""
from __future__ import absolute_import, division, print_function, unicode_literals

import logging

from django.core.management.base import BaseCommand

from djstripe import sync

log = logging.getLogger('resync_all')


class Command(BaseCommand):
    """Sync subscriber data with stripe."""

    help = "Sync subscriber data with stripe."

    def handle(self, *args, **options):
        """Call sync_subscriber on Subscribers without customers associated to them."""
        sync.resync_subscriptions()
        sync.resync_invoiceitems()
        sync.sync_charges()
        sync.sync_invoices()
        sync.sync_transfers()
        sync.sync_customers()


