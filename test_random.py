import random
from errbot.backends.test import testbot
from errbot import plugin_manager

class TestRandom(object):
    extra_plugin_dir = '.'

    def test_coinflip(self, testbot):
        testbot.push_message('!coinflip')
        result = testbot.pop_message()
        assert(result == 'HEADS!' or result == 'TAILS!')

    #def test_roll(self, testbot):
        #TODO 

    def test_wheel(self, testbot):
        testbot.push_message('!wheel')
        result = testbot.pop_message()
        assert(result == 'Yes' or result == 'No')
