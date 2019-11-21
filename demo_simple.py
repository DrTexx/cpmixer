import cpmixer

mixer = cpmixer.Mixer()

print(mixer.gvol())
print(mixer.svol(50))
print("mute:", mixer.gmute())
mixer.smute(True)
print("mute:", mixer.gmute())
mixer.smute(False)
print("mute:", mixer.gmute())
