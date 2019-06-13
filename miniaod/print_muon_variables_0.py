import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/data/Run2016H/SingleMuon/MINIAOD/03Feb2017_ver2-v1/80000/2C8B0F05-7AEA-E611-81BC-001E674FB1D5.root'])

muons, muonLabel = Handle("std::vector<pat::Muon>"), "slimmedMuons"


for event in events:

    #if event.eventAuxiliary().luminosityBlock() != 209529:
    #    continue

    if event.eventAuxiliary().event() != 1523698996:
        continue

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())

    event.getByLabel(muonLabel,muons)
    
    for muon in muons.product():
        print muon.pt()
        print muon.eta()
        print muon.isGlobalMuon()
        print muon.isPFMuon()
        print muon.numberOfMatchedStations()
        print muon.innerTrack().hitPattern().numberOfValidPixelHits()
        print muon.innerTrack().hitPattern().trackerLayersWithMeasurement() 
#        print muon.globalTrack().normalizedChi2()
        break

