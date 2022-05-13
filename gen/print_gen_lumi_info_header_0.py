import DataFormats.FWLite as fwlite

filename = "root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/120000/1655BE04-FA8A-DC44-A1B4-AE9D27AB3467.root"

lumis = fwlite.Lumis(filename)
handle = fwlite.Handle("GenLumiInfoHeader")
lumis.getByLabel("generator", handle)
genlumi = handle.product()
print("Length of weight names is",len(genlumi.weightNames()))
for i in range(len(genlumi.weightNames())):
    print(i,genlumi.weightNames()[i])
