# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django.db import migrations
from django.db.migrations.operations.special import RunPython

from djstripe.sync import (
    resync_subscriptions,
    resync_invoiceitems,
    sync_charges,
    sync_invoices,
    sync_transfers,
    sync_customers
)


class Migration(migrations.Migration):
    dependencies = [
        ('djstripe', '0011_charge_captured_update'),
    ]

    operations = [
        RunPython(resync_subscriptions),
        RunPython(resync_invoiceitems),
        RunPython(sync_charges),
        RunPython(sync_invoices),
        RunPython(sync_transfers),
        RunPython(sync_customers),
    ]
