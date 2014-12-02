#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================
    
# Get the user selected channels 
ns = GetNumSelCh()
if ns==0: 
    Message("Select some channels first!")

# Fan out the channels evenly
for i in range(ns):
    SetChVal(GetSelCh(i), 128)
