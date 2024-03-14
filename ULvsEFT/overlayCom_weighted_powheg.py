import ROOT

ROOT.gROOT.SetBatch(True)

# file1 = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/EFT/CMSSW_10_6_26/src/EFT_gen_old/EFT_samples/nanogen_folder/condor/output_EFT_weights/output_lhescale.root", "READ")
file2 = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/EFT/CMSSW_10_6_26/src/EFT_gen_old/UL_beforentuple/nano/condor/plots/output_latest.root", "READ")
file1 = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/EFT/CMSSW_10_6_26/src/EFT_gen_old/EFT_samples/nanogen_folder/condor/envelope_output.root", "READ")

output_file = ROOT.TFile.Open("output_madgraphVSpowheg.root", "RECREATE")


histograms_to_overlay = [
    ('h_leptonPt', 'h_leptonPt_scale_Down', 'h_leptonPt_ctGRe'),
    ('h_leptoneta', 'h_leptoneta_scale_Down', 'h_leptoneta_ctGRe'),
    ('h_electronPt', 'h_electronPt_scale_Down', 'h_electronPt_ctGRe'),
    ('h_electroneta', 'h_electroneta_scale_Down', 'h_electroneta_ctGRe'),
    ('h_muonPt', 'h_muonPt_scale_Down', 'h_muonPt_ctGRe'),
    ('h_muoneta', 'h_muoneta_scale_Down', 'h_muoneta_ctGRe'),
    ('h_topPt', 'h_topPt_scale_Down', 'h_topPt_ctGRe'),
    ('h_topEta', 'h_topEta_scale_Down', 'h_topEta_ctGRe'),
    ('h_antitopPt', 'h_antitopPt_scale_Down', 'h_antitopPt_ctGRe'),
    ('h_antitopEta', 'h_antitopEta_scale_Down', 'h_antitopEta_ctGRe'),
    ('h_invariantMass', 'h_invariantMass_scale_Down', 'h_invariantMass_ctGRe'),
    # ('h_LHE_HT', 'h_LHE_HT_scale_Down', 'h_LHE_HT_ctGRe'),
    # ('h_LHE_HT_0_500', 'h_LHE_HT_0_500_scale_Down', 'h_LHE_HT_0_500_ctGRe'),
    # ('h_LHE_HT_500_750', 'h_LHE_HT_500_750_scale_Down', 'h_LHE_HT_500_750_ctGRe'),
    # ('h_LHE_HT_750_1000', 'h_LHE_HT_750_1000_scale_Down', 'h_LHE_HT_750_1000_ctGRe'),
    # ('h_LHE_HT_1000_1500', 'h_LHE_HT_1000_1500_scale_Down', 'h_LHE_HT_1000_1500_ctGRe'),
    # ('h_LHE_HT_1500Inf', 'h_LHE_HT_1500Inf_scale_Down', 'h_LHE_HT_1500Inf_ctGRe'),
    ('h_leading_jet_pt', 'h_leading_jet_pt_scale_Down', 'h_leading_jet_pt_ctGRe'),
    ('h_second_leading_jet_pt', 'h_second_leading_jet_pt_scale_Down', 'h_second_leading_jet_pt_ctGRe'),
    # ('h_jet_multiplicity_last_copy', 'h_jet_multiplicity_last_copy_scale_Down', 'h_jet_multiplicity_last_copy_ctGRe'),
    # ("h_jet_multiplicity_hardprocess", "h_jet_multiplicity_hardprocess_scale_Down", "h_jet_multiplicity_hardprocess_ctGRe"),
    # ("h_jet_multiplicity_ishardprocess", "h_jet_multiplicity_ishardprocess_scale_Down", "h_jet_multiplicity_ishardprocess_ctGRe"),
    # ('h_mtt_vs_LHEHT', 'h_mtt_vs_LHEHT_scale_Down', 'h_mtt_vs_LHEHT_ctGRe'),
    # ('h_bquark_pt', 'h_bquark_pt_scale_Down', 'h_bquark_pt_ctGRe'),
    # ('h_bquark_eta', 'h_bquark_eta_scale_Down', 'h_bquark_eta_ctGRe'),
]

