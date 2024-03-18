import ROOT

ROOT.gROOT.SetBatch(True)

file1 = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/EFT/CMSSW_10_6_26/src/EFT_gen_old/EFT_samples/nanogen_folder/condor/output_weights_NoNu_latest/output_EFT.root", "READ")
file2 = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/EFT/CMSSW_10_6_26/src/EFT_gen_old/UL_beforentuple/nano/condor/plots/output_latest.root", "READ")
file3 = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/EFT/CMSSW_10_6_26/src/EFT_gen_old/ULvsEFT/envelope_output.root", "READ")

output_file = ROOT.TFile.Open("output_madgraphVSpowheg.root", "RECREATE")

histograms_to_overlay = [
    ('h_leptonPt', 'h_leptonPt_weightSM', 'h_leptonPt_ctGRe', "h_leptonPt_scale"),
    ('h_leptoneta', 'h_leptoneta_weightSM', 'h_leptoneta_ctGRe', "h_leptonEta_scale"),
    ('h_electronPt', 'h_electronPt_weightSM', 'h_electronPt_ctGRe', 'h_electronPt_scale'),
    ('h_electroneta', 'h_electroneta_weightSM', 'h_electroneta_ctGRe', 'h_electronEta_scale'),
    ('h_muonPt', 'h_muonPt_weightSM', 'h_muonPt_ctGRe', 'h_muonPt_scale'),
    ('h_muoneta', 'h_muoneta_weightSM', 'h_muoneta_ctGRe', 'h_muonEta_scale'),
    ('h_topPt', 'h_topPt_weightSM', 'h_topPt_ctGRe','h_topPt_scale' ),
    ('h_topEta', 'h_topEta_weightSM', 'h_topEta_ctGRe', 'h_topEta_scale'),
    ('h_antitopPt', 'h_antitopPt_weightSM', 'h_antitopPt_ctGRe', 'h_antitopPt_scale'),
    ('h_antitopEta', 'h_antitopEta_weightSM', 'h_antitopEta_ctGRe', 'h_antitopEta_scale'),
    ('h_invariantMass', 'h_invariantMass_weightSM', 'h_invariantMass_ctGRe', 'h_invariantMass_scale'),
    ('h_leading_jet_pt', 'h_leading_jet_pt_weightSM', 'h_leading_jet_pt_ctGRe', 'h_leading_jet_pt_scale'),
    ('h_second_leading_jet_pt', 'h_second_leading_jet_pt_weightSM', 'h_second_leading_jet_pt_ctGRe', 'h_second_leading_jet_pt_scale'),
    ('h_jet_multiplicity_last_copy', 'h_jet_multiplicity_last_copy_weightSM', 'h_jet_multiplicity_last_copy_ctGRe', 'h_jet_multiplicity_last_copy_scale'),
    ("h_jet_multiplicity_ishardprocess", "h_jet_multiplicity_ishardprocess_weightSM", "h_jet_multiplicity_ishardprocess_ctGRe", 'h_jet_multiplicity_ishardprocess_scale'),
    # ("h_jet_multiplicity_hardprocess", "h_jet_multiplicity_hardprocess_weightSM", "h_jet_multiplicity_hardprocess_ctGRe"),
    # ('h_mtt_vs_LHEHT', 'h_mtt_vs_LHEHT_weightSM', 'h_mtt_vs_LHEHT_ctGRe'),
    # ('h_bquark_pt', 'h_bquark_pt_weightSM', 'h_bquark_pt_ctGRe'),
    # ('h_bquark_eta', 'h_bquark_eta_weightSM', 'h_bquark_eta_ctGRe'),
    # ('h_LHE_HT', 'h_LHE_HT_weightSM', 'h_LHE_HT_ctGRe'),
    # ('h_LHE_HT_0_500', 'h_LHE_HT_0_500_weightSM', 'h_LHE_HT_0_500_ctGRe'),
    # ('h_LHE_HT_500_750', 'h_LHE_HT_500_750_weightSM', 'h_LHE_HT_500_750_ctGRe'),
    # ('h_LHE_HT_750_1000', 'h_LHE_HT_750_1000_weightSM', 'h_LHE_HT_750_1000_ctGRe'),
    # ('h_LHE_HT_1000_1500', 'h_LHE_HT_1000_1500_weightSM', 'h_LHE_HT_1000_1500_ctGRe'),
    # ('h_LHE_HT_1500Inf', 'h_LHE_HT_1500Inf_weightSM', 'h_LHE_HT_1500Inf_ctGRe'),
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
    
    name_Up = hist_names[3] + "_Up"
    name_Down = hist_names[3] + "_Down"
    
    print(name_Up)
    
    histUp = file3.Get(hist_names[3] + "_Up")  
    histDown = file3.Get(hist_names[3] + "_Down")
    
    
    # if hist1.Integral() > 0:
    #     hist1.Scale(1.0 / hist1.Integral())
    # if hist2.Integral() > 0:
    #     hist2.Scale(1.0 / hist2.Integral())

    hist1.SetLineColor(ROOT.kRed)
    hist2.SetLineColor(ROOT.kGreen-2)
    
    # hist1.SetLineWidth(3)
    # hist2.SetLineWidth(3)    
    
    c = ROOT.TCanvas("c", "canvas", 800, 600)
    c.SetLogy(1) 
    ROOT.gStyle.SetOptStat("iorme")
    pad1 = ROOT.TPad("pad1", "The upper pad", 0, 0.3, 1, 1.0)
    pad2 = ROOT.TPad("pad2", "The lower pad", 0, 0.05, 1, 0.3)
    pad1.Draw()
    pad2.Draw()

    pad1.cd()
    hist1.Draw("hist")
    hist2.Draw("histsame")
    
    pad1.SetLogy(1)
    pad1.SetBottomMargin(0) 

    pad2.SetTopMargin(0)  
    pad2.SetBottomMargin(0.33)

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
    
    
    
    pad2.cd()

    n = ratio.GetNbinsX()
    sysBand = ROOT.TGraphAsymmErrors(n)
    for i in range(1, n+1):
        x = ratio.GetBinCenter(i)
        y = ratio.GetBinContent(i)  # nominal ratio: EFT/Powheg

        # percentage differences for up and down variations relative to the nominal EFT
        if hist1.GetBinContent(i) > 0:
            upPercentage = (histUp.GetBinContent(i) - hist1.GetBinContent(i)) / hist1.GetBinContent(i)
            downPercentage = (hist1.GetBinContent(i) - histDown.GetBinContent(i)) / hist1.GetBinContent(i)
        else:
            upPercentage = downPercentage = 0

        # apply percentages to the ratio value
        errUp = y * upPercentage
        errDown = y * downPercentage
         
        print("ErrUp:", errUp, "ErrDown:", errDown)

        sysBand.SetPoint(i-1, x, y)
        sysBand.SetPointError(i-1, 0.0, 0.0, abs(errDown), abs(errUp)) 

    pad2.cd()
    ratio.GetYaxis().SetRangeUser(0, 2);
    if sysBand.GetN() > 0:
        sysBand.Draw("2")
        ratio.Draw("EP same")
        line.Draw("same")
        pad2.Update()
    else:
        print("Systematic band is empty or not visible.")

    c.SaveAs("output_madgraphVSpowheg_weighted.pdf")
    
    
    
for hist_names in histograms_to_overlay:
    
    hist1 = file1.Get(hist_names[1])
    hist1_clone = hist1.Clone(hist_names[1])
    hist1_clone.Write() 
    
    hist2 = file1.Get(hist_names[2])
    hist2_clone = hist2.Clone(hist_names[2])  
    hist2_clone.Write() 
    

file1.Close()
file2.Close()
file3.Close()
output_file.Close()
