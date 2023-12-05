import ROOT

file = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/EFT/CMSSW_10_6_27/src/EFT_gen_old/EFT_samples/nanogen_folder/condor/plots_all/hadd_all/output.root") 

h_before = file.Get("h_LHE_HT_before")
h_muon_after_jet = file.Get("h_muon_LHE_HT_after_jet_cut")
# h_muon_before = file.Get("h_muon_LHE_HT_before")
h_muon_after_lepton = file.Get("h_muon_LHE_HT_after_lepton_cut")
h_muon_after_met = file.Get("h_muon_LHE_HT_after_met_cut")
h_muon_after_pt200 = file.Get("h_muon_LHE_HT_after_toppt200_cut")
h_muon_after_pt400 = file.Get("h_muon_LHE_HT_after_toppt400_cut")

h_cutflow = ROOT.TH1F("h_cutflow", "Cut Flow; Cut; Number of Events", 6, 0, 6)

cut_names = ["Before Cuts", "Jet Pt", "Lepton Pt", "MET", "TopPt>200", "TopPt>400"]
for i, name in enumerate(cut_names, start=1):
    h_cutflow.GetXaxis().SetBinLabel(i, name)

h_cutflow.SetBinContent(1, h_before.GetEntries())
h_cutflow.SetBinContent(2, h_muon_after_jet.GetEntries())
# h_cutflow.SetBinContent(3, h_muon_before.GetEntries())
h_cutflow.SetBinContent(3, h_muon_after_lepton.GetEntries())
h_cutflow.SetBinContent(4, h_muon_after_met.GetEntries())
h_cutflow.SetBinContent(5, h_muon_after_pt200.GetEntries())
h_cutflow.SetBinContent(6, h_muon_after_pt400.GetEntries())

c = ROOT.TCanvas("c", "Cutflow Plot", 800, 600)
c.SetLogy()
h_cutflow.SetFillColor(ROOT.kBlue)
h_cutflow.SetLineColor(ROOT.kBlack)
h_cutflow.Draw("hist")

c.SaveAs("cutflow_stairs_plot_muon2.png")

file.Close()

