import random
from errbot.backends.test import testbot
from errbot import plugin_manager

class TestRandom(object):
    extra_plugin_dir = '.'

    def test_coinflip(self, testbot):
        testbot.push_message('!coinflip')
        assertIn(testbot.pop_message(), ['HEADS!', 'TAILS!'])

    def test_roll(self, testbot):
        testbot.push_message('!roll')
        assertIn(testbot.pop_message(), ['1', '2', '3', '4', '5', '6'])

    def test_wheel(self, testbot):
        testbot.push_message('!wheel')
        assertIn(testbot.pop_message(), ['Yes', 'No'])
