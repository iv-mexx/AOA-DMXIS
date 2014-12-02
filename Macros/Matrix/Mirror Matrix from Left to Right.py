#===============================================================
# DMXIS Macro (c) 2014 Markus Chmelar
#===============================================================

# Mirror the left matrix to the right matrix

offset = 1
numCols = 5
numRows = 5
bankSize = 32
fromBank = 1
toBank = 2

def addressForPoint(row, col, bank):
  return offset + ((bank - 1) * (bankSize - 1)) + (row * numCols) + col

for row in range(0, numRows):
  for col in range(0, numCols):
    fromRow = row
    toRow = row

    fromCol = col
    toCol = numCols - col

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

    # print "copy from point ({0},{1}) to point ({2},{3})".format(fromRow, fromCol, toRow, toCol)
    print "copy from channel {0} to channel {1}".format(GetChName(fromChannel), GetChName(toChannel))
