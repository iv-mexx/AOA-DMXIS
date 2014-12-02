#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Disable the global dimmer for the matrix
# Enable all other channels for the matrix


for ch in range(0,511):
  SetChEnabled(ch, 0)

SetChEnabled(0, 0)
SetChEnabled(32, 0)

for ch in range(1, 28):
  SetChEnabled(ch, 1)
  SetChEnabled(ch + 32, 1)
