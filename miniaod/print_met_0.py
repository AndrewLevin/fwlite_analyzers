import ROOT
import sys
from DataFormats.FWLite import Events, Handle

events = Events (['root://cms-xrd-global.cern.ch//store/data/Run2016B/DoubleMuon/MINIAOD/17Jul2018_ver2-v1/40000/0E0B06FC-008B-E811-9E4F-0025905A6110.root '])

#events = Events (['root://xrootd-cms.infn.it//store/data/Run2016B/DoubleMuon/MINIAOD/03Feb2017_ver2-v2/100000/CADA3398-13ED-E611-91B8-002590DD7E50.root'])

mets, metsLabel = Handle("vector<pat::MET>"),"slimmedMETs"
puppimets, puppimetsLabel = Handle("vector<pat::MET>"),"slimmedMETsPuppi"

for event in events:

    #if event.eventAuxiliary().luminosityBlock() != 209529:
    #    continue

    if event.eventAuxiliary().event() != 114052244:
        continue

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())

    event.getByLabel(metsLabel,mets)
    event.getByLabel(puppimetsLabel,puppimets)
    
    for met in mets.product():
        print met.pt()
        print met.uncorPt()
        print met.shiftedPt(ROOT.pat.MET.JetEnUp)
        print met.shiftedPt(ROOT.pat.MET.JetEnDown)
        print met.shiftedPt(ROOT.pat.MET.JetResUp)
        print met.shiftedPt(ROOT.pat.MET.JetResDown)
        print met.shiftedPt(ROOT.pat.MET.UnclusteredEnUp)
        print met.shiftedPt(ROOT.pat.MET.UnclusteredEnDown)
        print met.phi()

    for puppimet in puppimets.product():
        print puppimet.pt()
        print puppimet.uncorPt()
        print puppimet.shiftedPt(ROOT.pat.MET.JetEnUp)
        print puppimet.shiftedPt(ROOT.pat.MET.JetEnDown)
        print puppimet.shiftedPt(ROOT.pat.MET.JetResUp)
        print puppimet.shiftedPt(ROOT.pat.MET.JetResDown)
        print puppimet.shiftedPt(ROOT.pat.MET.UnclusteredEnUp)
        print puppimet.shiftedPt(ROOT.pat.MET.UnclusteredEnDown)
        print puppimet.phi()

        
