import ROOT
import sys
from DataFormats.FWLite import Events, Handle

from math import hypot, pi, sqrt, acos


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

events = Events (['/afs/cern.ch/work/a/amlevin/delete_this/SMP-RunIIWinter15pLHE-00008.root.bak'])

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/FAF3A57A-9B1F-E911-9D89-24BE05C3CBD1.root '])

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/0444D421-3448-E911-A380-AC1F6B596094.root'])  

lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "source"
#lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "externalLHEProducer"

h=ROOT.TH1D('','',16,0,pi)

n_events_processed = 0

for event in events:

    if n_events_processed % 10000 == 0 :
        print "n_events_processed = "+str(n_events_processed)

    n_events_processed+=1

#    if event.eventAuxiliary().event() != 16355436:
#    if event.eventAuxiliary().event() != 31915392:
#    if event.eventAuxiliary().event() != 31688057:
#        continue

    event.getByLabel(lheinfoLabel,lheinfo)

    v_photon=ROOT.TLorentzVector();
    v_lepton1=ROOT.TLorentzVector();
    v_lepton2=ROOT.TLorentzVector();

    njets = 0

    fsr=False

    for i in range(0,len(lheinfo.product().hepeup().IDUP)):

        if lheinfo.product().hepeup().ISTUP.at(i) == 1 and (abs(lheinfo.product().hepeup().IDUP.at(i)) == 1 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 2 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 3 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 4 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 5 or abs(lheinfo.product().hepeup().IDUP.at(i)) == 21):
            njets+=1

        if lheinfo.product().hepeup().IDUP.at(i) == 22:
            v_photon.SetPxPyPzE(lheinfo.product().hepeup().PUP.at(i)[0],lheinfo.product().hepeup().PUP.at(i)[1],lheinfo.product().hepeup().PUP.at(i)[2],lheinfo.product().hepeup().PUP.at(i)[3])

#        if lheinfo.product().hepeup().IDUP.at(i) == 11 or lheinfo.product().hepeup().IDUP.at(i) == 13:
#        if lheinfo.product().hepeup().IDUP.at(i) == 11:
#        if lheinfo.product().hepeup().IDUP.at(i) == 15:
        if lheinfo.product().hepeup().IDUP.at(i) == 13:
            v_lepton1.SetPxPyPzE(lheinfo.product().hepeup().PUP.at(i)[0],lheinfo.product().hepeup().PUP.at(i)[1],lheinfo.product().hepeup().PUP.at(i)[2],lheinfo.product().hepeup().PUP.at(i)[3])

#        if lheinfo.product().hepeup().IDUP.at(i) == -11 or lheinfo.product().hepeup().IDUP.at(i) == -13:
#        if lheinfo.product().hepeup().IDUP.at(i) == -11:
#        if lheinfo.product().hepeup().IDUP.at(i) == -15:
        if lheinfo.product().hepeup().IDUP.at(i) == -13:
            v_lepton2.SetPxPyPzE(lheinfo.product().hepeup().PUP.at(i)[0],lheinfo.product().hepeup().PUP.at(i)[1],lheinfo.product().hepeup().PUP.at(i)[2],lheinfo.product().hepeup().PUP.at(i)[3])

            
    if v_photon.M() == 0 or v_lepton1.M() == 0 or v_lepton2.M() == 0:
        continue

    if v_lepton1.Pt() > 20 and v_photon.Pt() > 20:
        h.Fill(abs(deltaPhi(v_lepton1.Phi(),v_photon.Phi())))

    #break
c=ROOT.TCanvas()
h.SetStats(0)
h.SetMinimum(0)
h.Draw()
c.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")
