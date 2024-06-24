#!/usr/bin/env python3

class MiniCSCRun:
    def __init__(self,name):
        self.name = name
    
        self._possibleLayers = ['L1','L2']
        self._possibleSources = {'None':'No Source','Cd':'Cd-109','Sr':'Sr-90'}
        self._numHoles = 6
        

    # Setters
    def setLayer(self,layer):
        if layer in self._possibleLayers:
            self._layer = layer
        else:
            return -1

    def setSource(self,src):
        if src in self._possibleSources.keys():
            self._source = self._possibleSources[src]
        elif src in self._possibleSources.values():
            self._source = src
        else:
            return -1

    def setHole(self,hole):
        try:
            mhole = int(hole)
        except:
            return -1

        if mhole > 0 and mhole <= self._numHoles:
            self._hole = mhole
        else:
            return -1

    def setHV(self,hv):
        self._hv = hv


    # Getters
    def allowedLayers(self):
        return(self._possibleLayers)
    def allowedSources(self):
        return(self._possibleSources)

    def getLayer(self):
        return self._layer
    def getSource(self):
        return self._source
    def getHole(self):
        return self._hole
    def getHV(self):
        return self._hv
