#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Shift Matrix Up, overflowing from Right (Bottom) to Left (Top)

def copyRow(fromAddress, toAddress):
  SetChVal(toAddress - 1, GetChVal(fromAddress - 1))
  SetChVal(toAddress + 0, GetChVal(fromAddress + 0))
  SetChVal(toAddress + 1, GetChVal(fromAddress + 1))
  SetChVal(toAddress + 2, GetChVal(fromAddress + 2))
  SetChVal(toAddress + 3, GetChVal(fromAddress + 3))


copyRow(7, 2)
copyRow(12, 7)
copyRow(17, 12)
copyRow(22, 17)
copyRow(34, 22)
copyRow(39, 34)
copyRow(44, 39)
copyRow(49, 44)
copyRow(54, 49)

SetChVal(53, 0)
SetChVal(54, 0)
SetChVal(55, 0)
SetChVal(56, 0)
SetChVal(57, 0)
