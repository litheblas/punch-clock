from __future__ import absolute_import, unicode_literals
import logging
from os import environ

logger = logging.getLogger(__name__)


CLOCK_GPIO_PIN = int(environ['CLOCK_GPIO_PIN'])
PULSE_DURATION = float(environ['CLOCK_PULSE_DURATION'])
