# -*- coding: utf-8 -*-

import warnings

from . import models


from .models import *  # noqa, isort:skip


warnings.warn(
    "djstripe.stripe_objects is a deprecated module, please use djstripe.models",
    DeprecationWarning
)

StripeCharge = Charge
StripeCustomer = Customer
StripeEvent = Event
StripePayout = Payout
StripeCard = Card
StripeCoupon = Coupon
StripeInvoice = Invoice
StripePlan = Plan
StripeSubscription = Subscription
StripeAccount = Account
StripeTransfer = Transfer
