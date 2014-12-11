#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Shift the whole Sunstrip up by one

offset = 0
numChannels = 10
bankSize = 16

def copyChannel(fromChannel, toChannel):
  SetChVal(toChannel, GetChVal(fromChannel))
  SetChEnabled(toChannel, GetChEnabled(fromChannel))

  SetChVal(toChannel, GetChVal(fromChannel))
  SetOscAmount(toChannel, GetOscAmount(fromChannel))
  SetOscType(toChannel, GetOscType(fromChannel))
  SetOscSpeed(toChannel, GetOscSpeed(fromChannel))
  SetOscChase(toChannel, GetOscChase(fromChannel))
  SetOscShape(toChannel, GetOscShape(fromChannel))

for channel in range(64, 73):
  copyChannel(channel+1, channel)
  copyChannel(channel+1+bankSize, channel+bankSize)

