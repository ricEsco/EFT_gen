import ROOT

ROOT.gROOT.SetBatch(True)

Infilename  = "/nfs/dust/cms/user/ricardo/EFT/CMSSW_10_6_26/src/EFT_gen/EFT_samples/nanogen_folder/condor/output/nanogen_ALL_histograms.root"
Outfilename = "/nfs/dust/cms/user/ricardo/EFT/CMSSW_10_6_26/src/EFT_gen/EFT_samples/nanogen_folder/condor/output/EFTnanogenplots_withratio.root"

file1       = ROOT.TFile.Open(Infilename, "READ")
output_file = ROOT.TFile.Open(Outfilename, "RECREATE")

print "Input files:", Infilename
print "Output file is:", Outfilename

histograms_to_overlay = [
    ('h_ttbarMass', 'h_ttbarMass_weight_ctu1'),
    ('h_ttbarMass', 'h_ttbarMass_weight_cQj11'),
    ('h_ttbarMass', 'h_ttbarMass_weight_ctu1_quad'),
    ('h_ttbarMass', 'h_ttbarMass_weight_cQj11_quad'),

    ('h_Deta', 'h_Deta_weight_ctu1'),
    ('h_Deta', 'h_Deta_weight_cQj11'),
    ('h_Deta', 'h_Deta_weight_ctu1_quad'),
    ('h_Deta', 'h_Deta_weight_cQj11_quad'),

    ('h_had_b_4vec_pt',   'h_had_b_4vec_pt_weight_ctu1'),
    ('h_had_b_4vec_pt',   'h_had_b_4vec_pt_weight_cQj11'),
    ('h_had_b_4vec_pt',   'h_had_b_4vec_pt_weight_ctu1_quad'),
    ('h_had_b_4vec_pt',   'h_had_b_4vec_pt_weight_cQj11_quad'),

    ('h_had_b_4vec_eta',  'h_had_b_4vec_eta_weight_ctu1'),
    ('h_had_b_4vec_eta',  'h_had_b_4vec_eta_weight_cQj11'),
    ('h_had_b_4vec_eta',  'h_had_b_4vec_eta_weight_ctu1_quad'),
    ('h_had_b_4vec_eta',  'h_had_b_4vec_eta_weight_cQj11_quad'),

    ('h_had_b_4vec_phi',  'h_had_b_4vec_phi_weight_ctu1'),
    ('h_had_b_4vec_phi',  'h_had_b_4vec_phi_weight_cQj11'),
    ('h_had_b_4vec_phi',  'h_had_b_4vec_phi_weight_ctu1_quad'),
    ('h_had_b_4vec_phi',  'h_had_b_4vec_phi_weight_cQj11_quad'),

    ('h_lepton_pt',       'h_lepton_pt_weight_ctu1'),
    ('h_lepton_pt',       'h_lepton_pt_weight_cQj11'),
    ('h_lepton_pt',       'h_lepton_pt_weight_ctu1_quad'),
    ('h_lepton_pt',       'h_lepton_pt_weight_cQj11_quad'),

    ('h_lepton_eta',      'h_lepton_eta_weight_ctu1'),
    ('h_lepton_eta',      'h_lepton_eta_weight_cQj11'),
    ('h_lepton_eta',      'h_lepton_eta_weight_ctu1_quad'),
    ('h_lepton_eta',      'h_lepton_eta_weight_cQj11_quad'),

    ('h_lepton_phi',      'h_lepton_phi_weight_ctu1'),
    ('h_lepton_phi',      'h_lepton_phi_weight_cQj11'),
    ('h_lepton_phi',      'h_lepton_phi_weight_ctu1_quad'),
    ('h_lepton_phi',      'h_lepton_phi_weight_cQj11_quad'),

    ('h_Sphi', 'h_Sphi_weight_ctu1'),
    ('h_Sphi', 'h_Sphi_weight_cQj11'),
    ('h_Sphi', 'h_Sphi_weight_ctu1_quad'),
    ('h_Sphi', 'h_Sphi_weight_cQj11_quad'),

    ('h_Dphi', 'h_Dphi_weight_ctu1'),
    ('h_Dphi', 'h_Dphi_weight_cQj11'),
    ('h_Dphi', 'h_Dphi_weight_ctu1_quad'),
    ('h_Dphi', 'h_Dphi_weight_cQj11_quad'),

    ('h_xi_kk', 'h_xi_kk_weight_ctu1'),
    ('h_xi_kk', 'h_xi_kk_weight_cQj11'),
    ('h_xi_kk', 'h_xi_kk_weight_ctu1_quad'),
    ('h_xi_kk', 'h_xi_kk_weight_cQj11_quad'),

]

