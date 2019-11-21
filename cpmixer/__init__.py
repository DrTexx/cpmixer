#!/usr/bin/env python -e

"""
DOCSTRING IS HERE
"""

from platform import system
user_platform = system()

if user_platform == "Windows":

    from .windows import Mixer

elif user_platform == "Darwin":

    from .darwin import Mixer

elif user_platform == "Linux":

    from .linux import Mixer

else:

    raise Exception("Sorry, your platform isn't supported yet by cpmixer ({})".format(user_platform))

# create common aliases for them all regardless of platform
    # tool 1
    # tool 2
    # tool 3
    # etc.
