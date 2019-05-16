import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/LNuAJJ_EWK_MJJ-120_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/00000/0E5DFD98-6820-E711-B304-001E67580724.root'])

lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "externalLHEProducer"

for event in events:

    if event.eventAuxiliary().luminosityBlock() != 213 or event.eventAuxiliary().event() != 39465:
        continue

    event.getByLabel(lheinfoLabel,lheinfo)

    print lheinfo.product().originalXWGTUP()
    print len(lheinfo.product().weights())
    for i in range(0,len(lheinfo.product().weights())):
        print lheinfo.product().weights()[i].wgt

    break
