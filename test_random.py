import logging

import random
from errbot.backends.test import testbot
from errbot import plugin_manager

logging.basicConfig(level=logging.WARNING)

class TestRandom(object):
    extra_plugin_dir = '.'

    def test_coinflip(self, testbot):
        testbot.push_message('!coinflip')
        result = testbot.pop_message()
        assert(result == 'HEADS!' or result == 'TAILS!')

    def test_roll(self, testbot):
        testbot.push_message('!roll 1d2')
        result = testbot.pop_message()
        assert(result == '1' or result == '2')

    def test_wheel(self, testbot):
        testbot.push_message('!wheel')
        result = testbot.pop_message()
        assert(result == 'Yes' or result == 'No')
