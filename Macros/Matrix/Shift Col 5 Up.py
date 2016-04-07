#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Copy the left matrix to the right matrix

offset = 1
numCols = 5
numRows = 5
bankSize = 33
col = 4

def addressForPoint(row, col, bank):
  return offset + ((bank - 1) * (bankSize - 1)) + (row * numCols) + col

for bank in range(1, 3):
  fromBank = bank
  toBank = bank
  for row in range(1, numRows):
    fromRow = row
    toRow = row-1
    fromCol = col
    toCol = col

    fromChannel = addressForPoint(fromRow, fromCol, fromBank)
    toChannel = addressForPoint(toRow, toCol, toBank)

    SetChVal(toChannel, GetChVal(fromChannel))
    SetChEnabled(toChannel, GetChEnabled(fromChannel))

    SetChVal(toChannel, GetChVal(fromChannel))
    SetOscAmount(toChannel, GetOscAmount(fromChannel))
    SetOscType(toChannel, GetOscType(fromChannel))
    SetOscSpeed(toChannel, GetOscSpeed(fromChannel))
    SetOscChase(toChannel, GetOscChase(fromChannel))
    SetOscShape(toChannel, GetOscShape(fromChannel))
