import ROOT
import sys
from DataFormats.FWLite import Events, Handle
#from PhysicsTools.HepMCCandAlgos import MCTruthHelper


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

lumi = float(1)/float(1000)

#events = Events (['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/845C832E-F36A-EA11-98EB-E0071B691B81.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/10000/E623313E-F36A-EA11-AF84-FA163E85C21B.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/F2EC71AC-8D51-EA11-90B9-506B4BF38320.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/E800FBEB-8D51-EA11-BA58-3CFDFE63F7E0.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/E6B877AF-8D51-EA11-98E7-0CC47A4D7646.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/E6774F7D-8D51-EA11-A13B-C45444922991.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/DAB266AA-8D51-EA11-8778-B02628DEBFC0.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/D0A57A67-8D51-EA11-B43F-28924A3504DA.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/C0D3851E-E24E-EA11-BDD3-FA163E26B2D6.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/BCF7C268-8D51-EA11-8B62-34E6D7BEAF1B.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/BCF40DD0-8D51-EA11-AB2A-0CC47AACFCDE.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/BAE969C2-8D51-EA11-9B35-0242AC130002.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/BA61E173-8D51-EA11-8174-0CC47A00A832.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/B82F5868-8D51-EA11-A90C-0CC47A5FC2A5.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/ACE370C0-8D51-EA11-9BFE-001E67A3EA11.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/62FC4DBF-8D51-EA11-99C1-F0D4E2E5327C.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/603385B7-8D51-EA11-9890-0CC47A4DECEE.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/5ED2F06D-8D51-EA11-90AD-B083FED0FFCF.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/5EA1B26E-8D51-EA11-BE2B-3417EBE6444A.root','root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WA_aTGC_NLO_2016_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/5E990B69-8D51-EA11-BCD2-901B0E6459CE.root'])

#xs = 5.230

events = Events(["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/60A0E321-D746-E911-92B1-EC0D9A822606.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/E002395A-0846-E911-8030-24BE05C6E7C1.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/38CE855A-5646-E911-8927-24BE05C6E7C1.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/DA761D59-3A45-E911-A55F-0242AC130002.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/2A91AE16-0D46-E911-933E-0242AC130002.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/FCA1B7E1-3C46-E911-A7D3-34E6D7BDDECE.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/C2454FAB-0C47-E911-9F7C-68CC6EA5BCF2.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/E6C03788-2146-E911-993B-0242AC130002.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/FA23766B-F146-E911-BBF4-0242AC130002.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/18E85576-1146-E911-836F-FA163EA74C3A.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/12A8FEE6-FC45-E911-952E-FA163E860EED.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/E6009AAF-E846-E911-B292-FA163EBC5C21.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/3A8BB16E-8D47-E911-9631-FA163EC09F36.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/10134F44-8F47-E911-8DED-FA163ECFF9E2.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/7414D6D0-1C46-E911-B5D2-24BE05C4C891.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/425374C7-E846-E911-9ADD-506B4BB166AE.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/EA90A351-1346-E911-A39C-1866DAEB4284.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/BABAC58B-F846-E911-9C12-B083FED424C3.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/D4584C59-E548-E911-A600-FA163E54E91E.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/705ABB2F-8E49-E911-90D3-FA163EC5FAA6.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7690906B-2448-E911-B65B-FA163E9B74D4.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9081CC7A-6948-E911-A729-FA163E122FAF.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/5429635F-CD48-E911-BD9F-FA163E7CA4F7.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/726B0A56-5347-E911-8EFA-24BE05C63721.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/422F0C14-8F49-E911-973A-FA163EA0A883.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/260000/B0B098CB-7B51-E911-B2F6-484D7E8DF05E.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/7C2E6CD4-1F50-E911-921D-509A4C74908E.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/70A0693C-4A50-E911-8275-40F2E9C6AE21.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/50323553-6B49-E911-A3E0-A4BF0112BBF4.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/782D1D07-3D4A-E911-8145-001E67E34165.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/B64986C1-4A50-E911-8B82-A4BADB1E6F27.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/2E65F760-254F-E911-8631-0025907277CE.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/AE6F2C3B-964E-E911-9CB8-509A4C83D54F.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/D0BBD7C2-9549-E911-88A2-0CC47AFCC6B2.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/7CE2526A-314A-E911-B760-0025905D1D52.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/BA99D144-F14F-E911-A6A7-484D7E8DF0B9.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/E68F916F-FD4F-E911-AE1E-008CFAE45380.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/DE3D4436-2F4F-E911-9F0F-A0369FF8852A.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/3A244DE1-F64F-E911-9FDA-0CC47A0092D0.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/9EC2C161-0450-E911-93B6-AC1F6B1AF176.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/60000/FC30BBCE-0D50-E911-BF93-002590D9D896.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/B47C84F4-FD4E-E911-A4E9-D48564599CEE.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/60B2C568-0D4E-E911-B04C-A0369FF88332.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/110000/885752AB-DA4D-E911-BD5D-38EAA78D8AD0.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/70000/3207E250-FB4D-E911-8AB7-509A4C72D502.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/270000/0CBAEC7F-014F-E911-BA6E-00259029E670.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/0C8794DF-5148-E911-83A4-A4BF011588E0.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/CA53C4E2-1F49-E911-9B0C-A4BF01125490.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/EEDB9047-5748-E911-9291-0242AC1C0503.root","root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv3/WGToLNuG_01J_5f_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/120000/BE8520D0-6A48-E911-BB43-0242AC1C0500.root"])