for hist_names in histograms_to_overlay:

    hist1 = file1.Get(hist_names[0]) #EFT SM
    hist2 = file1.Get(hist_names[1]) #EFT c*

    c = ROOT.TCanvas("c", "Canvas with Ratio", 800, 800)
    
    pad1 = ROOT.TPad("pad1", "The pad with the histogram", 0,  0.3, 1, 1.0)
    pad2 = ROOT.TPad("pad2", "The pad with the ratio"    , 0, 0.05, 1, 0.3)
    pad1.SetBottomMargin(0) 
    pad2.SetTopMargin(0)  
    pad2.SetBottomMargin(0.33)

    pad1.Draw()
    pad2.Draw()
  
    # # Normalizing histograms
    # if hist1.Integral() > 0:
    #     hist1.Scale(1.0 / hist1.Integral())
    # if hist2.Integral() > 0:
    #     hist2.Scale(1.0 / hist2.Integral())
        
    hist1.SetLineColor(ROOT.kRed)
    hist1.GetYaxis().SetTitleOffset(0.3)
    hist2.SetLineColor(ROOT.kGreen-2)
    
    hist1.SetLineWidth(2)
    hist2.SetLineWidth(2)    
    
    pad1.cd()
    hist1.Draw("hist")
    hist2.Draw("hist same")

    ROOT.gStyle.SetOptStat("iorm")
    st = hist1.FindObject("stats")
    st.SetX1NDC(0.75)
    st.SetX2NDC(0.90)
    st.SetY1NDC(0.70)
    st.SetY2NDC(0.80)

    if "phi" in hist_names[0]:
        hist1.SetMinimum(hist1.GetMinimum()*0.8)
        hist1.SetMaximum(hist1.GetMaximum()*1.2)
    else:
        pad1.SetLogy()

    # Syntax for TLegend: x1, y1, x2, y2
    legend = ROOT.TLegend(0.75, 0.80, 0.90, 0.90)
    legend.AddEntry(hist1, "SM")
    if "ctu1" in hist_names[1]:
        if "quad" in hist_names[1]:
            legend.AddEntry(hist2, "EFT: ctu1 (quad)")
        else:
            legend.AddEntry(hist2, "EFT: ctu1")
    elif "cQj11" in hist_names[1]:
        if "quad" in hist_names[1]:
            legend.AddEntry(hist2, "EFT: cQj11 (quad)")
        else:
            legend.AddEntry(hist2, "EFT: cQj11")
    legend.Draw()
    
    pad2.cd()
    # ROOT.gStyle.SetOptStat("0")

    ratio = hist1.Clone("ratio")
    ratio.Divide(hist2)
    ratio.SetLineColor(ROOT.kBlack)
    ratio.SetLineWidth(1)
    ratio.SetMinimum(0.5) 
    ratio.SetMaximum(1.5)
    ratio.GetYaxis().SetTitle("SM/EFT") 
    ratio.GetYaxis().SetTitleSize(0.1) 
    ratio.GetYaxis().SetTitleOffset(0.3)
    ratio.GetYaxis().SetLabelSize(0.05) 
    ratio.GetYaxis().CenterTitle(True)
    ratio.GetYaxis().SetNdivisions(505)
    ratio.SetTitle("")
    
    ratio.GetXaxis().SetTitleSize(0.12)  
    ratio.GetXaxis().SetTitleOffset(1.0) 
    ratio.GetXaxis().SetLabelSize(0.1) 

    ratio.Draw("hist")
    # Disable statistics box only for ratio plot
    ratio.SetStats(0)
    
    # ROOT TLine syntax: x1, y1, x2, y2
    line = ROOT.TLine(ratio.GetXaxis().GetXmin(), 1, ratio.GetXaxis().GetXmax(), 1)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineStyle(2)
    line.Draw("same")
    
    c.Update()
    c.SaveAs("outputPlots/{}_EFTcomparison.png".format(hist_names[1]))
    
    
    
for hist_names in histograms_to_overlay:
    
    hist1 = file1.Get(hist_names[0])
    hist1_clone = hist1.Clone(hist_names[0])
    hist1_clone.Write() 
    
    hist2 = file1.Get(hist_names[1])
    hist2_clone = hist2.Clone(hist_names[1])  
    hist2_clone.Write() 
    

file1.Close()
output_file.Close()
