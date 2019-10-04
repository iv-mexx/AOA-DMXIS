#===============================================================
# DMXIS Macro (c) 2010 db audioware limited
#===============================================================

# Grab a local copy of the selected channels and their settings
numSelCh = GetNumSelCh()
if numSelCh==0: Message("Select some channels first!")

selCh=[]
selVal=[]
selLevel=[]
selBand=[]
selAttack=[]
selRelease=[]
selDir=[]
selType=[]
selAmount=[]
selChase=[]
selSpeed=[]
selShape=[]

for i in range(numSelCh):
    ch = GetSelCh(i)
    selCh.append(ch)
    selVal.append(GetChVal(ch))
    selLevel.append(GetStLevel(ch))
    selBand.append(GetStBand(ch))
    selAttack.append(GetStAttack(ch))
    selRelease.append(GetStRelease(ch))
    selDir.append(GetStDir(ch))
    selType.append(GetOscType(ch))
    selAmount.append(GetOscAmount(ch))
    selChase.append(GetOscChase(ch))
    selSpeed.append(GetOscSpeed(ch))
    selShape.append(GetOscShape(ch))
    
# Copy the channel settings to every bank & preset
for b in range(GetNumBanks()):
    LoadBank(b)
    for p in range(GetNumPresets()):
        LoadPreset(p)
        for i in range(numSelCh):
            ch = selCh[i]
            SetChVal(ch, selVal[i])
            SetStLevel(ch, selLevel[i])
            SetStBand(ch, selBand[i])
            SetStAttack(ch, selAttack[i])
            SetStRelease(ch, selRelease[i])
            SetStDir(ch, selDir[i])
            SetOscType(ch, selType[i])
            SetOscAmount(ch, selAmount[i])
            SetOscChase(ch, selChase[i])
            SetOscSpeed(ch, selSpeed[i])
            SetOscShape(ch, selShape[i])
        SaveCurrentPreset()
        
Message("The selected channels have been\ncopied to every preset in every bank")