pastelRed = ROOT.TColor.GetColor("#FFA07A")  # Pastel red (Light Salmon)
pastelGreen = ROOT.TColor.GetColor("#98FB98")  # Pastel green (Pale Green)
pastelBlue = ROOT.TColor.GetColor("#ADD8E6")  # Pastel blue (Light Blue)
pastelPurple = ROOT.TColor.GetColor("#DDA0DD")  # Pastel purple (Plum)
pastelYellow = ROOT.TColor.GetColor("#FFFACD")  # Pastel yellow (Lemon Chiffon)
pastelCyan = ROOT.TColor.GetColor("#E0FFFF")  # Pastel cyan (Light Cyan)

for hist_names in histograms_to_overlay:

    hist1 = file1.Get(hist_names[1])
    hist2 = file2.Get(hist_names[0])
    
    
    if hist1.Integral() > 0:
        hist1.Scale(1.0 / hist1.Integral())
    if hist2.Integral() > 0:
        hist2.Scale(1.0 / hist2.Integral())

    hist1.SetLineColor(ROOT.kRed)
    hist2.SetLineColor(ROOT.kGreen-2)
    
    # hist1.SetLineWidth(3)
    # hist2.SetLineWidth(3)

    c = ROOT.TCanvas("c", "canvas", 800, 600)
    c.SetLogy(1) 
    ROOT.gStyle.SetOptStat("iorme")
    
    pad1 = ROOT.TPad("pad1", "The upper pad", 0, 0.3, 1, 1.0)
    pad1.SetLogy(1)
    pad1.SetBottomMargin(0) 
    pad1.Draw()  

    pad2 = ROOT.TPad("pad2", "The lower pad", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0)  
    pad2.SetBottomMargin(0.33)
    pad2.Draw()
    
    pad1.cd()
    hist1.Draw("hist")
    hist2.Draw("histsame")
    
    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.AddEntry(hist1, "Madgraph EFT, SM")
    legend.AddEntry(hist2, "Powheg UL18")
    legend.Draw()
    
    pad2.cd()
    ROOT.gStyle.SetOptStat("0")

    
    ratio = hist1.Clone("ratio")
    ratio.Divide(hist2)
    ratio.SetLineColor(ROOT.kBlack)
    ratio.SetMinimum(0.0) 
    ratio.SetMaximum(2.0)
    ratio.GetYaxis().SetTitle("Madgraph SM / Powheg") 
    ratio.GetYaxis().SetTitleSize(0.1) 
    ratio.GetYaxis().SetTitleOffset(0.5)
    ratio.GetYaxis().SetLabelSize(0.05) 
    ratio.GetYaxis().CenterTitle(True)
    ratio.SetTitle("")
    
    ratio.GetXaxis().SetTitleSize(0.12)  
    ratio.GetXaxis().SetTitleOffset(1.0) 
    ratio.GetXaxis().SetLabelSize(0.1) 

    ratio.Draw("ep")
    
    line = ROOT.TLine(ratio.GetXaxis().GetXmin(), 1, ratio.GetXaxis().GetXmax(), 1)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineStyle(2)
    line.Draw("same")


    c.SaveAs("{}.pdf".format(hist_names[0]))
    
    
    
for hist_names in histograms_to_overlay:
    
    hist1 = file1.Get(hist_names[1])
    hist1_clone = hist1.Clone(hist_names[1])
    hist1_clone.Write() 
    
    hist2 = file1.Get(hist_names[2])
    hist2_clone = hist2.Clone(hist_names[2])  
    hist2_clone.Write() 
    

file1.Close()
output_file.Close()
