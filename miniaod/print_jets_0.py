import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/30000/B8C1F9F9-871F-E911-BC4D-0CC47AC52AFC.root'])

jets, jetsLabel = Handle("std::vector<pat::Jet>"), "slimmedJets"

for event in events:

    if event.eventAuxiliary().event() != 1183564:
        continue

    if event.eventAuxiliary().luminosityBlock() != 2595:
        continue

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())

    event.getByLabel(jetsLabel, jets)

    for i,j in enumerate(jets.product()):
        print "j.eta() = "+str(j.eta())
        print "j.pt() = "+str(j.pt())
        print "j.pt()*j.jecFactor('Uncorrected') = "+str(j.pt()*j.jecFactor('Uncorrected'))
        print "j.jecFactor(\"Uncorrected\") = "+str(j.jecFactor("Uncorrected"))
    
    
    
    
