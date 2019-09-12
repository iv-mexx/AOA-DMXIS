#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Shift the whole Sunstrip Down by one

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

for channel in reversed(range(64, 73)):
  copyChannel(channel, channel+1)
  copyChannel(channel+bankSize, channel+1+bankSize)

