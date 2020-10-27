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
        testbot.push_message('!roll 1d2')
        assert('Rolled a 2-sided dice, and the result is...' \ 
               in testbot.pop_message())
        result = testbot.pop_message()
        assert(result == '1' or result == '2')

    def test_wheel(self, testbot):
        testbot.push_message('!wheel')
        result = testbot.pop_message()
        assert(result == 'Yes' or result == 'No')
