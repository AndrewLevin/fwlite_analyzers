import ROOT
import sys
from DataFormats.FWLite import Events, Handle

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EEF150FB-C5B1-E611-87B0-FA163EFD20EB.root'])

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/80008/9C1072E7-FC82-E611-A3CD-0CC47A78A3F8.root']) 

events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/70001/901B42AA-D229-E711-AD84-A4BF0101202F.root']) 

#events = Events (['/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.root']) 

genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

photons,photonsLabel = Handle("vector<reco::Photon>"), 'gedPhotons'

ebdigis,ebdigisLabel = Handle("EBDigiCollection"),("selectDigi","selectedEcalEBDigiCollection","RECO")

#puSummaryInfo,puSummaryInfoLabel = Handle("vector<PileupSummaryInfo>"),("addPileupInfo")
puSummaryInfo,puSummaryInfoLabel = Handle("vector<PileupSummaryInfo>"),("mixData")

from math import hypot, pi

def deltaPhi(phi1,phi2):
    ## Catch if being called with two objects                                                                                                                                             
    if type(phi1) != float and type(phi1) != int:
        phi1 = phi1.phi
    if type(phi2) != float and type(phi2) != int:
        phi2 = phi2.phi
    ## Otherwise                                                                                                                                                                          
    dphi = (phi1-phi2)
    while dphi >  pi: dphi -= 2*pi
    while dphi < -pi: dphi += 2*pi
    return dphi

def deltaR(eta1,phi1,eta2=None,phi2=None):
    ## catch if called with objects                                                                                                                                                       
    if eta2 == None:
        return deltaR(eta1.eta,eta1.phi,phi1.eta,phi1.phi)
    ## otherwise                                                                                                                                                                          
    return hypot(eta1-eta2, deltaPhi(phi1,phi2))

# loop over events
count= 0
for event in events:

    if event.eventAuxiliary().luminosityBlock() != 1054017:
        continue

    if event.eventAuxiliary().event() != 480842431:
        continue

    event.getByLabel(genParticlesLabel, genparticles)

#    event.getByLabel(photonsLabel, photons)
    event.getByLabel(puSummaryInfoLabel, puSummaryInfo)

    print "len(puSummaryInfo.product()) = "+str(len(puSummaryInfo.product()))

    for pu in puSummaryInfo.product():
        if pu.getBunchCrossing() != 0:
            continue
        print "len(pu.getPU_EventID()) = "+str(len(pu.getPU_EventID()))
        for eventid in pu.getPU_EventID():
            print str(eventid.run()) + " "+str(eventid.luminosityBlock()) + " " + str(eventid.event())