xs = 178.6

#events = Events(['/eos/user/w/wangk/andrew/miniaodsim/wpa_powheg/mergeStep3_1990163_0.root'])

#events = Events(['/eos/user/w/wangk/andrew/miniaodsim/wpa_powheg/mergeStep3_1990163_0.root','/eos/user/w/wangk/andrew/miniaodsim/wpa_powheg/mergeStep3_1990163_1.root','/eos/user/w/wangk/andrew/miniaodsim/wpa_powheg/mergeStep3_1990163_2.root'])

handleLHEEventProduct  = Handle ("LHEEventProduct")
labelLHEEventProduct = ("externalLHEProducer")
#lheinfo,lheinfoLabel = Handle("LHEEventProduct"), "externalLHEProducer"
geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"
genparticles, genParticlesLabel = Handle("vector<reco::GenParticle>"), "genParticles"

labelPruned = ("prunedGenParticles")
labelPacked = ("packedGenParticles")

handlePruned  = Handle ("std::vector<reco::GenParticle>")
handlePacked  = Handle ("std::vector<pat::PackedGenParticle>")

geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"

count = 0
countweighted = 0

h_photon_pt=ROOT.TH1F("photon_pt","photon_pt",18,200,2000)

h_photon_pt.Sumw2()

for event in events:

    if count > 2000000:
#    if count > 500000:
#    if count > 100000:
#    if count > -1:
        break

    if count % 10000 == 0:
#    if count % 1 == 0:
        print "count = " + str(count)

    count +=1

    event.getByLabel(geninfoLabel,geninfo)

    gen = geninfo.product()

    if gen.weight() > 0:
        countweighted += 1
    else:
        countweighted -= 1
    
    event.getByLabel (labelPacked, handlePacked)

    packed = handlePacked.product()

    event.getByLabel (labelPruned, handlePruned)

    pruned = handlePruned.product()

    nleptons = 0
    
    n_gen_leptons = 0
    n_gen_photons = 0
    gen_lepton_indexes = []
    gen_photon_indexes = []
    for i, p in enumerate(packed):
        if p.pt() > 20 and p.status() == 1 and (abs(p.pdgId()) == 11 or abs(p.pdgId()) == 13) and (p.statusFlags().isPrompt() or p.statusFlags().isDirectPromptTauDecayProduct()) and (p.statusFlags().fromHardProcess() or p.statusFlags().isDirectHardProcessTauDecayProduct()) and abs(p.eta()) < 2.5:
            gen_lepton_indexes.append(i)
            n_gen_leptons += 1

        if p.pt() > 20 and p.status() == 1 and p.pdgId() == 22 and (p.statusFlags().isPrompt() or p.statusFlags().isDirectPromptTauDecayProduct()) and abs(p.eta()) < 2.5:
            gen_photon_indexes.append(i)
            n_gen_photons += 1
            
    if n_gen_leptons == 1 and n_gen_photons == 1:
        gen_lepton_index = gen_lepton_indexes[0]
        gen_photon_index = gen_photon_indexes[0]
        if deltaR(packed[gen_lepton_index].eta(),packed[gen_lepton_index].phi(),packed[gen_photon_index].eta(),packed[gen_photon_index].phi()) > 0.7:
            if gen.weight() > 0:
                h_photon_pt.Fill(packed[gen_photon_index].pt())
            else:
                h_photon_pt.Fill(packed[gen_photon_index].pt(),-1)  

h_photon_pt.Scale(xs*1000*lumi/countweighted)

h_photon_pt.SetMinimum(0)

h_photon_pt.SetMaximum(0.14)

print "h_photon_pt.GetBinContent(1) = "+str(h_photon_pt.GetBinContent(1))
print "h_photon_pt.GetBinError(1) = "+str(h_photon_pt.GetBinError(1))

c=ROOT.TCanvas()

h_photon_pt.Draw()

c.SaveAs("/eos/user/a/amlevin/www/tmp/delete_this.png")
