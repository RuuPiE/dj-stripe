"""
.. module:: djstripe.

  :synopsis: dj-stripe - Django + Stripe Made Easy
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import pkg_resources

from . import checks  # noqa: Register the checks

try:
    __version__ = pkg_resources.require("dj-stripe")[0].version
except pkg_resources.DistributionNotFound:
    __version__ = 'no-dist'
