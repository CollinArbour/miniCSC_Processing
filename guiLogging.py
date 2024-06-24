#!/usr/bin/env python3
from easygui import *
from Run import MiniCSCRun as  mcsc
import os
from datetime import datetime

now = datetime.now()
mdate = now.strftime("%Y_%m_%d__%H_%M")

run = 0

title = 'MiniCSC DataRun Logging script'


layers = ['L1','L2']
srcs = ['Cd-109','Sr-90','No Source']
holes = ['1','2','3','4','5','6']


logRun = ynbox('Would you like to run a data-taking run?')

while logRun:
    stamp = f'{mdate}__run{run}'
    print(stamp)

    log_nm = f'./logs/{stamp}'
    os.mkdir(log_nm)

    # Initialize run object
    mrun = mcsc(stamp)

    # Which Layer?
    layer = buttonbox('Which Layer is being tested?', choices=layers)
    mrun.setLayer(layer)
    print(f'Layer:\t{layer}')

    # Which Source?
    src = buttonbox('What source are you using?', choices=srcs)
    mrun.setSource(src)
    print(f'Source:\t{src}')

    if(mrun.getSource() != 'No Source'):
        hole = buttonbox('Placed at what Hole?',choices=holes)
        mrun.setHole(hole)
        print(f'Hole:\t{hole}')

    # What is High Voltage set to? 
    hv = enterbox('What is High Voltage setting? (V)')
    mrun.setHV(hv)
    print(f'HV:\t{hv}')

    # How many events?
    evts = enterbox('How many events are you collecting?')
    print(f'Number of Events:\t{evts}')

    # Record initial TMB Dump
    idump = enterbox('Please input the 10 second TMB dump for run with HV not included')

    with open(f'{log_nm}/initial_TMB_Dump.txt','w') as fl:
        fl.write(idump)

    # Record running TMB Dump
    rdump = enterbox('Please input the 10 second TMB dump for run with HV turned on')

    with open(f'{log_nm}/running_TMB_Dump.txt','w') as fl:
        fl.write(rdump)
    

    # Dump all info in run log text file
    with open(f'{log_nm}/Run_Log.txt','w') as fl:
        fl.write(f'Stamp:\t{stamp}\n\n')
        fl.write(f'Layer:\t{layer}\n')
        fl.write(f'Source:\t{src}\n')
        if(mrun.getSource() != 'No Source'):
            fl.write(f'Hole:\t{hole}\n')
        fl.write(f'HV:\t{hv}\n')
        fl.write(f'Number of Events:\t{evts}\n')
    
    run += 1

    # End of logging actions
    logRun = ynbox('Would you like to run a data-taking run?')
