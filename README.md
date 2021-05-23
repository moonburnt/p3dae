*Audio effects support for panda3d*

# p3dae

## Description:

**p3dae** is a library dedicated to implementation of various audio effects for
panda3d's AudioManager. Its started as attempt to fix the "clicky noise" issue
appearing on switch of some tracks, caused by lack of crossfading - and, as for
now, only implements fade in/fade out/crossfade functions. Its goals are to be as
simple and flexible as possible (meaning it should work independant of particular
AudioManager instance) and dont rely on third party libs unless necessary

## Dependencies:

For the time being, this project depends solely on panda3d

## Limitations:

If you want to crossfade tracks - instance of AudioManager to which they belong,
should have concurrent sound limit set to 2 or more. For how to set things up,
[check official documentation](https://docs.panda3d.org/1.10/python/reference/panda3d.core.AudioManager#panda3d.core.AudioManager.setConcurrentSoundLimit).

## Usage:

- Install library with setup.py
- Check [usage examples](https://github.com/moonburnt/p3dae/tree/master/example)

## License:

This software has been licensed under [MIT](LICENSE). For license of media used
in example snippets, see [media_info.txt](
https://github.com/moonburnt/p3dae/tree/master/example/media_info.txt)

