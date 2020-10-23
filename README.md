random-errbot
=============

## Overview
An [Errbot](https://github.com/errbotio/errbot) plugin for coin flips, die rolls and other randomization tasks.

## Requirements
No external libraries besides `errbot` itself is required.

## Installation
Errbot admins can install this plugin for an Errbot using the `!repos install` command:
  - `!repos install https://github.com/torgeirl/random-errbot.git`

Run `!help Plugins` to get instructions on `!repo uninstall`, `!repo update` and other plugin commands.

## Usage
```
$ !coinflip
TAILS!

$ !roll
Rolled a 6-sided dice, and the result is...
... 4!

$ !roll 2d20
Rolled 2 20-sided dice, and the result is...
... 1 19!

$ !wheel
Yes

$ !wheel Cat Dog
Dog
```

## License
See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).
