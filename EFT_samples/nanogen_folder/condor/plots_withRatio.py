import ROOT

ROOT.gROOT.SetBatch(True)

Infilename  = "/nfs/dust/cms/user/ricardo/EFT/CMSSW_10_6_26/src/EFT_gen/EFT_samples/nanogen_folder/condor/output/nanogen_123_ALL_histograms.root"
Outfilename = "/nfs/dust/cms/user/ricardo/EFT/CMSSW_10_6_26/src/EFT_gen/EFT_samples/nanogen_folder/condor/output/output_overlaidplots.root"

file1       = ROOT.TFile.Open(Infilename, "READ")
output_file = ROOT.TFile.Open(Outfilename, "RECREATE")

print "Input files:", Infilename
print "Output file is:", Outfilename

histograms_to_overlay = [
    ('h_had_b_4vec_pt',   'h_had_b_4vec_pt_weight_ctu1'),
    ('h_had_b_4vec_eta',  'h_had_b_4vec_eta_weight_ctu1'),
    ('h_had_b_4vec_phi',  'h_had_b_4vec_phi_weight_ctu1'),
]
pastelRed    = ROOT.TColor.GetColor("#FFA07A")  # Pastel red (Light Salmon)
pastelGreen  = ROOT.TColor.GetColor("#98FB98")  # Pastel green (Pale Green)
pastelBlue   = ROOT.TColor.GetColor("#ADD8E6")  # Pastel blue (Light Blue)
pastelPurple = ROOT.TColor.GetColor("#DDA0DD")  # Pastel purple (Plum)
pastelYellow = ROOT.TColor.GetColor("#FFFACD")  # Pastel yellow (Lemon Chiffon)
pastelCyan   = ROOT.TColor.GetColor("#E0FFFF")  # Pastel cyan (Light Cyan)

for hist_names in histograms_to_overlay:

    hist1 = file1.Get(hist_names[0]) #EFT SM
    hist2 = file1.Get(hist_names[1]) #EFT c*

    c = ROOT.TCanvas("c", "Canvas with Ratio", 800, 800)
    
    pad1 = ROOT.TPad("pad1", "The pad with the histogram", 0,  0.3, 1, 1.0)
    pad2 = ROOT.TPad("pad2", "The pad with the ratio"    , 0, 0.05, 1, 0.3)
    pad1.SetLogy()
    pad1.SetBottomMargin(0) 
    pad2.SetTopMargin(0)  
    pad2.SetBottomMargin(0.33)

    pad1.Draw()
    pad2.Draw()
    
    ROOT.gStyle.SetOptStat("iorme")
  
    # Normalizing histograms
    # if hist1.Integral() > 0:
    #     hist1.Scale(1.0 / hist1.Integral())
    # if hist2.Integral() > 0:
    #     hist2.Scale(1.0 / hist2.Integral())
        
    hist1.SetLineColor(ROOT.kRed)
    hist2.SetLineColor(ROOT.kGreen-2)
    
    # hist1.SetLineWidth(3)
    # hist2.SetLineWidth(3)    
    
    pad1.cd()
    hist1.Draw("hist")
    hist2.Draw("histsame")

    # Syntax for legend: x1, y1, x2, y2
    legend = ROOT.TLegend(0.75, 0.8, 0.9, 0.9)
    legend.AddEntry(hist1, "EFT SM")
    legend.AddEntry(hist2, "EFT ctu1")

    legend.Draw()
    
    pad2.cd()
    ROOT.gStyle.SetOptStat("0")
    
    ratio = hist1.Clone("ratio")
    ratio.Divide(hist2)
    ratio.SetLineColor(ROOT.kBlack)
    ratio.SetMinimum(0.8) 
    ratio.SetMaximum(1.2)
    ratio.GetYaxis().SetTitle("SM/ctu1") 
    ratio.GetYaxis().SetTitleSize(0.1) 
    ratio.GetYaxis().SetTitleOffset(0.5)
    ratio.GetYaxis().SetLabelSize(0.05) 
    ratio.GetYaxis().CenterTitle(True)
    ratio.GetYaxis().SetNdivisions(505)
    ratio.SetTitle("")
    
    ratio.GetXaxis().SetTitleSize(0.12)  
    ratio.GetXaxis().SetTitleOffset(1.0) 
    ratio.GetXaxis().SetLabelSize(0.1) 

    ratio.Draw("hist")
    
    # ROOT TLine syntax: x1, y1, x2, y2
    line = ROOT.TLine(ratio.GetXaxis().GetXmin(), 1, ratio.GetXaxis().GetXmax(), 1)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineStyle(2)
    line.Draw("same")
    
    c.Update()

    c.SaveAs("{}_EFTcomparison.png".format(hist_names[0]))
    
    
    
for hist_names in histograms_to_overlay:
    
    hist1 = file1.Get(hist_names[0])
    hist1_clone = hist1.Clone(hist_names[0])
    hist1_clone.Write() 
    
    hist2 = file1.Get(hist_names[1])
    hist2_clone = hist2.Clone(hist_names[1])  
    hist2_clone.Write() 
    

file1.Close()
# file2.Close()
output_file.Close()
