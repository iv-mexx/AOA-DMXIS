#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Copy the left matrix to the right matrix

offset = 1
numChannels = 25
bankSize = 32
bankFrom = 1
bankTo = 2

for c in range(0, numChannels):
  fromChannel = (bankFrom - 1) * bankSize + offset + c
  toChannel = (bankTo - 1) * bankSize + offset + c
  SetChVal(toChannel, GetChVal(fromChannel))
  SetChEnabled(toChannel, GetChEnabled(fromChannel))
  
  SetChVal(toChannel, GetChVal(fromChannel))
  SetOscAmount(toChannel, GetOscAmount(fromChannel))
  SetOscType(toChannel, GetOscType(fromChannel))
  SetOscSpeed(toChannel, GetOscSpeed(fromChannel))
  SetOscChase(toChannel, GetOscChase(fromChannel))
  SetOscShape(toChannel, GetOscShape(fromChannel))