#!/usr/bin/env python3

import p3dae
from direct.showbase.ShowBase import ShowBase
import logging

SONG_0 = "./OveMelaa - Trance Bit Bit Loop.ogg"
SONG_1 = "./Ove Melaa Supa Powa Loop B.ogg"

# this library supports logging via python's logger module. But if you wont use
# it, nothing bad will happen - you just wont get status updates in terminal
log = logging.getLogger()
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
log.addHandler(handler)


class Game(ShowBase):
    def __init__(self):
        # Setting up base stuff
        super().__init__()
        self.disable_mouse()

        # because in this example we are using default musicManager for simplicity,
        # increasing its concurrent sound limit from default (1) to ensure things
        # will crossfade properly
        base.musicManager.set_concurrent_sound_limit(2)

        self.music_effects = p3dae.AudioEffects()

        # loading up sounds and ensuring they wont stop preemptively
        self.song_0 = loader.loadMusic(SONG_0)
        self.song_1 = loader.loadMusic(SONG_1)
        self.song_0.setLoop(True)
        self.song_1.setLoop(True)

        # fade in example, where we start the track and slowly increase its volume.
        # Keep in mind that track's volume and AudioManager's volume are different
        # things that affect eachother, but dont override
        self.music_effects.fade_in(self.song_0, volume=1.0, speed=3)

        # after 5 secs of playback, crossfading it with second track
        base.taskMgr.doMethodLater(
            5, self.crossfade_tracks, f"crossfade {self.song_0} and {self.song_1}"
        )

    def crossfade_tracks(self, event):
        # crossfading example, where we make one track slowly switch to other and
        # then stop. For best experience, use small timeframes (in between 0.5 and
        # 3 seconds) and make fade in and fade out speeds match eachother
        self.music_effects.crossfade(
            song=self.song_1,
            active_songs=[self.song_0],
            fade_in_speed=2.5,
            fade_out_speed=2.5,
        )
        base.taskMgr.doMethodLater(10, self.fadeout_track, f"fade out {self.song_1}")

        return

    def fadeout_track(self, event):
        # fading out example, where we fade out song with default settings
        self.music_effects.fade_out(self.song_1)

        print("Thats it!")
        return


if __name__ == "__main__":
    play = Game()
    play.run()
