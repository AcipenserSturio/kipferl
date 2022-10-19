# kipferl

A basic roguelike game written in Python and curses.

# Setup

## Prerequisits

* Python 3.10 or above

* a terminal emulator with 8-bit colour support

  * cmd.exe, Powershell, Konsole, and GNOME Terminal are officially supported and tested.

  * If you use other terminal emulators, however, they are still highly likely to work.

  * IDLE is not a terminal emulator, and trying to run the game in IDLE will raise an error.

## Installation

* Run `python -m pip install -r requirements.txt` to install dependencies.

  * On Linux, you may remove `windows-curses` from `requirements.txt`, since it is only needed for a Windows installation.

* Run `python main.py` to launch the game.

  * On Windows, you may double-click `start_on_windows` instead, for convenience.

# License

This repository is a fork of `fpl-programming/programming-2022-20fpl`, which is licensed under MIT.

However, this fork only acts as a mirror for development being done in `AcipenserSturio/kipferl`, which uses none of the contents from `fpl-programming/programming-2022-20fpl`, and is entirely licensed under GPL-3.0 (as agreed upon by the contributors).

`AcipenserSturio/programming-2022-20fpl` is, therefore, licensed under GPL-3.0, while acknowledging the copyright notice of MIT.

By contributing to `AcipenserSturio/programming-2022-20fpl`, you agree to license your contributions under GPL-3.0, for future merge into `AcipenserSturio/kipferl`.

Note: since `AcipenserSturio/kipferl` uses none of the contents present in `fpl-programming/programming-2022-20fpl` prior to the fork, and any contributions made to this fork are also GPL-3.0, it does not need to honour the copyright notice that comes with the MIT license.
