#===============================================================
# DMXIS Macro (c) 2019 Markus Chmelar
#===============================================================

# Copy Channel Settings from Color Channels (Ego Risers) to the Complementary Color Channels
for ch in range(106, 112):
  SetChEnabled(ch, GetChEnabled(ch - 8))
  SetChVal(ch, GetChVal(ch - 8))
  SetOscAmount(ch, GetOscAmount(ch - 8))
  SetOscType(ch, GetOscType(ch - 8))
  SetOscSpeed(ch, GetOscSpeed(ch - 8))
  SetOscChase(ch, GetOscChase(ch - 8))
  SetOscShape(ch, GetOscShape(ch - 8))