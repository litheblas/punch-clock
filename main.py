from __future__ import absolute_import, unicode_literals
import logging
import signal
import sys

from clock import io, lib

logging.basicConfig(level=logging.INFO, format='[%(asctime)s / %(name)s / %(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


def run():
    logger.info('Starting.')
    io.setup()
    logger.debug('GPIO set up.')

    while True:
        lib.sleep_until_next_minute()
        lib.pulse()


def signal_handler(signal, frame):
    logger.info('Caught signal {}. Shutting down.'.format(signal))
    io.cleanup()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    run()
