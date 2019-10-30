#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Shift Matrix Down, overflowing from Left (Top) to Right (Bottom)

def copyRow(fromAddress, toAddress):
  SetChVal(toAddress - 1, GetChVal(fromAddress - 1))
  SetChVal(toAddress + 0, GetChVal(fromAddress + 0))
  SetChVal(toAddress + 1, GetChVal(fromAddress + 1))
  SetChVal(toAddress + 2, GetChVal(fromAddress + 2))
  SetChVal(toAddress + 3, GetChVal(fromAddress + 3))


copyRow(49, 54)
copyRow(44, 49)
copyRow(39, 44)
copyRow(34, 39)
copyRow(22, 34)
copyRow(17, 22)
copyRow(12, 17)
copyRow(7, 12)
copyRow(2, 7)

SetChVal(1, 0)
SetChVal(2, 0)
SetChVal(3, 0)
SetChVal(4, 0)
SetChVal(5, 0)
