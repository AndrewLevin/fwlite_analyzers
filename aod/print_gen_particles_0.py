import ROOT
import sys
from DataFormats.FWLite import Events, Handle

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/EEF150FB-C5B1-E611-87B0-FA163EFD20EB.root'])

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16DR80Premix/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v2/70001/901B42AA-D229-E711-AD84-A4BF0101202F.root']) 

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/80008/9C1072E7-FC82-E611-A3CD-0CC47A78A3F8.root']) 

events = Events (['/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.1.root','/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.2.root','/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.3.root','/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.4.root','/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.5.root','/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.6.root','/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.7.root','/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.8.root','/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.9.root','/afs/cern.ch/work/a/amlevin/wjets_prod/CMSSW_8_0_21/src/SMP-RunIISummer16DR80Premix-00199.10.root']) 

genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

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

    if event.eventAuxiliary().luminosityBlock() != 452505:
        continue

    if event.eventAuxiliary().event() != 206432897:
        continue

    event.getByLabel(genParticlesLabel, genparticles)

    for genparticle in genparticles.product():

#        if deltaR(genparticle.eta(),genparticle.phi(),0.1269836,1.9614257) > 0.7:
#            continue
        
        
#        if genparticle.pt() < 10:
#            continue

        if genparticle.mother(0) and genparticle.mother(1):
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mass())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+ str(genparticle.mother(0).eta())+ " " +str(genparticle.mother(0).phi()) +" "+str(genparticle.mother(0).mass()) + " " +str(genparticle.mother(1).pdgId())+" "+str(genparticle.mother(1).pt())+" "+str(genparticle.mother(1).eta())+" "+str(genparticle.mother(1).phi())+" "+str(genparticle.mother(1).mass())+" "+str(genparticle.numberOfMothers())
        elif genparticle.mother(0):
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mass())+" "+str(genparticle.mother(0).pdgId())+" "+str(genparticle.mother(0).pt())+" "+str(genparticle.mother(0).eta())+" "+ str(genparticle.mother(0).phi())+" "+str(genparticle.mother(0).mass())+" "+str(genparticle.numberOfMothers())
        else:
            print str(genparticle.status())+" "+str(genparticle.pdgId())+" "+str(genparticle.pt())+" "+str(genparticle.eta())+" "+str(genparticle.phi())+" "+str(genparticle.mass())+" "+str(genparticle.numberOfMothers())



