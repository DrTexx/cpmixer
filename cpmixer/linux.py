import alsaaudio
from template import MixerTemplate


class Mixer(MixerTemplate):
    def __init__(self,*args,**kwargs):
        super().__init__(
            self,
            *args,
            **kwargs,
        )


# print(alsaaudio.mixers())
# mixer = alsaaudio.Mixer(control='Master')
#
# print(mixer.cardname())
# print(mixer.mixer())
# print(mixer.mixerid())
# print(mixer.switchcap())
# print(mixer.volumecap())
# print(mixer.getenum())
# print(mixer.getmute())
# print(mixer.getrange())
# # print(mixer.getrec())
# print(mixer.getvolume())
# # print(mixer.setvolume())
# # print(mixer.setmute())
# # print(mixer.setrec())
# print(mixer.polldescriptors())
# print(mixer.handleevents())