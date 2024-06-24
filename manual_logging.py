#!/usr/bin/env python3

from Run import MiniCSCRun

mRun = MiniCSCRun('test')


def askForLayer():
    print('What is Layer are you using?:')
    if mRun.setLayer(input()) == -1:
        print('Layer name not supported')
        print(f'Available layers are:\t{mRun.allowedLayers()}')
        askForLayer()

def askForSource():
    print('What source are you using?:')
    if mRun.setSource(input()) == -1:
        print('Source not supported')
        print(f'Source options are:\t{mRun.allowedSources()}')
        askForSource()

def askForHole():
    print(f'Which hole is the {mRun.getSource()} source placed on?')
    if mRun.setHole(input()) == -1:
        print('Location does not exist (must be integer between 1-6)')
        askForHole()
    


if __name__ == "__main__":
    askForLayer()

    print(f'You have entered layer:\t{mRun.getLayer()}\n')

    askForSource()

    print(f'You have entered source:\t{mRun.getSource()}\n')

    if mRun.getSource() != 'No Source':
        askForHole()
        print(f'Source located in hole:\t{mRun.getHole()}')
