#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Select Matrices
for ch in range(1, 26):
  SelectCh(ch, 1)
  SelectCh(ch + 32, 1)
