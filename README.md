# opensouls-python
Python helpers for using opensoul's socialagi and soul-engine over JSPyBridge 

the main file which is also executable is
https://github.com/antont/opensouls-python/blob/main/soulengine_chat.py

installing the npm deps to the py-js bridge may require some doing still, one way is to *temporarily* comment out line 4 in soulengine.py:
soul_engine = javascript.require('soul-engine')

or maybe also just using npm to install it to system works. the bridge has also some ways to run package install commands for it, 

the rationale for those helpers is that creating complex objects, passing callbacks etc. was not so easy / possible over the bridge, so i added things in js to make the bridging simpler.

if interested, please be in touch here or in the opensouls discord, i'm open for continuing with this to have a well developed lib later on. although optimally it does not need almost anything, as the bridge should work for this. i first tried to use their @on thing for registering JS event handlers from Python, but had some probs, so resorted to this. their docs are at https://github.com/extremeheat/JSPyBridge/blob/master/docs/python.md

might be a good idea to report things to the bridge project, maybe they could help or improve things.
