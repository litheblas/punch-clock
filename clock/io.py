from __future__ import absolute_import, unicode_literals
import logging

import RPi.GPIO as GPIO

from . import settings

logger = logging.getLogger(__name__)


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(settings.CLOCK_GPIO_PIN, GPIO.OUT, initial=GPIO.LOW)


def pull():
    GPIO.output(settings.CLOCK_GPIO_PIN, GPIO.HIGH)


def release():
    GPIO.output(settings.CLOCK_GPIO_PIN, GPIO.LOW)


def cleanup():
    release()
    GPIO.cleanup()
