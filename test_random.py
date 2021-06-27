import random
from errbot.backends.test import testbot
from errbot import plugin_manager


class TestRandom(object):
    extra_plugin_dir = '.'

    def test_coinflip(self, testbot):
        testbot.push_message('!coinflip')
        result = testbot.pop_message()
        assert(result == 'HEADS!' or result == 'TAILS!')

    def test_roll(self, testbot):
        testbot.push_message('!roll')
        testbot.pop_message() # discard roll's start message
        result = testbot.pop_message().partition('... ')[2].partition('!')[0]
        assert(result == '1' or result == '2' or result == '3' or \
               result == '4' or result == '5' or result == '6')

    def test_wheel(self, testbot):
        testbot.push_message('!wheel')
        result = testbot.pop_message()
        assert(result == 'Yes' or result == 'No')
