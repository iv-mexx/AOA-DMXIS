#===============================================================
# DMXIS Macro (c) 2019 Markus Chmelar
#===============================================================

# Disable Channesl for Ego-Risers and Wash

SetChEnabled(28, 0)
SetChEnabled(29, 0)
SetChEnabled(30, 0)
SetChEnabled(31, 0)

SetChEnabled(74, 0)
SetChEnabled(75, 0)
SetChEnabled(76, 0)
SetChEnabled(77, 0)
SetChEnabled(78, 0)
SetChEnabled(79, 0)

for ch in range(96, 106):
  SetChEnabled(ch, 0)
  SetChEnabled(ch + 16, 0)