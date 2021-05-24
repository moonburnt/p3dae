from direct.interval.LerpInterval import LerpFunctionInterval
from direct.interval.IntervalGlobal import *
#from panda3d.core import AudioManager
import logging

log = logging.getLogger(__name__)

class AudioEffects:
    '''Class that implements ability to use various sound effects, such as fading
    and crossfading. For crossfade function to work, set_concurrent_sound_limit()
    of AudioManager attached to sounds should be set to 2 or more'''
    def __init__(self):
        log.debug("Initializing AudioEffects instance")

    def fade_out(self, song, speed = 0.5, stop:bool = True, reset_volume:bool = True):
        '''Slowly decrease song's volume within 'speed' amount of seconds.
        Then stop it (unless this option is disabled) and reset its volume to
        initial value (unless disabled aswell)'''

        #idk if this needs option to dont completely disable sound, but stop it
        #at some certain volume #TODO
        sequence = Sequence()

        current_volume = song.get_volume()
        fade_out_interval = LerpFunctionInterval(song.set_volume,
                                                 duration = speed,
                                                 fromData = current_volume,
                                                 toData = 0)

        sequence.append(fade_out_interval)
        if stop:
            sequence.append(Func(song.stop))

        if reset_volume:
            sequence.append(Func(song.set_volume, current_volume))

        log.debug(f"Fading out {song.getName()}")
        sequence.start()

    def fade_in(self, song, volume:float = 1.0, speed = 0.5):
        '''Slowly increase song's volume within 'speed' amount of seconds,
        until its volume reach specified amount'''
        #idk yet if there is a point in implementing safety checks for volume
        sequence = Sequence()

        #its a bit confusing, but status isnt bool and return 2 on playing
        if song.status() != 2:
            sequence.append(Func(song.play))

        fade_in_interval = LerpFunctionInterval(song.set_volume,
                                                duration = speed,
                                                fromData = 0,
                                                toData = volume)

        sequence.append(fade_in_interval)

        log.debug(f"Fading in {song.getName()}")
        sequence.start()

    def crossfade(self, song, active_songs:list = None, stop_active:bool = True,
                  fade_in_volume:float = 1.0, reset_volume:bool = True,
                  fade_out_speed = 0.5, fade_in_speed = 0.5):
        '''Slowly increase one song's volume, while decreasing others into silence.
        For the best effect, fade_out_speed and fade_in_speed should be set same'''
        #no safety checks for negative fading values yet #TODO
        parallel = Parallel()

        if active_songs:
            for track in active_songs:
                parallel.append(Func(self.fade_out,
                                     song = track,
                                     speed = fade_out_speed,
                                     stop = stop_active,
                                     reset_volume = reset_volume))

        parallel.append(Func(self.fade_in,
                             song = song,
                             volume = fade_in_volume,
                             speed = fade_in_speed))

        log.debug(f"Crossfading {song.getName()}")
        parallel.start()
