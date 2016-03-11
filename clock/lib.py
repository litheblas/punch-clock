from __future__ import absolute_import, unicode_literals
import logging
from time import sleep
from datetime import datetime

from .settings import PULSE_DURATION
from .io import pull, release

logger = logging.getLogger(__name__)


def pulse():
    logger.debug('Pulsing at {}'.format(datetime.now().time()))
    pull()
    sleep(PULSE_DURATION)
    release()


def sleep_until_next_minute():
    """
    Sleeps until the time is xx:xx:00 with good enough accuracy (the error is
    usually in the order of 10-100 milliseconds).
    """
    now = datetime.now().time()
    sleep(60.0 - now.second - now.microsecond/1000000.0)
