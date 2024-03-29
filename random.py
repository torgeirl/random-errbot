import logging
from random import choice, randint
from re import match as re_match
from shlex import split as shlex_split
from time import sleep

from errbot import BotPlugin, botcmd

logger = logging.getLogger(__name__)


class Random(BotPlugin):
    '''Plugin for coin flips, die rolls and other randomization tasks.'''

    @botcmd
    def coinflip(self, msg, args):
        '''Need to toss a coin in these cash-free times? Look no further.'''
        logger.info('Flipping coin for {}'.format(msg.frm))
        return choice(['HEADS!', 'TAILS!'])

    @botcmd
    def eightball(self, msg, args):
        '''Fortune telling at your fingertips.'''
        logger.info('Magic 8 ball got shook by {}'.format(msg.frm))
        answers = ['It is certain.', 'It is decidedly so.',
                   'Without a doubt.', 'Yes definitely.',
                   'You may rely on it.', 'As I see it, yes.',
                   'Most likely.', 'Outlook good.',
                   'Yes.', 'Signs point to yes.',
                   'Reply hazy, try again.', 'Ask again later.',
                   'Better not tell you now.', 'Cannot predict now.',
                   'Concentrate and ask again.', 'Don\'t count on it.',
                   'My reply is no.', 'My sources say no.',
                   'Outlook not so good.', 'Very doubtful.']
        return choice(answers)

    @botcmd
    def roll(self, msg, args):
        '''Rolls one or more dice with N sides; defaults to 1D6.'''
        match = re_match(r'(?:(?P<number>\d+)d)?(?P<sides>\d+)?$', args)
        if not match:
            yield 'Please supply a valid number sufficient for rolling.'
            return
        number = int(match.group('number') or 1)  # default to 1 die rolled
        sides = int(match.group('sides') or 6)  # default to 6 sides
        if not 1 < sides <= 10**6:
            yield 'Please supply a valid number of sides.'
            return
        elif not 0 < number <= 100:
            yield 'Please supply a valid number of dice.'
            return
        logger.info('Rolling {}D{} for {}'.format(number, sides, msg.frm))
        results = [str(randint(1, sides)) for _ in range(number)]
        roll_msg = 'Rolled {} {}-sided dice, and the result is...'
        yield roll_msg.format(number if number > 1 else 'a', sides)
        sleep(1)  # TODO is there a 'send_user_typing_pause()' equivalent for Errbot?
        yield '... {}!'.format(' '.join(results))

    @botcmd
    def wheel(self, msg, args):
        '''Spin the wheel decider; defaults to Y/N.'''
        options = shlex_split(args)
        logger.info('Running wheel decider for {}'.format(msg.frm))
        return choice(['Yes', 'No']) if len(options) == 0 else choice(options)
