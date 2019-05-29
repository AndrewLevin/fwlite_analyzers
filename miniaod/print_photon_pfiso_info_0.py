import ROOT
import sys
from DataFormats.FWLite import Events, Handle

#events = Events (['root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleElectron/MINIAOD/03Feb2017_ver2-v2/110000/8E9BFBDA-49EB-E611-A3F8-6C3BE5B58198.root '])
#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/40000/24EF20BF-A82D-E911-AB94-801844DEEFD8.root'])

events = Events(['/eos/user/a/amlevin/data/miniaodsim/za_lowmll/s3_merge_ZA_lowmass_197092_187.root'])

photons, photonLabel = Handle("std::vector<pat::Photon>"), "slimmedPhotons"
pfcands, pfcandsLabel = Handle("vector<pat::PackedCandidate>"), "packedPFCandidates"

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

for event in events:

    #if event.eventAuxiliary().luminosityBlock() != 209529:
    #    continue

#    print event.eventAuxiliary().event()

    if event.eventAuxiliary().event() != 18890133:
        continue

    print "run %6d, lumi %4d, event %12d" % (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())

    event.getByLabel(photonLabel,photons)
    
    for pho in photons.product():
        print "pho.pt() = "+str(pho.pt())
        print "pho.chargedHadronIso() = "+str(pho.chargedHadronIso())
        print "pho.photonIso() = "+str(pho.photonIso())
        print "pho.eta() = "+str(pho.eta())
        print "pho.superCluster().eta() = "+str(pho.superCluster().eta())
        print "pho.userFloat(\"phoChargedIsolation\") = "+str(pho.userFloat("phoChargedIsolation"))
        print "pho.userFloat(\"phoPhotonIsolation\") = "+str(pho.userFloat("phoPhotonIsolation"))

    event.getByLabel(pfcandsLabel,pfcands)

    for pfcand in pfcands.product():
        if pfcand.pt() < 5:
            continue
        if abs(pfcand.pdgId()) != 13:
            continue

        print pfcand.dz()
        print pfcand.dxy()
        print deltaR(pfcand.eta(),pfcand.phi(),pho.eta(),pho.phi())
        print pfcand.pt()
