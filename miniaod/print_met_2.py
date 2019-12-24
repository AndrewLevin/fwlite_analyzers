import ROOT
from DataFormats.FWLite import Events, Handle
import numpy

events1 = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/60000/FEF52C15-5142-E911-8AE2-AC1F6B56768C.root'])
events2 = Events (['/afs/cern.ch/user/a/amlevin/for_nanoaod_pull_request/CMSSW_11_0_0_pre11/corMETMiniAOD.root'])

mets, metLabel = Handle("std::vector<pat::MET>"), "slimmedMETs"
puppimets, puppimetLabel = Handle("std::vector<pat::MET>"), "slimmedMETsPuppi"

puppimets1 = []
puppimets2 = []

for event in events1:

    event.getByLabel(metLabel, mets)
    event.getByLabel(puppimetLabel, puppimets)

    met = mets.product().front()
    puppimet = puppimets.product().front()
    
    puppimets1.append(puppimet.pt())


for event in events2:

    event.getByLabel(metLabel, mets)
    event.getByLabel(puppimetLabel, puppimets)

    met = mets.product().front()
    puppimet = puppimets.product().front()
    
    puppimets2.append(puppimet.pt())

assert(len(puppimets1) == len(puppimets2))

abspuppimetdiffs = []

for i in range(len(puppimets1)):
    abspuppimetdiffs.append(abs(puppimets1[i] - puppimets2[i]))

print numpy.mean(abspuppimetdiffs)
print numpy.std(abspuppimetdiffs)
