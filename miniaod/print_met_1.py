import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/30000/B8C1F9F9-871F-E911-BC4D-0CC47AC52AFC.root'])

mets, metLabel = Handle("std::vector<pat::MET>"), "slimmedMETs"
puppimets, puppimetLabel = Handle("std::vector<pat::MET>"), "slimmedMETsPuppi"

for event in events:

    if event.eventAuxiliary().event() != 1183564:
        continue

    if event.eventAuxiliary().luminosityBlock() != 2595:
        continue

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())
    
    event.getByLabel(metLabel, mets)
    event.getByLabel(puppimetLabel, puppimets)

    met = mets.product().front()
    print "met.pt() = "+str(met.pt())
    print "met.px() = "+str(met.px())
    print "met.py() = "+str(met.py())
    print "met.uncorPt() = "+str(met.uncorPt())
    print "met.uncorPx() = "+str(met.uncorPx())
    print "met.uncorPy() = "+str(met.uncorPy())


    puppimet = puppimets.product().front()
    print "puppimet.pt() = "+str(puppimet.pt())
    print "puppimet.uncorPt() = "+str(puppimet.uncorPt())
    
    
    
