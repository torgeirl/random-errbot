from random import choice, randint
from re import match

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
    def roll(self, msg, args):
        '''Rolls one or more dice with N sides; defaults to 1D6.'''
        match = match(r'(?:(?P<number>\d+)d)?(?P<sides>\d+)?$', args)
        if not match:
            yield 'Please supply a valid number sufficient for rolling.'
            return

        number = int(match.group('number') or 1)  # default to 1 die rolled
        sides = int(match.group('sides') or 6)  # default to 6 sides
        logger.info('Rolling {}D{} for {}'.format(number, sides, msg.frm))

        if not 1 < sides <= 10**6:
            yield 'Please supply a valid number of sides.'
            return
        elif not 0 < number <= 100:
            yield 'Please supply a valid number of dice.'
            return

        results = [str(randint(1, sides)) for _ in range(number)]
        roll_msg = 'Rolled {} {}-sided dice, and the result is...'
        yield roll_msg.format(number if number > 1 else 'a', sides)
        sleep(1)  #TODO is there a 'send_user_typing_pause()' equivalent for Errbot?
        yield '... {}!'.format(' '.join(results))
