#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Disable the global dimmer for the matrix
# Enable all other channels for the matrix

for ch in range(64, 74):
  SetChEnabled(ch, 1)
  SetChEnabled(ch + 16, 1)
