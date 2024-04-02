# -*- coding: utf-8 -*-
import ROOT
import os
from array import array
import sys
from DataFormats.FWLite import Events, Handle
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.Config as edm
from XRootD import client
from XRootD.client.flags import DirListFlags, StatInfoFlags, OpenFlags, QueryCode

# Enable ROOT's batch mode to prevent graphics from opening for every plot
ROOT.gROOT.SetBatch(True)

# Set output directory
output_dir = "/nfs/dust/cms/user/ricardo/EFT/CMSSW_10_6_26/src/EFT_gen/EFT_samples/nanogen_folder/condor/output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

## Initializing Histograms -*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------*
# ROOT histogram constructor syntax: ROOT.TH1F("name", "title; x-axis title; y-axis title", n_bins, x_min, x_max)

# bin edges for leptonFlavor histogram
bin_edges = [-16.5, -14.5, -12.5, -10.5, 10.5, 12.5, 14.5, 16.5]
# nominal
h_leptonPt = ROOT.TH1F("h_leptonPt", "Lepton pT ; pT (GeV);Events", 25, 0, 500)
h_leptoneta = ROOT.TH1F("h_leptoneta", "Lepton Eta ; #eta;Events", 100, -5, 5)
h_leptonphi = ROOT.TH1F("h_leptonphi", "Azimuthal Angle ; #phi;Events", 100, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_leptonFlavor = ROOT.TH1F("h_leptonFlavor", "Lepton Flavor; PDG ID;Events", len(bin_edges)-1, array('d', bin_edges))
h_leptonFlavor.GetXaxis().SetBinLabel(1, "muon-")
h_leptonFlavor.GetXaxis().SetBinLabel(2, "electron-")
h_leptonFlavor.GetXaxis().SetBinLabel(4, "electron+")
h_leptonFlavor.GetXaxis().SetBinLabel(5, "muon+")
h_electronPt = ROOT.TH1F("h_electronPt", "Electron pT ; pT (GeV);Events", 25, 0, 500)
h_electroneta = ROOT.TH1F("h_electroneta", "Electron #eta ; #eta;Events", 100, -5, 5)
h_muonPt = ROOT.TH1F("h_muonPt", "Muon pT ; pT (GeV);Events", 25, 0, 500)
h_muoneta = ROOT.TH1F("h_muoneta", " Muon #eta ; #eta;Events", 100, -5, 5)
h_hadronic_w_mass = ROOT.TH1F("h_hadronic_w_mass", "Hadronic Decaying W Mass ; M (GeV);Events", 10, 60, 100)
h_topPt = ROOT.TH1F("h_topPt", "Top Quark pT ; pT (GeV);Events", 100, 0, 2000)
h_topEta = ROOT.TH1F("h_topEta", "Top Quark #eta ;#eta;Events", 100, -5, 5)
h_antitopPt = ROOT.TH1F("h_antitopPt", "Anti-Top Quark p_{T} ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta = ROOT.TH1F("h_antitopEta", "Anti-Top Quark #eta ;#eta;Events", 100, -5, 5)
h_bquark_pt = ROOT.TH1F("h_bquark_pt", "b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_bquark_eta = ROOT.TH1F("h_bquark_eta", "b-quark #eta  ;#eta;Events", 100, -5, 5)
h_had_b_4vec_pt = ROOT.TH1F("h_had_b_4vec_pt", "Hadronic b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_had_b_4vec_eta = ROOT.TH1F("h_had_b_4vec_eta", "Hadronic b-quark #eta  ;#eta;Events", 100, -5, 5)
h_had_b_4vec_phi = ROOT.TH1F("h_had_b_4vec_phi", "Hadronic b-quark #phi  ;#phi;Events", 100, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass = ROOT.TH1F("h_had_b_4vec_mass", "Hadronic b-quark Mass  ;Mass;Events", 50, 0, 10)
h_topMultiplicity = ROOT.TH1F("h_topMultiplicity", "Top Multiplicity ; N_{top};Events", 5, 0, 5)
h_antitopMultiplicity = ROOT.TH1F("h_antitopMultiplicity", "Anti-Top Multiplicity ; N_{antitop};Events", 5, 0, 5)
h_jetMultiplicity_fromW = ROOT.TH1F("h_jetMultiplicity_fromW", "Jet Multiplicity from W ; Number of Jets; Events", 10, 0, 5)
h_invariantMass = ROOT.TH1F("h_invariantMass", "Invariant Mass; M (GeV);Events", 250, 0, 5000)
h_jetMultiplicity = ROOT.TH1F("h_jetMultiplicity Without Cuts", "Number of Jets per Event", 10, 0, 50)
h_jet_multiplicity_last_copy = ROOT.TH1F('h_jet_multiplicity_last_copy', 'Jet Multiplicity Last Copy;Number of Jets;Events', 10, 0, 10)
h_nonTopMotherJets = ROOT.TH1F("h_nonTopMotherJets", "Jets without Top as Mother; Count;Events", 10, 0, 50)
h_LHE_HT = ROOT.TH1F("h_LHE_HT", "LHE_HT ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_0_500 = ROOT.TH1F("h_LHE_HT_0_500", "LHE_HT Mtt = [0,500] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_500_750 = ROOT.TH1F("h_LHE_HT_500_750", "LHE_HT Mtt = [500,750] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_750_1000 = ROOT.TH1F("h_LHE_HT_750_1000", "LHE_HT Mtt = [750,1000] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_1000_1500 = ROOT.TH1F("h_LHE_HT_1000_1500", "LHE_HT Mtt = [1000,1500] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_1500Inf = ROOT.TH1F("h_LHE_HT_1500Inf", "LHE_HT Mtt = [1500,Inf) ; HT (GeV); Events", 150, 0, 3000)
h_both_decays = ROOT.TH1F("h_both_decays", "Events with Both Leptonic and Hadronic Decays; Number of Events; Count", 2, 0, 2)
h_jetFromW_pt = ROOT.TH1F("h_jetFromW_pt", "Jet pT from W ; pT (GeV);Events", 1000, 0, 1000)
h_jetFromW_eta = ROOT.TH1F("h_jetFromW_eta", "Jet Eta from W ; #eta;Events", 100, -5, 5)
h_leading_jet_pt = ROOT.TH1F("h_leading_jet_pt", "Leading Jet pT; pT (GeV);Events", 100, 0, 1000)
h_second_leading_jet_pt = ROOT.TH1F("h_second_leading_jet_pt", "Second Leading Jet pT; pT (GeV);Events", 100, 0, 1000)
h_mtt_vs_LHEHT = ROOT.TH2F("h_mtt_vs_LHEHT", "Invariant Mass of ttbar vs. LHE HT;LHE HT (GeV);m_{tt} (GeV)", 50, 0, 1000, 50, 300, 5000)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# (ren scfact 0.5, fac scfact 0.5) variations
h_leptonPt_scale_0 = ROOT.TH1F("h_leptonPt_scale_0", "Lepton pT MUF=0.5 MUR=0.5 ; pT (GeV);Events", 25, 0, 500)
h_leptonEta_scale_0 = ROOT.TH1F("h_leptonEta_scale_0", "Lepton Eta MUF=0.5 MUR=0.5 ; #eta;Events", 100, -5, 5)
h_electronPt_scale_0 = ROOT.TH1F("h_electronPt_scale_0", "Electron pT MUF=0.5 MUR=0.5; pT (GeV);Events", 25, 0, 500)
h_electronEta_scale_0 = ROOT.TH1F("h_electronEta_scale_0", "Electron #eta MUF=0.5 MUR=0.5; #eta;Events", 100, -5, 5)
h_muonPt_scale_0 = ROOT.TH1F("h_muonPt_scale_0", "Muon pT MUF=0.5 MUR=0.5; pT (GeV);Events", 25, 0, 500)
h_muonEta_scale_0 = ROOT.TH1F("h_muonEta_scale_0", " Muon #eta MUF=0.5 MUR=0.5 ; #eta;Events", 100, -5, 5)
h_topPt_scale_0 = ROOT.TH1F("h_topPt_scale_0", "Top Quark pT MUF=0.5 MUR=0.5; pT (GeV);Events", 100, 0, 2000)
h_topEta_scale_0 = ROOT.TH1F("h_topEta_scale_0", "Top Quark #eta MUF=0.5 MUR=0.5 ;#eta;Events", 100, -5, 5)
h_antitopPt_scale_0 = ROOT.TH1F("h_antitopPt_scale_0", "Anti-Top Quark p_{T} MUF=0.5 MUR=0.5 ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta_scale_0 = ROOT.TH1F("h_antitopEta_scale_0", "Anti-Top Quark #eta MUF=0.5 MUR=0.5 ;#eta;Events", 100, -5, 5)
h_invariantMass_scale_0 = ROOT.TH1F("h_invariantMass_scale_0", "Invariant Mass MUF=0.5 MUR=0.5; M (GeV);Events", 250, 0, 5000)
h_leading_jet_pt_scale_0 = ROOT.TH1F("h_leading_jet_pt_scale_0", "Leading Jet pT MUF=0.5 MUR=0.5; pT (GeV);Events", 100, 0, 1000)
h_second_leading_jet_pt_scale_0 = ROOT.TH1F("h_second_leading_jet_pt_scale_0", "Second Leading Jet pT MUF=0.5 MUR=0.5; pT (GeV);Events", 100, 0, 1000)
h_jet_multiplicity_last_copy_scale_0 = ROOT.TH1F('h_jet_multiplicity_last_copy_scale_0', 'Jet Multiplicity Last Copy MUF=0.5 MUR=0.5;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_ishardprocess_scale_0 = ROOT.TH1F('h_jet_multiplicity_ishardprocess_scale_0', 'Jet Multiplicity isHardProcess MUF=0.5 MUR=0.5 ;Number of Jets;Events', 10, 0, 10)
# (ren scfact 0.5, fac scfact 1.0) variations
h_leptonPt_scale_1 = ROOT.TH1F("h_leptonPt_scale_1", "Lepton pT MUF=1.0 MUR=0.5 ; pT (GeV);Events", 25, 0, 500)
h_leptonEta_scale_1 = ROOT.TH1F("h_leptonEta_scale_1", "Lepton Eta MUF=1.0 MUR=0.5 ; #eta;Events", 100, -5, 5)
h_electronPt_scale_1 = ROOT.TH1F("h_electronPt_scale_1", "Electron pT MUF=1.0 MUR=0.5; pT (GeV);Events", 25, 0, 500)
h_electronEta_scale_1 = ROOT.TH1F("h_electronEta_scale_1", "Electron #eta MUF=1.0 MUR=0.5; #eta;Events", 100, -5, 5)
h_muonPt_scale_1 = ROOT.TH1F("h_muonPt_scale_1", "Muon pT MUF=1.0 MUR=0.5; pT (GeV);Events", 25, 0, 500)
h_muonEta_scale_1 = ROOT.TH1F("h_muonEta_scale_1", " Muon #eta MUF=1.0 MUR=0.5 ; #eta;Events", 100, -5, 5)
h_topPt_scale_1 = ROOT.TH1F("h_topPt_scale_1", "Top Quark pT MUF=1.0 MUR=0.5; pT (GeV);Events", 100, 0, 2000)
h_topEta_scale_1 = ROOT.TH1F("h_topEta_scale_1", "Top Quark #eta MUF=1.0 MUR=0.5 ;#eta;Events", 100, -5, 5)
h_antitopPt_scale_1 = ROOT.TH1F("h_antitopPt_scale_1", "Anti-Top Quark p_{T} MUF=1.0 MUR=0.5 ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta_scale_1 = ROOT.TH1F("h_antitopEta_scale_1", "Anti-Top Quark #eta MUF=1.0 MUR=0.5 ;#eta;Events", 100, -5, 5)
h_invariantMass_scale_1 = ROOT.TH1F("h_invariantMass_scale_1", "Invariant Mass MUF=1.0 MUR=0.5; M (GeV);Events", 250, 0, 5000)
h_leading_jet_pt_scale_1 = ROOT.TH1F("h_leading_jet_pt_scale_1", "Leading Jet pT MUF=1.0 MUR=0.5; pT (GeV);Events", 100, 0, 1000)
h_second_leading_jet_pt_scale_1 = ROOT.TH1F("h_second_leading_jet_pt_scale_1", "Second Leading Jet pT MUF=1.0 MUR=0.5; pT (GeV);Events", 100, 0, 1000)
h_jet_multiplicity_last_copy_scale_1 = ROOT.TH1F('h_jet_multiplicity_last_copy_scale_1', 'Jet Multiplicity Last Copy MUF=1.0 MUR=0.5;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_ishardprocess_scale_1 = ROOT.TH1F('h_jet_multiplicity_ishardprocess_scale_1', 'Jet Multiplicity isHardProcess MUF=1.0 MUR=0.5 ;Number of Jets;Events', 10, 0, 10)
# (ren scfact 1.0, fac scfact 0.5) variations
h_leptonPt_scale_3 = ROOT.TH1F("h_leptonPt_scale_3", "Lepton pT MUF=0.5 MUR=1.0 ; pT (GeV);Events", 25, 0, 500)
h_leptonEta_scale_3 = ROOT.TH1F("h_leptonEta_scale_3", "Lepton Eta MUF=0.5 MUR=1.0 ; #eta;Events", 100, -5, 5)
h_electronPt_scale_3 = ROOT.TH1F("h_electronPt_scale_3", "Electron pT MUF=0.5 MUR=1.0; pT (GeV);Events", 25, 0, 500)
h_electronEta_scale_3 = ROOT.TH1F("h_electronEta_scale_3", "Electron #eta MUF=0.5 MUR=1.0; #eta;Events", 100, -5, 5)
h_muonPt_scale_3 = ROOT.TH1F("h_muonPt_scale_3", "Muon pT MUF=0.5 MUR=1.0; pT (GeV);Events", 25, 0, 500)
h_muonEta_scale_3 = ROOT.TH1F("h_muonEta_scale_3", " Muon #eta MUF=0.5 MUR=1.0 ; #eta;Events", 100, -5, 5)
h_topPt_scale_3 = ROOT.TH1F("h_topPt_scale_3", "Top Quark pT MUF=0.5 MUR=1.0; pT (GeV);Events", 100, 0, 2000)
h_topEta_scale_3 = ROOT.TH1F("h_topEta_scale_3", "Top Quark #eta MUF=0.5 MUR=1.0 ;#eta;Events", 100, -5, 5)
h_antitopPt_scale_3 = ROOT.TH1F("h_antitopPt_scale_3", "Anti-Top Quark p_{T} MUF=0.5 MUR=1.0 ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta_scale_3 = ROOT.TH1F("h_antitopEta_scale_3", "Anti-Top Quark #eta MUF=0.5 MUR=1.0 ;#eta;Events", 100, -5, 5)
h_invariantMass_scale_3 = ROOT.TH1F("h_invariantMass_scale_3", "Invariant Mass MUF=0.5 MUR=1.0; M (GeV);Events", 250, 0, 5000)
h_leading_jet_pt_scale_3 = ROOT.TH1F("h_leading_jet_pt_scale_3", "Leading Jet pT MUF=0.5 MUR=1.0; pT (GeV);Events", 100, 0, 1000)
h_second_leading_jet_pt_scale_3 = ROOT.TH1F("h_second_leading_jet_pt_scale_3", "Second Leading Jet pT MUF=0.5 MUR=1.0; pT (GeV);Events", 100, 0, 1000)
h_jet_multiplicity_last_copy_scale_3 = ROOT.TH1F('h_jet_multiplicity_last_copy_scale_3', 'Jet Multiplicity Last Copy MUF=0.5 MUR=1.0;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_ishardprocess_scale_3 = ROOT.TH1F('h_jet_multiplicity_ishardprocess_scale_3', 'Jet Multiplicity isHardProcess MUF=0.5 MUR=1.0 ;Number of Jets;Events', 10, 0, 10)
# (ren scfact 1.0, fac scfact 1.0) variations
h_leptonPt_scale_4 = ROOT.TH1F("h_leptonPt_scale_4", "Lepton pT MUF=2.0 MUR=1.0 ; pT (GeV);Events", 25, 0, 500)
h_leptonEta_scale_4 = ROOT.TH1F("h_leptonEta_scale_4", "Lepton Eta MUF=2.0 MUR=1.0 ; #eta;Events", 100, -5, 5)
h_electronPt_scale_4 = ROOT.TH1F("h_electronPt_scale_4", "Electron pT MUF=2.0 MUR=1.0; pT (GeV);Events", 25, 0, 500)
h_electronEta_scale_4 = ROOT.TH1F("h_electronEta_scale_4", "Electron #eta MUF=2.0 MUR=1.0; #eta;Events", 100, -5, 5)
h_muonPt_scale_4 = ROOT.TH1F("h_muonPt_scale_4", "Muon pT MUF=2.0 MUR=1.0; pT (GeV);Events", 25, 0, 500)
h_muonEta_scale_4 = ROOT.TH1F("h_muonEta_scale_4", " Muon #eta MUF=2.0 MUR=1.0 ; #eta;Events", 100, -5, 5)
h_topPt_scale_4 = ROOT.TH1F("h_topPt_scale_4", "Top Quark pT MUF=2.0 MUR=1.0; pT (GeV);Events", 100, 0, 2000)
h_topEta_scale_4 = ROOT.TH1F("h_topEta_scale_4", "Top Quark #eta MUF=2.0 MUR=1.0 ;#eta;Events", 100, -5, 5)
h_antitopPt_scale_4 = ROOT.TH1F("h_antitopPt_scale_4", "Anti-Top Quark p_{T} MUF=2.0 MUR=1.0 ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta_scale_4 = ROOT.TH1F("h_antitopEta_scale_4", "Anti-Top Quark #eta MUF=2.0 MUR=1.0 ;#eta;Events", 100, -5, 5)
h_invariantMass_scale_4 = ROOT.TH1F("h_invariantMass_scale_4", "Invariant Mass MUF=2.0 MUR=1.0; M (GeV);Events", 250, 0, 5000)
h_leading_jet_pt_scale_4 = ROOT.TH1F("h_leading_jet_pt_scale_4", "Leading Jet pT MUF=2.0 MUR=1.0; pT (GeV);Events", 100, 0, 1000)
h_second_leading_jet_pt_scale_4 = ROOT.TH1F("h_second_leading_jet_pt_scale_4", "Second Leading Jet pT MUF=2.0 MUR=1.0; pT (GeV);Events", 100, 0, 1000)
h_jet_multiplicity_last_copy_scale_4 = ROOT.TH1F('h_jet_multiplicity_last_copy_scale_4', 'Jet Multiplicity Last Copy MUF=2.0 MUR=1.0;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_ishardprocess_scale_4 = ROOT.TH1F('h_jet_multiplicity_ishardprocess_scale_4', 'Jet Multiplicity isHardProcess MUF=2.0 MUR=1.0 ;Number of Jets;Events', 10, 0, 10)
# (ren scfact 2.0, fac scfact 1.0) variations
h_leptonPt_scale_6 = ROOT.TH1F("h_leptonPt_scale_6", "Lepton pT MUF=1.0 MUR=2.0 ; pT (GeV);Events", 25, 0, 500)
h_leptonEta_scale_6 = ROOT.TH1F("h_leptonEta_scale_6", "Lepton Eta MUF=1.0 MUR=2.0 ; #eta;Events", 100, -5, 5)
h_electronPt_scale_6 = ROOT.TH1F("h_electronPt_scale_6", "Electron pT MUF=1.0 MUR=2.0; pT (GeV);Events", 25, 0, 500)
h_electronEta_scale_6 = ROOT.TH1F("h_electronEta_scale_6", "Electron #eta MUF=1.0 MUR=2.0; #eta;Events", 100, -5, 5)
h_muonPt_scale_6 = ROOT.TH1F("h_muonPt_scale_6", "Muon pT MUF=1.0 MUR=2.0; pT (GeV);Events", 25, 0, 500)
h_muonEta_scale_6 = ROOT.TH1F("h_muonEta_scale_6", " Muon #eta MUF=1.0 MUR=2.0 ; #eta;Events", 100, -5, 5)
h_topPt_scale_6 = ROOT.TH1F("h_topPt_scale_6", "Top Quark pT MUF=1.0 MUR=2.0; pT (GeV);Events", 100, 0, 2000)
h_topEta_scale_6 = ROOT.TH1F("h_topEta_scale_6", "Top Quark #eta MUF=1.0 MUR=2.0 ;#eta;Events", 100, -5, 5)
h_antitopPt_scale_6 = ROOT.TH1F("h_antitopPt_scale_6", "Anti-Top Quark p_{T} MUF=1.0 MUR=2.0 ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta_scale_6 = ROOT.TH1F("h_antitopEta_scale_6", "Anti-Top Quark #eta MUF=1.0 MUR=2.0 ;#eta;Events", 100, -5, 5)
h_invariantMass_scale_6 = ROOT.TH1F("h_invariantMass_scale_6", "Invariant Mass MUF=1.0 MUR=2.0; M (GeV);Events", 250, 0, 5000)
h_leading_jet_pt_scale_6 = ROOT.TH1F("h_leading_jet_pt_scale_6", "Leading Jet pT MUF=1.0 MUR=2.0; pT (GeV);Events", 100, 0, 1000)
h_second_leading_jet_pt_scale_6 = ROOT.TH1F("h_second_leading_jet_pt_scale_6", "Second Leading Jet pT MUF=1.0 MUR=2.0; pT (GeV);Events", 100, 0, 1000)
h_jet_multiplicity_last_copy_scale_6 = ROOT.TH1F('h_jet_multiplicity_last_copy_scale_6', 'Jet Multiplicity Last Copy MUF=1.0 MUR=2.0;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_ishardprocess_scale_6 = ROOT.TH1F('h_jet_multiplicity_ishardprocess_scale_6', 'Jet Multiplicity isHardProcess MUF=1.0 MUR=2.0 ;Number of Jets;Events', 10, 0, 10)
# (ren scfact 2.0, fac scfact 1.0) variations
h_leptonPt_scale_7 = ROOT.TH1F("h_leptonPt_scale_7", "Lepton pT MUF=2.0 MUR=2.0 ; pT (GeV);Events", 25, 0, 500)
h_leptonEta_scale_7 = ROOT.TH1F("h_leptonEta_scale_7", "Lepton Eta MUF=2.0 MUR=2.0 ; #eta;Events", 100, -5, 5)
h_electronPt_scale_7 = ROOT.TH1F("h_electronPt_scale_7", "Electron pT MUF=2.0 MUR=2.0; pT (GeV);Events", 25, 0, 500)
h_electronEta_scale_7 = ROOT.TH1F("h_electronEta_scale_7", "Electron #eta MUF=2.0 MUR=2.0; #eta;Events", 100, -5, 5)
h_muonPt_scale_7 = ROOT.TH1F("h_muonPt_scale_7", "Muon pT MUF=2.0 MUR=2.0; pT (GeV);Events", 25, 0, 500)
h_muonEta_scale_7 = ROOT.TH1F("h_muonEta_scale_7", " Muon #eta MUF=2.0 MUR=2.0 ; #eta;Events", 100, -5, 5)
h_topPt_scale_7 = ROOT.TH1F("h_topPt_scale_7", "Top Quark pT MUF=2.0 MUR=2.0; pT (GeV);Events", 100, 0, 2000)
h_topEta_scale_7 = ROOT.TH1F("h_topEta_scale_7", "Top Quark #eta MUF=2.0 MUR=2.0 ;#eta;Events", 100, -5, 5)
h_antitopPt_scale_7 = ROOT.TH1F("h_antitopPt_scale_7", "Anti-Top Quark p_{T} MUF=2.0 MUR=2.0 ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta_scale_7 = ROOT.TH1F("h_antitopEta_scale_7", "Anti-Top Quark #eta MUF=2.0 MUR=2.0 ;#eta;Events", 100, -5, 5)
h_invariantMass_scale_7 = ROOT.TH1F("h_invariantMass_scale_7", "Invariant Mass MUF=2.0 MUR=2.0; M (GeV);Events", 250, 0, 5000)
h_leading_jet_pt_scale_7 = ROOT.TH1F("h_leading_jet_pt_scale_7", "Leading Jet pT MUF=2.0 MUR=2.0; pT (GeV);Events", 100, 0, 1000)
h_second_leading_jet_pt_scale_7 = ROOT.TH1F("h_second_leading_jet_pt_scale_7", "Second Leading Jet pT MUF=2.0 MUR=2.0; pT (GeV);Events", 100, 0, 1000)
h_jet_multiplicity_last_copy_scale_7 = ROOT.TH1F('h_jet_multiplicity_last_copy_scale_7', 'Jet Multiplicity Last Copy MUF=2.0 MUR=2.0;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_ishardprocess_scale_7 = ROOT.TH1F('h_jet_multiplicity_ishardprocess_scale_7', 'Jet Multiplicity isHardProcess MUF=2.0 MUR=2.0 ;Number of Jets;Events', 10, 0, 10)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# Standard Model (SM) weight: "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p"
h_leptonPt_weightSM = ROOT.TH1F("h_leptonPt_weightSM", "Lepton pT ; pT (GeV);Events", 25, 0, 500)
h_leptoneta_weightSM = ROOT.TH1F("h_leptoneta_weightSM", "Lepton Eta ; #eta;Events", 100, -5, 5)
h_leptonphi_weightSM = ROOT.TH1F("h_leptonphi_weightSM", "Azimuthal Angle ; #phi;Events", 100, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_leptonFlavor_weightSM = ROOT.TH1F("h_leptonFlavor_weightSM", "Lepton Flavor; PDG ID;Events", len(bin_edges)-1, array('d', bin_edges))
h_leptonFlavor_weightSM.GetXaxis().SetBinLabel(1, "muon-")
h_leptonFlavor_weightSM.GetXaxis().SetBinLabel(2, "electron-")
h_leptonFlavor_weightSM.GetXaxis().SetBinLabel(4, "electron+")
h_leptonFlavor_weightSM.GetXaxis().SetBinLabel(5, "muon+")
h_electronPt_weightSM = ROOT.TH1F("h_electronPt_weightSM", "Electron pT ; pT (GeV);Events", 25, 0, 500)
h_electroneta_weightSM = ROOT.TH1F("h_electroneta_weightSM", "Electron #eta ; #eta;Events", 100, -5, 5)
h_muonPt_weightSM = ROOT.TH1F("h_muonPt_weightSM", "Muon pT ; pT (GeV);Events", 25, 0, 500)
h_muoneta_weightSM = ROOT.TH1F("h_muoneta_weightSM", " Muon #eta ; #eta;Events", 100, -5, 5)
h_hadronic_w_mass_weightSM = ROOT.TH1F("h_hadronic_w_mass_weightSM", "Hadronic Decaying W Mass ; M (GeV);Events", 10, 60, 100)
h_topPt_weightSM = ROOT.TH1F("h_topPt_weightSM", "Top Quark pT ; pT (GeV);Events", 100, 0, 2000)
h_topEta_weightSM = ROOT.TH1F("h_topEta_weightSM", "Top Quark #eta ;#eta;Events", 100, -5, 5)
h_antitopPt_weightSM = ROOT.TH1F("h_antitopPt_weightSM", "Anti-Top Quark p_{T} ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta_weightSM = ROOT.TH1F("h_antitopEta_weightSM", "Anti-Top Quark #eta ;#eta;Events", 100, -5, 5)
h_bquark_pt_weightSM = ROOT.TH1F("h_bquark_pt_weightSM", "b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_bquark_eta_weightSM = ROOT.TH1F("h_bquark_eta_weightSM", "b-quark #eta  ;#eta;Events", 100, -5, 5)
h_topMultiplicity_weightSM = ROOT.TH1F("h_topMultiplicit_weightSM", "Top Multiplicity ; N_{top};Events", 5, 0, 5)
h_antitopMultiplicity_weightSM = ROOT.TH1F("h_antitopMultiplicity_weightSM", "Anti-Top Multiplicity ; N_{antitop};Events", 5, 0, 5)
h_jetMultiplicity_fromW_weightSM = ROOT.TH1F("h_jetMultiplicity_fromW_weightSM", "Jet Multiplicity from W ; Number of Jets; Events", 10, 0, 5)
h_invariantMass_weightSM = ROOT.TH1F("h_invariantMass_weightSM", "Invariant Mass; M (GeV);Events", 250, 0, 5000)
h_jetMultiplicity_weightSM = ROOT.TH1F("h_jetMultiplicity_weightSM", "Number of Jets per Event", 10, 0, 50)
h_nonTopMotherJets_weightSM = ROOT.TH1F("h_nonTopMotherJets_weightSM", "Jets without Top as Mother; Count;Events", 10, 0, 50)
h_LHE_HT_weightSM = ROOT.TH1F("h_LHE_HT_weightSM", "LHE_HT ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_0_500_weightSM = ROOT.TH1F("h_LHE_HT_0_500_weightSM", "LHE_HT Mtt = [0,500] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_500_750_weightSM = ROOT.TH1F("h_LHE_HT_500_750_weightSM", "LHE_HT Mtt = [500,750] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_750_1000_weightSM = ROOT.TH1F("h_LHE_HT_750_1000_weightSM", "LHE_HT Mtt = [750,1000] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_1000_1500_weightSM = ROOT.TH1F("h_LHE_HT_1000_1500_weightSM", "LHE_HT Mtt = [1000,1500] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_1500Inf_weightSM = ROOT.TH1F("h_LHE_HT_1500Inf_weightSM", "LHE_HT Mtt = [1500,Inf) ; HT (GeV); Events", 150, 0, 3000)
h_both_decays_weightSM  = ROOT.TH1F("h_both_decays_weightSM", "Events with Both Leptonic and Hadronic Decays; Number of Events; Count", 2, 0, 2)
h_jetFromW_pt_weightSM  = ROOT.TH1F("h_jetFromW_pt_weightSM", "Jet pT from W ; pT (GeV);Events", 1000, 0, 1000)
h_jetFromW_eta_weightSM  = ROOT.TH1F("h_jetFromW_eta_weightSM", "Jet Eta from W ; #eta;Events", 100, -5, 5)
h_leading_jet_pt_weightSM  = ROOT.TH1F("h_leading_jet_pt_weightSM", "Leading Jet pT; pT (GeV);Events", 100, 0, 1000)
h_second_leading_jet_pt_weightSM  = ROOT.TH1F("h_second_leading_jet_pt_weightSM", "Second Leading Jet pT; pT (GeV);Events", 100, 0, 1000)
h_jet_multiplicity_last_copy_weightSM  = ROOT.TH1F('h_jet_multiplicity_last_copy_weightSM', 'Jet Multiplicity Last Copy;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_hardprocess_weightSM = ROOT.TH1F('h_jet_multiplicity_hardprocess_weightSM', 'Jet Multiplicity HardProcess before FSR;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_ishardprocess_weightSM = ROOT.TH1F('h_jet_multiplicity_ishardprocess_weightSM', 'Jet Multiplicity isHardProcess ;Number of Jets;Events', 10, 0, 10)
h_mtt_vs_LHEHT_weightSM  = ROOT.TH2F("h_mtt_vs_LHEHT_weightSM", "Invariant Mass of ttbar vs. LHE HT;LHE HT (GeV);m_{tt} (GeV)", 50, 0, 1000, 50, 300, 5000)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# EFT weight ctGRe: LHEWeight_ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p"
h_leptonPt_ctGRe = ROOT.TH1F("h_leptonPt_ctGRe", "Lepton pT ; pT (GeV);Events", 25, 0, 500)
h_leptoneta_ctGRe = ROOT.TH1F("h_leptoneta_ctGRe", "Lepton Eta ; #eta;Events", 100, -5, 5)
h_leptonphi_ctGRe = ROOT.TH1F("h_leptonphi_ctGRe", "Azimuthal Angle ; #phi;Events", 100, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_leptonFlavor_ctGRe = ROOT.TH1F("h_leptonFlavor_ctGRe", "Lepton Flavor; PDG ID;Events", len(bin_edges)-1, array('d', bin_edges))
h_leptonFlavor_ctGRe.GetXaxis().SetBinLabel(1, "muon-")
h_leptonFlavor_ctGRe.GetXaxis().SetBinLabel(2, "electron-")
h_leptonFlavor_ctGRe.GetXaxis().SetBinLabel(4, "electron+")
h_leptonFlavor_ctGRe.GetXaxis().SetBinLabel(5, "muon+")
h_electronPt_ctGRe = ROOT.TH1F("h_electronPt_ctGRe", "Electron pT ; pT (GeV);Events", 25, 0, 500)
h_electroneta_ctGRe = ROOT.TH1F("h_electroneta_ctGRe", "Electron #eta ; #eta;Events", 100, -5, 5)
h_muonPt_ctGRe = ROOT.TH1F("h_muonPt_ctGRe", "Muon pT ; pT (GeV);Events", 25, 0, 500)
h_muoneta_ctGRe = ROOT.TH1F("h_muoneta_ctGRe", " Muon #eta ; #eta;Events", 100, -5, 5)
h_hadronic_w_mass_ctGRe = ROOT.TH1F("h_hadronic_w_mass_ctGRe", "Hadronic Decaying W Mass ; M (GeV);Events", 10, 60, 100)
h_topPt_ctGRe = ROOT.TH1F("h_topPt_ctGRe", "Top Quark pT ; pT (GeV);Events", 100, 0, 2000)
h_topEta_ctGRe = ROOT.TH1F("h_topEta_ctGRe", "Top Quark #eta ;#eta;Events", 100, -5, 5)
h_antitopPt_ctGRe = ROOT.TH1F("h_antitopPt_ctGRe", "Anti-Top Quark p_{T} ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta_ctGRe = ROOT.TH1F("h_antitopEta_ctGRe", "Anti-Top Quark #eta ;#eta;Events", 100, -5, 5)
h_bquark_pt_ctGRe = ROOT.TH1F("h_bquark_pt_ctGRe", "b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_bquark_eta_ctGRe = ROOT.TH1F("h_bquark_eta_ctGRe", "b-quark #eta  ;#eta;Events", 100, -5, 5)
h_topMultiplicity_ctGRe = ROOT.TH1F("h_topMultiplicit_ctGRe", "Top Multiplicity ; N_{top};Events", 5, 0, 5)
h_antitopMultiplicity_ctGRe = ROOT.TH1F("h_antitopMultiplicity_ctGRe", "Anti-Top Multiplicity ; N_{antitop};Events", 5, 0, 5)
h_jetMultiplicity_fromW_ctGRe = ROOT.TH1F("h_jetMultiplicity_fromW_ctGRe", "Jet Multiplicity from W ; Number of Jets; Events", 10, 0, 5)
h_invariantMass_ctGRe = ROOT.TH1F("h_invariantMass_ctGRe", "Invariant Mass; M (GeV);Events", 250, 0, 5000)
h_jetMultiplicity_ctGRe = ROOT.TH1F("h_jetMultiplicity_ctGRe", "Number of Jets per Event", 10, 0, 50)
h_nonTopMotherJets_ctGRe = ROOT.TH1F("h_nonTopMotherJets_ctGRe", "Jets without Top as Mother; Count;Events", 10, 0, 50)
h_LHE_HT_ctGRe = ROOT.TH1F("h_LHE_HT_ctGRe", "LHE_HT ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_0_500_ctGRe = ROOT.TH1F("h_LHE_HT_0_500_ctGRe", "LHE_HT Mtt = [0,500] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_500_750_ctGRe = ROOT.TH1F("h_LHE_HT_500_750_ctGRe", "LHE_HT Mtt = [500,750] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_750_1000_ctGRe = ROOT.TH1F("h_LHE_HT_750_1000_ctGRe", "LHE_HT Mtt = [750,1000] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_1000_1500_ctGRe = ROOT.TH1F("h_LHE_HT_1000_1500_ctGRe", "LHE_HT Mtt = [1000,1500] ; HT (GeV); Events", 150, 0, 3000)
h_LHE_HT_1500Inf_ctGRe = ROOT.TH1F("h_LHE_HT_1500Inf_ctGRe", "LHE_HT Mtt = [1500,Inf) ; HT (GeV); Events", 150, 0, 3000)
h_both_decays_ctGRe  = ROOT.TH1F("h_both_decays_ctGRe", "Events with Both Leptonic and Hadronic Decays; Number of Events; Count", 2, 0, 2)
h_jetFromW_pt_ctGRe  = ROOT.TH1F("h_jetFromW_pt_ctGRe", "Jet pT from W ; pT (GeV);Events", 1000, 0, 1000)
h_jetFromW_eta_ctGRe  = ROOT.TH1F("h_jetFromW_eta_ctGRe", "Jet Eta from W ; #eta;Events", 100, -5, 5)
h_leading_jet_pt_ctGRe  = ROOT.TH1F("h_leading_jet_pt_ctGRe", "Leading Jet pT; pT (GeV);Events", 100, 0, 1000)
h_second_leading_jet_pt_ctGRe  = ROOT.TH1F("h_second_leading_jet_pt_ctGRe", "Second Leading Jet pT; pT (GeV);Events", 100, 0, 1000)
h_jet_multiplicity_last_copy_ctGRe  = ROOT.TH1F('h_jet_multiplicity_last_copy_ctGRe', 'Jet Multiplicity Last Copy;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_hardprocess_ctGRe = ROOT.TH1F('h_jet_multiplicity_hardprocess_ctGRe', 'Jet Multiplicity HardProcess before FSR;Number of Jets;Events', 10, 0, 10)
h_jet_multiplicity_ishardprocess_ctGRe = ROOT.TH1F('h_jet_multiplicity_ishardprocess_ctGRe', 'Jet Multiplicity isHardProcess ;Number of Jets;Events', 10, 0, 10)
h_mtt_vs_LHEHT_ctGRe  = ROOT.TH2F("h_mtt_vs_LHEHT_ctGRe", "Invariant Mass of ttbar vs. LHE HT;LHE HT (GeV);m_{tt} (GeV)", 50, 0, 1000, 50, 300, 5000)
h_pdgId_last_copy = ROOT.TH1F('h_pdgId_last_copy', 'PDG ID Last Copy',  51, -25.5, 25.5)
h_pdgId_first_copy = ROOT.TH1F('h_pdgId_first_copy', 'PDG ID First Copy', 51, -25.5, 25.5)
h_pdgId_ishardprocess = ROOT.TH1F('h_pdgId_ishardprocess', 'PDG ID isHardProcess', 51, -25.5, 25.5)
h_pdgId_fromhardprocess = ROOT.TH1F('h_pdgId_fromhardprocess', 'PDG ID fromHardProcess', 51, -25.5, 25.5)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# LHE weight ctu1
h_had_b_4vec_pt_weight_ctu1  = ROOT.TH1F("h_had_b_4vec_pt_weight_ctu1", "Hadronic b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_had_b_4vec_eta_weight_ctu1 = ROOT.TH1F("h_had_b_4vec_eta_weight_ctu1", "Hadronic b-quark #eta  ;#eta;Events", 100, -5, 5)
h_had_b_4vec_phi_weight_ctu1 = ROOT.TH1F("h_had_b_4vec_phi_weight_ctu1", "Hadronic b-quark #phi  ;#phi;Events", 100, -ROOT.TMath.Pi(), ROOT.TMath.Pi())

#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

## Define useful functions -*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------*

# Calculate deltaR distance between two particles
# Input eta and phi of two particles
def deltaR(eta1, phi1, eta2, phi2):
    deta = eta1 - eta2
    dphi = abs(phi1 - phi2)
    if dphi > ROOT.TMath.Pi():
        dphi = 2 * ROOT.TMath.Pi() - dphi
    return (deta * deta + dphi * dphi) ** 0.5        

# LHE HT cut
def passes_selection_HT(entry):
    LHE_HT = getattr(entry, "LHE_HT", -1)         
    if LHE_HT < 800:
        return False
    return True

# Functions checking status flags of particles
#FLAGS = ['isPrompt', 'isDecayedLeptonHadron', 'isTauDecayProduct', 'isPromptTauDecayProduct', 'isDirectTauDecayProduct', 
#         'isDirectPromptTauDecayProduct', 'isDirectHadronDecayProduct', 'isHardProcess', 'fromHardProcess', 'isHardProcessTauDecayProduct', 
#         'isDirectHardProcessTauDecayProduct', 'fromHardProcessBeforeFSR', 'isFirstCopy', 'isLastCopy', 'isLastCopyBeforeFSR']
#
# statusFlags is a 16-bit integer, where each bit indicates a specific flag
# the expression (statusFlags & (1 << n)) != 0 checks if the nth bit is set to 1
def is_last_copy(statusFlags):
    try:
        status_flags_int = int(statusFlags)
        return (status_flags_int & (1 << 13)) != 0 # (1 << n) indicates (n+1)th element in the list
    except ValueError:
        return False
    
def is_first_copy(statusFlags):
    try:
        status_flags_int = int(statusFlags)
        return (status_flags_int & (1 << 12)) != 0
    except ValueError:
        return False

def ishardprocess(statusFlags):
    try:
        status_flags_int = int(statusFlags)
        return (status_flags_int & (1 << 7)) != 0
    except ValueError:
        return False
    
def fromHardProcess(statusFlags):
    try:
        status_flags_int = int(statusFlags)
        return (status_flags_int & (1 << 11)) != 0
    except ValueError:
        return False
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------*-----------------------------------------------------------------------------------------#
    
### Start main loop over the events
def process_event(entry, histograms, relevant_pdgIds):
    # Initialize variables
    top_count, antitop_count = 0, 0
    jets_from_w_count = 0
    tops = []
    b_quarks = []
    w_bosons = []
    hadronic_top_pt = []
    last_copy_decays = []
    jets_from_w, jets_from_w_info = [], []
    last_copy_top_decays, last_copy_partons = [], []
    first_copy_partons = []
    ishard_process = []
    fromHardProcess_jets = []
    leptons = []
    w_quarks1, w_quarks2, w_quarks_indices = [], [], []
    met_vector = ROOT.TLorentzVector()
    had_b_4vec = ROOT.TLorentzVector()
    jets =[]
    top_4vec = None
    antitop_4vec = None
    top_related_parton_indices = set()
    lhe_weight_0 = array('f', [0])  # for SM LHEWeight_ctGRe_0p...
    lhe_weight_1 = array('f', [0])  # for LHEWeight_ctGRe_1p...

    # Standard Model weight
    weight_0 = getattr(entry, "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")

    ## Linear EFT weights
    # EFT weight for ctGRe linear
    weight_1 = getattr(entry, "LHEWeight_ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")
    # EFT weight for ctu1 linear
    weight_ctu1 = getattr(entry, "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")
    # EFT weight for cQj11 linear
    weight_cQj11 = getattr(entry, "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")

    ## Quadratic EFT weights
    # EFT weight for ctu1 quadratic
    weight_ctu1_quad = getattr(entry, "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_2p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")
    # EFT weight for cQj11 quadratic
    weight_cQj11_quad = getattr(entry, "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_2p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")

    # print("SM weight: ", weight_0)
    # print("ctGRe weight: ", weight_1) 

    # LHE Q2 scale weights
    lheScaleWeights = getattr(entry,"LHEScaleWeight")
    # combine EFT weight with Q2 scale weights
    scale_weight_0 = lheScaleWeights[0] * weight_1 # ren scfact 0.5, fac scfact 0.5
    scale_weight_1 = lheScaleWeights[1] * weight_1 # ren scfact 0.5, fac scfact 1.0
    scale_weight_3 = lheScaleWeights[3] * weight_1 # ren scfact 1.0, fac scfact 0.5
    scale_weight_4 = lheScaleWeights[4] * weight_1 # ren scfact 1.0, fac scfact 1.0
    scale_weight_6 = lheScaleWeights[6] * weight_1 # ren scfact 2.0, fac scfact 1.0
    scale_weight_7 = lheScaleWeights[7] * weight_1 # ren scfact 2.0, fac scfact 1.0

    # processing particless ------------------------------------------------------------------------------------------------------------------------------------------------------*
    # Loop over all particles in the event
    for i in range(entry.nGenPart):
        # Get ith-particle properties
        pdgId = entry.GenPart_pdgId[i]
        pt = entry.GenPart_pt[i]
        eta = entry.GenPart_eta[i]
        phi = entry.GenPart_phi[i]
        mass = entry.GenPart_mass[i]
        mother_idx = entry.GenPart_genPartIdxMother[i]
        status = entry.GenPart_status[i]
        statusFlags = entry.GenPart_statusFlags[i]

        # Check particle's statusFlag
        if is_last_copy(statusFlags):
            parton_4vec = ROOT.TLorentzVector()
            parton_4vec.SetPtEtaPhiM(pt, eta, phi, mass)
            last_copy_partons.append((parton_4vec, i)) 
        
        if is_first_copy(statusFlags):
            parton_4vec = ROOT.TLorentzVector()
            parton_4vec.SetPtEtaPhiM(pt, eta, phi, mass)
            first_copy_partons.append((parton_4vec, i)) 
        
        if ishardprocess(statusFlags):
            parton_4vec = ROOT.TLorentzVector()
            parton_4vec.SetPtEtaPhiM(pt, eta, phi, mass)
            # if abs(pdgId) in (1,2,3,4,5,21):
            ishard_process.append((parton_4vec, entry.GenPart_pdgId[i])) 
        
        if fromHardProcess(statusFlags): 
            parton_4vec = ROOT.TLorentzVector()
            parton_4vec.SetPtEtaPhiM(pt, eta, phi, mass)
            # if abs(pdgId) in (1,2,3,4,5,21): 
            fromHardProcess_jets.append((parton_4vec, i))
        
        # Check for last copy of relevant particle ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*
        if abs(pdgId) in relevant_pdgIds and is_last_copy(statusFlags):  # relevant pdgIDs = {12, 14, 16, 24, 1, 2, 3, 4, 5, 6, 21, 11, 13, 15}
            # Check if particle is a top or antitop quark
            if abs(pdgId) == 6:
                top_related_parton_indices.add(i)
                w_daughter = None
                b_daughter = None
                last_copy_top_decays.append((pdgId))
                has_leptonic_w_decay = False
                has_hadronic_w_decay = False
                vec = ROOT.TLorentzVector()
                vec.SetPtEtaPhiM(entry.GenPart_pt[i], entry.GenPart_eta[i], entry.GenPart_phi[i], entry.GenPart_mass[i]) # <<<-* top quarks
                if pdgId == 6:
                    top_4vec = vec
                else:
                    antitop_4vec = vec
                tops.append((top_4vec, pdgId)) 
                
            # i is still the index of the top quark
                
                # Loop over all particles, again
                for j in range(entry.nGenPart):
                    # Check if Mother of jth-particle is the top quark found above ----------------------------------------------------------------------------------------------------------------------------------------------*
                    # and if the jth-particle is a W boson or a b-quark
                    if entry.GenPart_genPartIdxMother[j] == i and abs(entry.GenPart_pdgId[j]) in [24, 5]:
                        last_copy_decays.append((pt, eta, phi, pdgId, i)) # append as a tuple
                        top_related_parton_indices.add(j)
                        daughter_pdgId = entry.GenPart_pdgId[j]

                        # Double check that top quark mother really is last_copy << is this necessary? last_copy already checked above and if not satisfied, has_leptonic
                        if daughter_pdgId != 6 and daughter_pdgId != -6:

                    # j is still the index of the b quark

                            # Check if the daughter is a W boson -----------------------------------------------------------------------------------------------------------------------------------------------------------------*
                            if abs(daughter_pdgId) == 24:
                                w_daughter = j
                                w_4vec = ROOT.TLorentzVector()
                                w_4vec.SetPtEtaPhiM(entry.GenPart_pt[w_daughter], entry.GenPart_eta[w_daughter], entry.GenPart_phi[w_daughter], entry.GenPart_mass[w_daughter]) # <<<-*--* W bosons
                                w_bosons.append(w_4vec)
                                # Check if W decays leptonically or hadronically --------------------------------------------------------------------------------------------------------------------------------------------------*
                                # List comprehension syntax: ({expression} for {item} in {list} {if condition}) if condition is evaluated first to make the list, then elements of said list are evaluated by the expression
                                if any(abs(entry.GenPart_pdgId[k]) in [11, 13] for k in range(entry.nGenPart) if entry.GenPart_genPartIdxMother[k] == w_daughter):
                                    has_leptonic_w_decay = True
                                elif any(abs(entry.GenPart_pdgId[k]) in [1, 2, 3, 4] for k in range(entry.nGenPart) if entry.GenPart_genPartIdxMother[k] == w_daughter):
                                    has_hadronic_w_decay = True
                            # Check if the daughter is a b-quark -----------------------------------------------------------------------------------------------------------------------------------------------------------------*
                            elif abs(daughter_pdgId) == 5:
                                b_daughter = j
                                b_4vec = ROOT.TLorentzVector() 
                                b_4vec.SetPtEtaPhiM(entry.GenPart_pt[b_daughter], entry.GenPart_eta[b_daughter], entry.GenPart_phi[b_daughter], entry.GenPart_mass[b_daughter]) # <<<-*--*---* b-quarks
                                b_quarks.append((b_4vec, entry.GenPart_pdgId[j]))
                                # had_b_quark = False # <<<-*--*---*-----*--------* new code
                                # for m in range(entry.nGenPart):
                                #     if entry.GenPart_genPartIdxMother[m] == i and abs(entry.GenPart_pdgId[m]) == 24:

                                #         for l in range(entry.nGenPart):
                                #             if entry.GenPart_genPartIdxMother[l] == m and abs(entry.GenPart_pdgId[l]) in [1, 2, 3, 4]:
                                #                 had_b_quark = True
                                #                 break      
         
                # For leptonically decaying top quarks -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------*
                if has_leptonic_w_decay:

                    # Loop over all particles, again again
                    for k in range(entry.nGenPart):

                        # Check if Mother of kth-particle is the W boson found above ---------------------------------------------------------------------------------------------------------------------------------------------*
                        if entry.GenPart_genPartIdxMother[k] == w_daughter:
                            top_related_parton_indices.add(k)

                            # Check if the kth-particle is an electron or muon ---------------------------------------------------------------------------------------------------------------------------------------*
                            if abs(entry.GenPart_pdgId[k]) in [11, 13]:  
                                lepton_pdg = entry.GenPart_pdgId[k]
                                lepton_pt = entry.GenPart_pt[k]
                                lepton_eta = entry.GenPart_eta[k]
                                lepton_phi = entry.GenPart_phi[k]
                                leptons.append((lepton_pt, lepton_eta, lepton_phi, lepton_pdg)) # <<<-*--*---*-----* leptons
                                leptonic_decay = True
                                if abs(lepton_pdg) == 11:
                                    electron_found = True
                                elif abs(lepton_pdg) == 13:
                                    muon_found = True      
                            else: 
                                continue # skip tau decays

                        # Check if the kth-particle is an electron or muon or tau neutrino ---------------------------------------------------------------------------------------------------------------------------------------*
                        if abs(pdgId) in [12, 14, 16]:  
                            neutrino = ROOT.TLorentzVector()
                            neutrino.SetPtEtaPhiM(pt, eta, phi, mass) # <<<-*--*---*-----*--------* neutrinos
                            met_vector += neutrino

                # For hadronically decaying top quarks -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------*
                if has_hadronic_w_decay:  

                    # Loop over all particles, again again again
                    for j in range(entry.nGenPart):
                        if entry.GenPart_genPartIdxMother[j] == w_daughter and abs(entry.GenPart_pdgId[j]) in [1, 2, 3, 4]:
                            w_quarks_indices.append(j)
                            top_related_parton_indices.add(j)

                    # Now that we know this top (with index i) has decayed hadronically, we know its b quark daughter is the hadronic b quark
                    for m in range(entry.nGenPart):
                        if entry.GenPart_genPartIdxMother[m] == i and abs(entry.GenPart_pdgId[m]) == 5:
                            had_b_4vec.SetPtEtaPhiM(entry.GenPart_pt[m], entry.GenPart_eta[m], entry.GenPart_phi[m], entry.GenPart_mass[m]) # <<<-*--*---* HADRONIC b-quark

                    # Check that W decays into exactly two quarks -------------------------------------------------------------------------------------------------------------------------------------------------------------------*
                    if len(w_quarks_indices) == 2:
                        hadronic_decay = True
                        hadronic_top_pt.append(pt)
                        quark1_vec = ROOT.TLorentzVector()
                        quark2_vec = ROOT.TLorentzVector()
                        quark1_index, quark2_index = w_quarks_indices
                        quark1_vec.SetPtEtaPhiM(entry.GenPart_pt[quark1_index], entry.GenPart_eta[quark1_index], entry.GenPart_phi[quark1_index], entry.GenPart_mass[quark1_index]) # <<<-*--*---*-----*--------*-------------* quark1 from W-decay
                        quark2_vec.SetPtEtaPhiM(entry.GenPart_pt[quark2_index], entry.GenPart_eta[quark2_index], entry.GenPart_phi[quark2_index], entry.GenPart_mass[quark2_index]) # <<<-*--*---*-----*--------*-------------* quark2 from W-decay
                        w_quarks1.append((quark1_vec, entry.GenPart_pdgId[quark1_index]))
                        w_quarks2.append((quark2_vec, entry.GenPart_pdgId[quark2_index]))
                        hadronic_w_mass = (quark1_vec + quark2_vec).M()
                        if 65 < hadronic_w_mass < 95: # I include this line to ensure that the events are indeed hadronic W decays
                            histograms['h_hadronic_w_mass'].Fill(hadronic_w_mass)
                            histograms['h_hadronic_w_mass_weightSM'].Fill(hadronic_w_mass, weight_0)
                            histograms['h_hadronic_w_mass_ctGRe'].Fill(hadronic_w_mass, weight_1)
                            
            
                # b-quarks ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*
                if b_daughter is not None:
                    b_vector = ROOT.TLorentzVector()
                    b_vector.SetPtEtaPhiM(entry.GenPart_pt[b_daughter], entry.GenPart_eta[b_daughter], entry.GenPart_phi[b_daughter], entry.GenPart_mass[b_daughter])   
            
            else: 
                continue  
  
        else:
            continue
    ## Finished processing particles ---------------------------------------------------------------------------------------------------------------------------------------------*
        
    # print(last_copy_partons[1])

    # Fill histograms for particles with following properties
    # last_copy
    for _, pdgId in last_copy_partons:
        histograms['h_pdgId_last_copy'].Fill(pdgId) 
    # first_copy
    for _, pdgId in first_copy_partons:
        histograms['h_pdgId_first_copy'].Fill(pdgId) 
    # ishardprocess    
    for _,pdgId in ishard_process:
        histograms['h_pdgId_ishardprocess'].Fill(pdgId)
    # fromHardProcess
    for _,pdgId in fromHardProcess_jets:
        histograms['h_pdgId_fromhardprocess'].Fill(pdgId)
    
    # print("relevant_partons: ", len(relevant_partons))
    # print("matched_jets: ", len(matched_jets)) 
    # matches = one_to_one_matching(entry, b_quarks, w_quarks1, w_quarks2)

    ## processing jets -*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------*
    if len(w_quarks_indices) == 2 and len(b_quarks) == 2:
        
        # jet collection = jets
        jets = []
        for j in range(entry.nGenJet):
            jet_vec = ROOT.TLorentzVector()
            jet_vec.SetPtEtaPhiM(entry.GenJet_pt[j], entry.GenJet_eta[j], entry.GenJet_phi[j], 0)# <<<-*--*---*-----*--------*-------------*---------------------* jets
            jets.append((jet_vec, j))
        
        # list of pdgID's of all partons from top decay
        partons = b_quarks + w_quarks1 + w_quarks2 # list of tuples (parton_4vec, pdgId)
        
        # initializing containers for matched jets and partons
        matched_jets_indices = set()
        matched_partons_indices = set()
        matches = []

        # matching wquarks+bquarks from top decay with jets
        for jet_index, jet in enumerate(jets):
            closest_deltaR = float('inf')
            closest_parton_index = None
            closest_parton_pdgId = None
            # Collect all unmatched partons as tuples of (index, parton)
            unmatched_partons = [(idx, parton) for idx, parton in enumerate(partons) if idx not in matched_partons_indices]
            # Only consider partons that have yet to be matched
            if not unmatched_partons:
                continue
            # Calculate deltaR between the current jet and each unmatched parton
            # Then find the parton with the smallest deltaR, store the (deltaR, parton index, and parton pdgId)
            closest_deltaR, closest_parton_index, closest_parton_pdgId = min(((deltaR(jet[0].Eta(), jet[0].Phi(), parton[1][0].Eta(), parton[1][0].Phi()), parton[0], parton[1][1]) for parton in unmatched_partons), key=lambda x: x[0])
            # Closest parton must be within a cone of radius 0.4
            if closest_deltaR < 0.4:
                matched_jets_indices.add(jet_index) # stores the index of matched jet
                matched_partons_indices.add(closest_parton_index) # stores the index of matched parton
                matches.append((jet, (partons[closest_parton_index][0], closest_parton_pdgId))) # stores the matched jet and parton's pdgID

        # List comprehension syntax: ({expression} for {item} in {list} {if condition}) if condition is evaluated first to make the list, then elements of said list are evaluated by the expression

        # b quark matched jets
        b_quark_jets = [jet for jet, parton in matches if abs(parton[1]) == 5]
        # W boson quark matched jets
        jets_from_w = [jet for jet, parton in matches if abs(parton[1]) in [1, 2, 3, 4]]
        # Unique list of all jets from top decay
        combined_jets = list(set(b_quark_jets + jets_from_w))
    
        # matching partons in isHARDPROCESS with jets excluding ttbar jets
        additional_ishardprocess_jets = []
        matched_jets_indices_ishardprocess = set()
        matched_partons_indices_ishardprocess = set()
        for jet_index, jet in enumerate(jets):
            if jet_index not in matched_jets_indices: 
                closest_deltaR = float('inf')
                closest_parton_index = None
                closest_parton_pdgId = None
                unmatched_ishardprocess_partons = [(idx, parton) for idx, parton in enumerate(ishard_process) if idx not in matched_partons_indices_ishardprocess and idx not in top_related_parton_indices]

                if not unmatched_ishardprocess_partons:
                    continue
                
                closest_deltaR, closest_parton_index, closest_parton_pdgId = min(
                    ((deltaR(jet[0].Eta(), jet[0].Phi(), parton[0].Eta(), parton[0].Phi()), idx, parton[1]) for idx, parton in unmatched_ishardprocess_partons),
                    key=lambda x: x[0])
                
                if closest_deltaR < 0.4:
                    matched_jets_indices_ishardprocess.add(jet_index)
                    matched_partons_indices_ishardprocess.add(closest_parton_index)
                    additional_ishardprocess_jets.append((jet, ishard_process[closest_parton_index]))

                
        # checking if there is any overlap 
        jets_from_b_set = set(b_quark_jets)
        jets_from_w_set = set(jets_from_w)

        overlapping_jets = jets_from_b_set.intersection(jets_from_w_set)
        if len(overlapping_jets)>0:
            print "overlapping: ", len(overlapping_jets)

        
        # matching partons in fromHARDPROCESS with jets excluding ttbar jets
        additional_fromhardprocess_jets = []
        matched_jets_indices_fromhardprocess = set()
        matched_partons_indices_fromhardprocess = set()
        for jet_index, jet in enumerate(jets):
            if jet_index not in matched_jets_indices: 
                closest_deltaR = float('inf')
                closest_parton_index = None
                closest_parton_pdgId = None
                
                unmatched_fromhardprocess_partons = [(idx, parton) for idx, parton in enumerate(fromHardProcess_jets) if idx not in matched_partons_indices_fromhardprocess and idx not in top_related_parton_indices]

                if not unmatched_fromhardprocess_partons:
                    continue
                
                closest_deltaR, closest_parton_index, closest_parton_pdgId = min(
                    ((deltaR(jet[0].Eta(), jet[0].Phi(), parton[0].Eta(), parton[0].Phi()), idx, parton[1]) for idx, parton in unmatched_fromhardprocess_partons),
                    key=lambda x: x[0])
                
                if closest_deltaR < 0.4:
                    matched_jets_indices_fromhardprocess.add(jet_index)
                    matched_partons_indices_fromhardprocess.add(closest_parton_index)
                    additional_fromhardprocess_jets.append((jet, fromHardProcess_jets[closest_parton_index]))

        # last copy matching list
        combined_jets = len(list(set(b_quark_jets + jets_from_w)))
        
        # isHardProcess jet matching list
        total_jets_count = combined_jets + len([jet for jet, parton in additional_ishardprocess_jets if abs(parton[1]) in [1, 2, 3, 4, 5, 21]])
        
        # fromHardProcess jet matching list
        matched_quark_jets_hardprocess = combined_jets + len([jet for jet, parton in additional_fromhardprocess_jets if abs(parton[1]) in [1, 2, 3, 4, 5, 21]])
        
        ## Finished processing jets -*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------*

        # Filling histograms for jets
        histograms['h_jet_multiplicity_last_copy'].Fill(combined_jets)
        histograms['h_jet_multiplicity_last_copy_weightSM'].Fill(combined_jets, weight_0)
        histograms['h_jet_multiplicity_last_copy_ctGRe'].Fill(combined_jets, weight_1)
        
        histograms['h_jet_multiplicity_ishardprocess_weightSM'].Fill(total_jets_count, weight_0)  
        histograms['h_jet_multiplicity_ishardprocess_ctGRe'].Fill(total_jets_count, weight_1) 
            
        histograms['h_jet_multiplicity_hardprocess_weightSM'].Fill(matched_quark_jets_hardprocess, weight_0)  
        histograms['h_jet_multiplicity_hardprocess_ctGRe'].Fill(matched_quark_jets_hardprocess, weight_1) 
        
        histograms['h_jetMultiplicity'].Fill(entry.nGenJet)
        histograms['h_jetMultiplicity_weightSM'].Fill(entry.nGenJet, weight_0)
        histograms['h_jetMultiplicity_ctGRe'].Fill(entry.nGenJet, weight_1)
        
        histograms['h_jet_multiplicity_last_copy_scale_0'].Fill(combined_jets, scale_weight_0)
        histograms['h_jet_multiplicity_last_copy_scale_1'].Fill(combined_jets, scale_weight_1)
        histograms['h_jet_multiplicity_last_copy_scale_3'].Fill(combined_jets, scale_weight_3)
        histograms['h_jet_multiplicity_last_copy_scale_4'].Fill(combined_jets, scale_weight_4)
        histograms['h_jet_multiplicity_last_copy_scale_6'].Fill(combined_jets, scale_weight_6)
        histograms['h_jet_multiplicity_last_copy_scale_7'].Fill(combined_jets, scale_weight_7)
        
        histograms['h_jet_multiplicity_ishardprocess_scale_0'].Fill(total_jets_count, scale_weight_0)
        histograms['h_jet_multiplicity_ishardprocess_scale_1'].Fill(total_jets_count, scale_weight_1)
        histograms['h_jet_multiplicity_ishardprocess_scale_3'].Fill(total_jets_count, scale_weight_3)
        histograms['h_jet_multiplicity_ishardprocess_scale_4'].Fill(total_jets_count, scale_weight_4)
        histograms['h_jet_multiplicity_ishardprocess_scale_6'].Fill(total_jets_count, scale_weight_6)
        histograms['h_jet_multiplicity_ishardprocess_scale_7'].Fill(total_jets_count, scale_weight_7)

        # Fill histograms for hadronic b quarks
        histograms['h_had_b_4vec_pt'].Fill(had_b_4vec.Pt())
        histograms['h_had_b_4vec_eta'].Fill(had_b_4vec.Eta())
        histograms['h_had_b_4vec_phi'].Fill(had_b_4vec.Phi())
        histograms['h_had_b_4vec_mass'].Fill(had_b_4vec.M())

        histograms['h_had_b_4vec_pt_weight_ctu1'].Fill(had_b_4vec.Pt(), weight_ctu1)
        histograms['h_had_b_4vec_eta_weight_ctu1'].Fill(had_b_4vec.Eta(), weight_ctu1)
        histograms['h_had_b_4vec_phi_weight_ctu1'].Fill(had_b_4vec.Phi(), weight_ctu1)


        
        
        jet_pt_cut = 10
        leading_jet, second_leading_jet = select_leading_jets_from_matched(matches, jet_pt_cut) 
    
        # Filling histograms for
        for lepton in leptons:
            lepton_pt, lepton_eta, lepton_phi, lepton_pdgId = lepton

            # leptons in general
            histograms['h_leptonPt'].Fill(lepton_pt)
            histograms['h_leptoneta'].Fill(lepton_eta)
            histograms['h_leptonphi'].Fill(lepton_phi)
            histograms['h_leptonFlavor'].Fill(entry.GenPart_pdgId[k])
            
            histograms['h_leptonPt_weightSM'].Fill(lepton_pt, weight_0)
            histograms['h_leptoneta_weightSM'].Fill(lepton_eta, weight_0)
            histograms['h_leptonphi_weightSM'].Fill(lepton_phi, weight_0)
            histograms['h_leptonFlavor_weightSM'].Fill(entry.GenPart_pdgId[k], weight_0)
            
            histograms['h_leptonPt_ctGRe'].Fill(lepton_pt, weight_1)
            histograms['h_leptoneta_ctGRe'].Fill(lepton_eta, weight_1)
            histograms['h_leptonphi_ctGRe'].Fill(lepton_phi, weight_1)
            histograms['h_leptonFlavor_ctGRe'].Fill(entry.GenPart_pdgId[k], weight_1)
            
            histograms['h_leptonPt_scale_0'].Fill(lepton_pt, scale_weight_0)
            histograms['h_leptonPt_scale_1'].Fill(lepton_pt, scale_weight_1)
            histograms['h_leptonPt_scale_3'].Fill(lepton_pt, scale_weight_3)
            histograms['h_leptonPt_scale_4'].Fill(lepton_pt, scale_weight_4)
            histograms['h_leptonPt_scale_6'].Fill(lepton_pt, scale_weight_6)
            histograms['h_leptonPt_scale_7'].Fill(lepton_pt, scale_weight_7)
            
            histograms['h_leptonEta_scale_0'].Fill(lepton_eta, scale_weight_0)
            histograms['h_leptonEta_scale_1'].Fill(lepton_eta, scale_weight_1)
            histograms['h_leptonEta_scale_3'].Fill(lepton_eta, scale_weight_3)
            histograms['h_leptonEta_scale_4'].Fill(lepton_eta, scale_weight_4)
            histograms['h_leptonEta_scale_6'].Fill(lepton_eta, scale_weight_6)
            histograms['h_leptonEta_scale_7'].Fill(lepton_eta, scale_weight_7)
            

            # print("scale_index: ", scale_index, "scale_adjusted_weight: ", scale_adjusted_weight)
            # print("lepton_pt: ", lepton_pt ,"|| scaled by EFT: ", weight_1, "|| EVAL SM: ", histograms["h_leptoneta_weightSM"].Eval(lepton_pt), " || EVAL EFT: ", histograms["h_leptoneta_ctGRe"].Eval(lepton_pt))

            # electrons
            if abs(lepton_pdgId) == 11:
                histograms['h_electronPt'].Fill(lepton_pt)
                histograms['h_electroneta'].Fill(lepton_eta)
                
                histograms['h_electronPt_weightSM'].Fill(lepton_pt, weight_0)
                histograms['h_electroneta_weightSM'].Fill(lepton_eta, weight_0)
                
                histograms['h_electronPt_ctGRe'].Fill(lepton_pt, weight_1)
                histograms['h_electroneta_ctGRe'].Fill(lepton_eta, weight_1)
                
                histograms['h_electronPt_scale_0'].Fill(lepton_pt, scale_weight_0)
                histograms['h_electronPt_scale_1'].Fill(lepton_pt, scale_weight_1)
                histograms['h_electronPt_scale_3'].Fill(lepton_pt, scale_weight_3)
                histograms['h_electronPt_scale_4'].Fill(lepton_pt, scale_weight_4)
                histograms['h_electronPt_scale_6'].Fill(lepton_pt, scale_weight_6)
                histograms['h_electronPt_scale_7'].Fill(lepton_pt, scale_weight_7)
                
                histograms['h_electronEta_scale_0'].Fill(lepton_eta, scale_weight_0)
                histograms['h_electronEta_scale_1'].Fill(lepton_eta, scale_weight_1)
                histograms['h_electronEta_scale_3'].Fill(lepton_eta, scale_weight_3)
                histograms['h_electronEta_scale_4'].Fill(lepton_eta, scale_weight_4)
                histograms['h_electronEta_scale_6'].Fill(lepton_eta, scale_weight_6)
                histograms['h_electronEta_scale_7'].Fill(lepton_eta, scale_weight_7)
                
                                    
            elif abs(lepton_pdgId) == 13:
                muonPt = [lepton_pt * scale_weight for scale_weight in lheScaleWeights]
                muonEta = [lepton_eta * scale_weight for scale_weight in lheScaleWeights]
                
                histograms['h_muonPt'].Fill(lepton_pt)
                histograms['h_muoneta'].Fill(lepton_eta)
                
                histograms['h_muonPt_weightSM'].Fill(lepton_pt, weight_0)
                histograms['h_muoneta_weightSM'].Fill(lepton_eta, weight_0)
                
                histograms['h_muonPt_ctGRe'].Fill(lepton_pt,weight_1)
                histograms['h_muoneta_ctGRe'].Fill(lepton_eta, weight_1)
                
                histograms['h_muonPt_ctGRe'].Fill(lepton_pt, weight_1)
                histograms['h_muoneta_ctGRe'].Fill(lepton_eta, weight_1)
                
                histograms['h_muonPt_scale_0'].Fill(lepton_pt, scale_weight_0)
                histograms['h_muonPt_scale_1'].Fill(lepton_pt, scale_weight_1)
                histograms['h_muonPt_scale_3'].Fill(lepton_pt, scale_weight_3)
                histograms['h_muonPt_scale_4'].Fill(lepton_pt, scale_weight_4)
                histograms['h_muonPt_scale_6'].Fill(lepton_pt, scale_weight_6)
                histograms['h_muonPt_scale_7'].Fill(lepton_pt, scale_weight_7)
                
                histograms['h_muonEta_scale_0'].Fill(lepton_eta, scale_weight_0)
                histograms['h_muonEta_scale_1'].Fill(lepton_eta, scale_weight_1)
                histograms['h_muonEta_scale_3'].Fill(lepton_eta, scale_weight_3)
                histograms['h_muonEta_scale_4'].Fill(lepton_eta, scale_weight_4)
                histograms['h_muonEta_scale_6'].Fill(lepton_eta, scale_weight_6)
                histograms['h_muonEta_scale_7'].Fill(lepton_eta, scale_weight_7)
                
        # Filling histograms for
        for top_4vec, pdgId in tops:
            # top quarks
            if pdgId == 6:
                top_count += 1

                histograms['h_topPt'].Fill(top_4vec.Pt())
                histograms['h_topEta'].Fill(top_4vec.Eta())
                
                histograms['h_topPt_weightSM'].Fill(top_4vec.Pt(), weight_0)
                histograms['h_topEta_weightSM'].Fill(top_4vec.Eta(), weight_0)
                
                histograms['h_topPt_ctGRe'].Fill(top_4vec.Pt(),weight_1)
                histograms['h_topEta_ctGRe'].Fill(top_4vec.Eta(), weight_1)
                
                histograms['h_topPt_scale_0'].Fill(top_4vec.Pt(), scale_weight_0)
                histograms['h_topPt_scale_1'].Fill(top_4vec.Pt(), scale_weight_1)
                histograms['h_topPt_scale_3'].Fill(top_4vec.Pt(), scale_weight_3)
                histograms['h_topPt_scale_4'].Fill(top_4vec.Pt(), scale_weight_4)
                histograms['h_topPt_scale_6'].Fill(top_4vec.Pt(), scale_weight_6)
                histograms['h_topPt_scale_7'].Fill(top_4vec.Pt(), scale_weight_7)
                
                histograms['h_topEta_scale_0'].Fill(top_4vec.Eta(), scale_weight_0)
                histograms['h_topEta_scale_1'].Fill(top_4vec.Eta(), scale_weight_1)
                histograms['h_topEta_scale_3'].Fill(top_4vec.Eta(), scale_weight_3)
                histograms['h_topEta_scale_4'].Fill(top_4vec.Eta(), scale_weight_4)
                histograms['h_topEta_scale_6'].Fill(top_4vec.Eta(), scale_weight_6)
                histograms['h_topEta_scale_7'].Fill(top_4vec.Eta(), scale_weight_7)

            # top antiquarks
            elif pdgId == -6:
                antitop_count += 1
                
                histograms['h_antitopPt'].Fill(antitop_4vec.Pt())
                histograms['h_antitopEta'].Fill(antitop_4vec.Eta())
                
                histograms['h_antitopPt_weightSM'].Fill(antitop_4vec.Pt(), weight_0)
                histograms['h_antitopEta_weightSM'].Fill(antitop_4vec.Eta(), weight_0)
                
                histograms['h_antitopPt_ctGRe'].Fill(antitop_4vec.Pt(), weight_1)
                histograms['h_antitopEta_ctGRe'].Fill(antitop_4vec.Eta(), weight_1)
                
                histograms['h_antitopPt_scale_0'].Fill(antitop_4vec.Pt(), scale_weight_0)
                histograms['h_antitopPt_scale_1'].Fill(antitop_4vec.Pt(), scale_weight_1)
                histograms['h_antitopPt_scale_3'].Fill(antitop_4vec.Pt(), scale_weight_3)
                histograms['h_antitopPt_scale_4'].Fill(antitop_4vec.Pt(), scale_weight_4)
                histograms['h_antitopPt_scale_6'].Fill(antitop_4vec.Pt(), scale_weight_6)
                histograms['h_antitopPt_scale_7'].Fill(antitop_4vec.Pt(), scale_weight_7)
                
                histograms['h_antitopEta_scale_0'].Fill(antitop_4vec.Eta(), scale_weight_0)
                histograms['h_antitopEta_scale_1'].Fill(antitop_4vec.Eta(), scale_weight_1)
                histograms['h_antitopEta_scale_3'].Fill(antitop_4vec.Eta(), scale_weight_3)
                histograms['h_antitopEta_scale_4'].Fill(antitop_4vec.Eta(), scale_weight_4)
                histograms['h_antitopEta_scale_6'].Fill(antitop_4vec.Eta(), scale_weight_6)
                histograms['h_antitopEta_scale_7'].Fill(antitop_4vec.Eta(), scale_weight_7)


            histograms['h_topMultiplicity'].Fill(top_count)
            histograms['h_topMultiplicity_weightSM'].Fill(top_count, weight_0)
            histograms['h_topMultiplicity_ctGRe'].Fill(top_count, weight_1)
            
            histograms['h_antitopMultiplicity'].Fill(antitop_count)
            histograms['h_antitopMultiplicity_weightSM'].Fill(antitop_count, weight_0)
            histograms['h_antitopMultiplicity_ctGRe'].Fill(antitop_count, weight_1)

        #Filling histograms for b quarks
        for b_quark in b_quarks:
            b_vector, b_index = b_quark 
            
            histograms['h_bquark_pt'].Fill(b_vector.Pt())
            histograms['h_bquark_eta'].Fill(b_vector.Eta())

            histograms['h_bquark_pt_weightSM'].Fill(b_vector.Pt(), weight_0)
            histograms['h_bquark_eta_weightSM'].Fill(b_vector.Eta(), weight_0)
            
            histograms['h_bquark_pt_ctGRe'].Fill(b_vector.Pt(), weight_1)
            histograms['h_bquark_eta_ctGRe'].Fill(b_vector.Eta(), weight_1)
            
        for jet_info in jets_from_w_info:
            jet_idx, jet_pt, jet_eta, jet_phi = jet_info
            histograms['h_jetFromW_pt'].Fill(jet_pt)
            histograms['h_jetFromW_eta'].Fill(jet_eta)
            
            histograms['h_jetFromW_pt_weightSM'].Fill(jet_pt, weight_0)
            histograms['h_jetFromW_eta_weightSM'].Fill(jet_eta, weight_0)
            
            histograms['h_jetFromW_pt_ctGRe'].Fill(jet_pt, weight_1)
            histograms['h_jetFromW_eta_ctGRe'].Fill(jet_eta, weight_1)
            

        histograms['h_jetMultiplicity_fromW'].Fill(jets_from_w_count)
        histograms['h_jetMultiplicity_fromW_weightSM'].Fill(jets_from_w_count, weight_0)
        histograms['h_jetMultiplicity_fromW_ctGRe'].Fill(jets_from_w_count, weight_1)
        
        # HT variable from data in ttree
        LHE_HT = getattr(entry, "LHE_HT", -1)

        # Filling histograms for ttbar system
        if top_4vec and antitop_4vec:
            ttbar = top_4vec + antitop_4vec
            m_tt = ttbar.M()
                
            histograms['h_invariantMass'].Fill(ttbar.M())
            histograms['h_invariantMass_weightSM'].Fill(ttbar.M(), weight_0)
            histograms['h_invariantMass_ctGRe'].Fill(ttbar.M(), weight_1)
            
            histograms['h_invariantMass_scale_0'].Fill(ttbar.M(), scale_weight_0)
            histograms['h_invariantMass_scale_1'].Fill(ttbar.M(), scale_weight_1)
            histograms['h_invariantMass_scale_3'].Fill(ttbar.M(), scale_weight_3)
            histograms['h_invariantMass_scale_4'].Fill(ttbar.M(), scale_weight_4)
            histograms['h_invariantMass_scale_6'].Fill(ttbar.M(), scale_weight_6)
            histograms['h_invariantMass_scale_7'].Fill(ttbar.M(), scale_weight_7)
                    
            # LHE_HT = getattr(entry, "LHE_HT", -1)
            if LHE_HT >= 0:                    
                    
                LHE_HT = getattr(entry, "LHE_HT", -1)
                if LHE_HT >= 0:
    
                    if 0 <= m_tt < 500:
                        histograms['h_LHE_HT_0_500'].Fill(LHE_HT)
                        histograms['h_LHE_HT_0_500_weightSM'].Fill(LHE_HT, weight_0)
                        histograms['h_LHE_HT_0_500_ctGRe'].Fill(LHE_HT, weight_1)
                    elif 500 <= m_tt < 750:
                        histograms['h_LHE_HT_500_750'].Fill(LHE_HT)
                        histograms['h_LHE_HT_500_750_weightSM'].Fill(LHE_HT, weight_0)
                        histograms['h_LHE_HT_500_750_ctGRe'].Fill(LHE_HT, weight_1)
                    elif 750 <= m_tt < 1000:
                        histograms['h_LHE_HT_750_1000'].Fill(LHE_HT)
                        histograms['h_LHE_HT_750_1000_weightSM'].Fill(LHE_HT, weight_0)
                        histograms['h_LHE_HT_750_1000_ctGRe'].Fill(LHE_HT, weight_1)
                    elif 1000 <= m_tt < 1500:
                        histograms['h_LHE_HT_1000_1500'].Fill(LHE_HT)
                        histograms['h_LHE_HT_1000_1500_weightSM'].Fill(LHE_HT, weight_0)
                        histograms['h_LHE_HT_1000_1500_ctGRe'].Fill(LHE_HT, weight_1)
                    elif m_tt >= 1500:
                        histograms['h_LHE_HT_1500Inf'].Fill(LHE_HT)
                        histograms['h_LHE_HT_1500Inf_weightSM'].Fill(LHE_HT, weight_0)
                        histograms['h_LHE_HT_1500Inf_ctGRe'].Fill(LHE_HT, weight_1)
            
        # # HT variable from data in ttree
        # LHE_HT = getattr(entry, "LHE_HT", -1)
        if LHE_HT >= 0:
            histograms['h_mtt_vs_LHEHT'].Fill(LHE_HT, m_tt)
            histograms['h_LHE_HT'].Fill(LHE_HT)
            
            histograms['h_mtt_vs_LHEHT_weightSM'].Fill(LHE_HT, m_tt, weight_0)
            histograms['h_LHE_HT_weightSM'].Fill(LHE_HT, weight_0)
            
            histograms['h_mtt_vs_LHEHT_ctGRe'].Fill(LHE_HT, m_tt, weight_1)
            histograms['h_LHE_HT_ctGRe'].Fill(LHE_HT, weight_1)
        
        
        if leading_jet is not None and second_leading_jet is not None:
            if leading_jet:
            
                histograms['h_leading_jet_pt'].Fill(leading_jet[0].Pt()) #leading_jet[0] contains the pt of the leading jet
                histograms['h_leading_jet_pt_weightSM'].Fill(leading_jet[0].Pt(), weight_0)
                histograms['h_leading_jet_pt_ctGRe'].Fill(leading_jet[0].Pt(), weight_1)
                
                histograms['h_leading_jet_pt_scale_0'].Fill(leading_jet[0].Pt(), scale_weight_0)
                histograms['h_leading_jet_pt_scale_1'].Fill(leading_jet[0].Pt(), scale_weight_1)
                histograms['h_leading_jet_pt_scale_3'].Fill(leading_jet[0].Pt(), scale_weight_3)
                histograms['h_leading_jet_pt_scale_4'].Fill(leading_jet[0].Pt(), scale_weight_4)
                histograms['h_leading_jet_pt_scale_6'].Fill(leading_jet[0].Pt(), scale_weight_6)
                histograms['h_leading_jet_pt_scale_7'].Fill(leading_jet[0].Pt(), scale_weight_7)
                
            if second_leading_jet:
                
                histograms['h_second_leading_jet_pt'].Fill(second_leading_jet[0].Pt())
                histograms['h_second_leading_jet_pt_weightSM'].Fill(second_leading_jet[0].Pt(), weight_0)
                histograms['h_second_leading_jet_pt_ctGRe'].Fill(second_leading_jet[0].Pt(), weight_1) 
                
                histograms['h_second_leading_jet_pt_scale_0'].Fill(second_leading_jet[0].Pt(), scale_weight_0)
                histograms['h_second_leading_jet_pt_scale_1'].Fill(second_leading_jet[0].Pt(), scale_weight_1)
                histograms['h_second_leading_jet_pt_scale_3'].Fill(second_leading_jet[0].Pt(), scale_weight_3)
                histograms['h_second_leading_jet_pt_scale_4'].Fill(second_leading_jet[0].Pt(), scale_weight_4)
                histograms['h_second_leading_jet_pt_scale_6'].Fill(second_leading_jet[0].Pt(), scale_weight_6)
                histograms['h_second_leading_jet_pt_scale_7'].Fill(second_leading_jet[0].Pt(), scale_weight_7)
                

    return tops, hadronic_top_pt, leptons, b_quarks, w_quarks1, w_quarks2, last_copy_partons
    ### End of process_event
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------*-----------------------------------------------------------------------------------------#

# This function identifies jets that are closely matched with last copy partons. 
# It appends a tuple to matched_jets which includes the jet and its index in the GenJet collection.
def one_to_one_matching(entry, b_quarks, w_quarks1, w_quarks2):

    jets = []
    for j in range(entry.nGenJet):
        jet_vec = ROOT.TLorentzVector()
        jet_vec.SetPtEtaPhiM(entry.GenJet_pt[j], entry.GenJet_eta[j], entry.GenJet_phi[j], 0)  # Assuming massless jets
        jets.append(jet_vec)
        
        
    partons = b_quarks + w_quarks1 + w_quarks2
    
    matched_jets_indices = set()
    matched_partons_indices = set()
    matches = []

    for jet_index, jet in enumerate(jets):
        closest_deltaR = float('inf')
        closest_parton_index = None
        # second element is not used here, that's why I have "_" next to parton_vec as a placeholder for the other info in the tuple
        for parton_index, (parton_vec, _) in enumerate(partons):
            dR = deltaR(jet.Eta(), jet.Phi(), parton_vec.Eta(), parton_vec.Phi())
            if dR < closest_deltaR and parton_index not in matched_partons_indices:
                closest_deltaR = dR
                closest_parton_index = parton_index
        
        if closest_deltaR < 0.4 and closest_parton_index is not None:
            matched_jets_indices.add(jet_index)
            matched_partons_indices.add(closest_parton_index)
            matches.append((jets[jet_index], partons[closest_parton_index]))

    return matches


# This function filters and sorts the jets based on their Pt, 
# then identifies the leading and second-leading jets.
def select_leading_jets_from_matched(matches, jet_pt_cut):
    
    filtered_jets = [(jet, pdg_id) for (jet, _), pdg_id in matches if jet.Pt() > jet_pt_cut]

    # Sort the matched jets by their pT in descending order
    sorted_jets = sorted(filtered_jets, key=lambda jet_tuple: jet_tuple[0].Pt(), reverse=True)

    # Select the leading and second leading jets
    leading_jet = sorted_jets[0] if len(sorted_jets) > 0 else None
    second_leading_jet = sorted_jets[1] if len(sorted_jets) > 1 else None

    return leading_jet, second_leading_jet


# This function correctly identifies the leading b-quark that is not part of the leading or second-leading jets. 
# It iterates through the b_quarks, excludes those that match the leading or second-leading jets, and then finds the one with the highest Pt.
def find_leading_b_quark(b_quarks, leading_jet, second_leading_jet, last_copy_partons):
    highest_pt = 0
    leading_b_quark = None
    for b_quark in b_quarks:
        b_vector, _ = b_quark
        if leading_jet and deltaR(leading_jet[0].Eta(), leading_jet[0].Phi(), b_vector.Eta(), b_vector.Phi()) < 0.4:
            continue
        if second_leading_jet and deltaR(second_leading_jet[0].Eta(), second_leading_jet[0].Phi(), b_vector.Eta(), b_vector.Phi()) < 0.4:
            continue
        if b_vector.Pt() > highest_pt:
            highest_pt = b_vector.Pt()
            leading_b_quark = b_quark
    # veto if no suitable b-quark is found
    return leading_b_quark if highest_pt > 30 else None


# Main function that reads the input file, fills the histograms, and returns the number of events processed.
totalEvents = 0
def analyze(filename):
    print "Processing file:", filename
    
    if not os.path.isfile(filename):
        print "Error: The path provided is not a file:", filename
        return None

    try:
        file = ROOT.TFile.Open(filename)
        if not file or file.IsZombie():
            print "Error: Unable to open file:", filename
            return None
        tree = file.Get("Events")
        
    except Exception as e:
        print "An error occurred while processing the file {}: {}".format(filename, str(e))
        return None
    
    global totalEvents
    totalEvents += tree.GetEntries()
    print "Number of events in file:", int(tree.GetEntries())
    
    relevant_pdgIds = {12, 14, 16, 24, 1, 2, 3, 4, 5, 6, 21, 11, 13, 15}
    
    histograms = {
    'h_leptonPt': h_leptonPt,
    'h_leptoneta': h_leptoneta,
    'h_leptonphi': h_leptonphi,
    'h_leptonFlavor': h_leptonFlavor,
    'h_electronPt': h_electronPt,
    'h_electroneta': h_electroneta,

    'h_muonPt': h_muonPt,
    'h_muoneta': h_muoneta,

    'h_hadronic_w_mass': h_hadronic_w_mass,

    'h_topPt': h_topPt,
    'h_topEta': h_topEta,
    'h_antitopPt': h_antitopPt,
    'h_antitopEta': h_antitopEta,
    'h_topMultiplicity': h_topMultiplicity,
    'h_antitopMultiplicity': h_antitopMultiplicity,
    'h_invariantMass': h_invariantMass,

    'h_jetMultiplicity_fromW': h_jetMultiplicity_fromW,
    'h_jetMultiplicity': h_jetMultiplicity,
    'h_nonTopMotherJets': h_nonTopMotherJets,

    'h_LHE_HT' : h_LHE_HT,
    'h_LHE_HT_0_500' : h_LHE_HT_0_500,
    'h_LHE_HT_500_750' : h_LHE_HT_500_750,
    'h_LHE_HT_750_1000' : h_LHE_HT_750_1000,
    'h_LHE_HT_1000_1500' : h_LHE_HT_1000_1500,
    'h_LHE_HT_1500Inf' : h_LHE_HT_1500Inf,

    'h_both_decays': h_both_decays,

    'h_jetFromW_pt': h_jetFromW_pt,
    'h_jetFromW_eta': h_jetFromW_eta,
    'h_leading_jet_pt' : h_leading_jet_pt,
    'h_second_leading_jet_pt' : h_second_leading_jet_pt,
    "h_jet_multiplicity_last_copy" : h_jet_multiplicity_last_copy,

    "h_mtt_vs_LHEHT" : h_mtt_vs_LHEHT,

    "h_bquark_pt" : h_bquark_pt,
    "h_bquark_eta": h_bquark_eta,

    "h_had_b_4vec_pt" : h_had_b_4vec_pt,
    "h_had_b_4vec_eta" : h_had_b_4vec_eta,
    "h_had_b_4vec_phi" : h_had_b_4vec_phi,
    "h_had_b_4vec_mass" : h_had_b_4vec_mass,

    "h_had_b_4vec_pt_weight_ctu1" :h_had_b_4vec_pt_weight_ctu1,
    "h_had_b_4vec_eta_weight_ctu1" : h_had_b_4vec_eta_weight_ctu1,
    "h_had_b_4vec_phi_weight_ctu1" : h_had_b_4vec_phi_weight_ctu1,

    "h_pdgId_last_copy": h_pdgId_last_copy,
    "h_pdgId_first_copy": h_pdgId_first_copy,
    "h_pdgId_ishardprocess" : h_pdgId_ishardprocess,
    "h_pdgId_fromhardprocess" : h_pdgId_fromhardprocess,

    
    'h_leptonPt_scale_0': h_leptonPt_scale_0,
    'h_leptonEta_scale_0': h_leptonEta_scale_0,
    'h_electronPt_scale_0' : h_electronPt_scale_0,
    'h_electronEta_scale_0': h_electronEta_scale_0,
    'h_muonPt_scale_0': h_muonPt_scale_0,
    'h_muonEta_scale_0': h_muonEta_scale_0,

    'h_topPt_scale_0': h_topPt_scale_0,
    'h_topEta_scale_0': h_topEta_scale_0,
    'h_antitopPt_scale_0': h_antitopPt_scale_0,
    'h_antitopEta_scale_0': h_antitopEta_scale_0,
    'h_invariantMass_scale_0': h_invariantMass_scale_0,
    "h_leading_jet_pt_scale_0" : h_leading_jet_pt_scale_0,
    "h_second_leading_jet_pt_scale_0" : h_second_leading_jet_pt_scale_0,
    "h_jet_multiplicity_ishardprocess_scale_0" : h_jet_multiplicity_ishardprocess_scale_0,
    "h_jet_multiplicity_last_copy_scale_0" : h_jet_multiplicity_last_copy_scale_0,
    
    'h_leptonPt_scale_1': h_leptonPt_scale_1,
    'h_leptonEta_scale_1': h_leptonEta_scale_1,
    'h_electronPt_scale_1' : h_electronPt_scale_1,
    'h_electronEta_scale_1': h_electronEta_scale_1,
    'h_muonPt_scale_1': h_muonPt_scale_1,
    'h_muonEta_scale_1': h_muonEta_scale_1,
    'h_topPt_scale_1': h_topPt_scale_1,
    'h_topEta_scale_1': h_topEta_scale_1,
    'h_antitopPt_scale_1': h_antitopPt_scale_1,
    'h_antitopEta_scale_1': h_antitopEta_scale_1,
    'h_invariantMass_scale_1': h_invariantMass_scale_1,
    "h_leading_jet_pt_scale_1" : h_leading_jet_pt_scale_1,
    "h_second_leading_jet_pt_scale_1" : h_second_leading_jet_pt_scale_1,
    "h_jet_multiplicity_ishardprocess_scale_1" : h_jet_multiplicity_ishardprocess_scale_1,
    "h_jet_multiplicity_last_copy_scale_1" : h_jet_multiplicity_last_copy_scale_1,
    
    'h_leptonPt_scale_3': h_leptonPt_scale_3,
    'h_leptonEta_scale_3': h_leptonEta_scale_3,
    'h_electronPt_scale_3' : h_electronPt_scale_3,
    'h_electronEta_scale_3': h_electronEta_scale_3,
    'h_muonPt_scale_3': h_muonPt_scale_3,
    'h_muonEta_scale_3': h_muonEta_scale_3,
    'h_topPt_scale_3': h_topPt_scale_3,
    'h_topEta_scale_3': h_topEta_scale_3,
    'h_antitopPt_scale_3': h_antitopPt_scale_3,
    'h_antitopEta_scale_3': h_antitopEta_scale_3,
    'h_invariantMass_scale_3': h_invariantMass_scale_3,
    "h_leading_jet_pt_scale_3" : h_leading_jet_pt_scale_3,
    "h_second_leading_jet_pt_scale_3" : h_second_leading_jet_pt_scale_3,
    "h_jet_multiplicity_ishardprocess_scale_3" : h_jet_multiplicity_ishardprocess_scale_3,
    "h_jet_multiplicity_last_copy_scale_3" : h_jet_multiplicity_last_copy_scale_3,
    
    'h_leptonPt_scale_4': h_leptonPt_scale_4,
    'h_leptonEta_scale_4': h_leptonEta_scale_4,
    'h_electronPt_scale_4' : h_electronPt_scale_4,
    'h_electronEta_scale_4': h_electronEta_scale_4,
    'h_muonPt_scale_4': h_muonPt_scale_4,
    'h_muonEta_scale_4': h_muonEta_scale_4,
    'h_topPt_scale_4': h_topPt_scale_4,
    'h_topEta_scale_4': h_topEta_scale_4,
    'h_antitopPt_scale_4': h_antitopPt_scale_4,
    'h_antitopEta_scale_4': h_antitopEta_scale_4,
    'h_invariantMass_scale_4': h_invariantMass_scale_4,
    "h_leading_jet_pt_scale_4" : h_leading_jet_pt_scale_4,
    "h_second_leading_jet_pt_scale_4" : h_second_leading_jet_pt_scale_4,
    "h_jet_multiplicity_ishardprocess_scale_4" : h_jet_multiplicity_ishardprocess_scale_4,
    "h_jet_multiplicity_last_copy_scale_4" : h_jet_multiplicity_last_copy_scale_4,
    
    'h_leptonPt_scale_6': h_leptonPt_scale_6,
    'h_leptonEta_scale_6': h_leptonEta_scale_6,
    'h_electronPt_scale_6' : h_electronPt_scale_6,
    'h_electronEta_scale_6': h_electronEta_scale_6,
    'h_muonPt_scale_6': h_muonPt_scale_6,
    'h_muonEta_scale_6': h_muonEta_scale_6,
    'h_topPt_scale_6': h_topPt_scale_6,
    'h_topEta_scale_6': h_topEta_scale_6,
    'h_antitopPt_scale_6': h_antitopPt_scale_6,
    'h_antitopEta_scale_6': h_antitopEta_scale_6,
    'h_invariantMass_scale_6': h_invariantMass_scale_6,
    "h_leading_jet_pt_scale_6" : h_leading_jet_pt_scale_6,
    "h_second_leading_jet_pt_scale_6" : h_second_leading_jet_pt_scale_6,
    "h_jet_multiplicity_ishardprocess_scale_6" : h_jet_multiplicity_ishardprocess_scale_6,
    "h_jet_multiplicity_last_copy_scale_6" : h_jet_multiplicity_last_copy_scale_6,
    
    'h_leptonPt_scale_7': h_leptonPt_scale_7,
    'h_leptonEta_scale_7': h_leptonEta_scale_7,
    'h_electronPt_scale_7' : h_electronPt_scale_7,
    'h_electronEta_scale_7': h_electronEta_scale_7,
    'h_muonPt_scale_7': h_muonPt_scale_7,
    'h_muonEta_scale_7': h_muonEta_scale_7,
    'h_topPt_scale_7': h_topPt_scale_7,
    'h_topEta_scale_7': h_topEta_scale_7,
    'h_antitopPt_scale_7': h_antitopPt_scale_7,
    'h_antitopEta_scale_7': h_antitopEta_scale_7,
    'h_invariantMass_scale_7': h_invariantMass_scale_7,
    "h_leading_jet_pt_scale_7" : h_leading_jet_pt_scale_7,
    "h_second_leading_jet_pt_scale_7" : h_second_leading_jet_pt_scale_7,
    "h_jet_multiplicity_ishardprocess_scale_7" : h_jet_multiplicity_ishardprocess_scale_7,
    "h_jet_multiplicity_last_copy_scale_7" : h_jet_multiplicity_last_copy_scale_7,
    
    'h_leptonPt_weightSM': h_leptonPt_weightSM,
    'h_leptoneta_weightSM': h_leptoneta_weightSM,
    'h_leptonphi_weightSM': h_leptonphi_weightSM,
    'h_leptonFlavor_weightSM': h_leptonFlavor_weightSM,
    'h_electronPt_weightSM': h_electronPt_weightSM,
    'h_electroneta_weightSM': h_electroneta_weightSM,
    'h_muonPt_weightSM': h_muonPt_weightSM,
    'h_muoneta_weightSM': h_muoneta_weightSM,
    'h_hadronic_w_mass_weightSM': h_hadronic_w_mass_weightSM,
    'h_topPt_weightSM': h_topPt_weightSM,
    'h_topEta_weightSM': h_topEta_weightSM,
    'h_antitopPt_weightSM': h_antitopPt_weightSM,
    'h_antitopEta_weightSM': h_antitopEta_weightSM,
    'h_topMultiplicity_weightSM': h_topMultiplicity_weightSM,
    'h_antitopMultiplicity_weightSM': h_antitopMultiplicity_weightSM,
    'h_jetMultiplicity_fromW_weightSM': h_jetMultiplicity_fromW_weightSM,
    'h_invariantMass_weightSM': h_invariantMass_weightSM,
    'h_jetMultiplicity_weightSM': h_jetMultiplicity_weightSM,
    'h_nonTopMotherJets_weightSM': h_nonTopMotherJets_weightSM,
    'h_LHE_HT_weightSM' : h_LHE_HT_weightSM,
    'h_LHE_HT_0_500_weightSM' : h_LHE_HT_0_500_weightSM,
    'h_LHE_HT_500_750_weightSM' : h_LHE_HT_500_750_weightSM,
    'h_LHE_HT_750_1000_weightSM' : h_LHE_HT_750_1000_weightSM,
    'h_LHE_HT_1000_1500_weightSM' : h_LHE_HT_1000_1500_weightSM,
    'h_LHE_HT_1500Inf_weightSM' : h_LHE_HT_1500Inf_weightSM,
    'h_both_decays_weightSM': h_both_decays_weightSM,
    'h_jetFromW_pt_weightSM': h_jetFromW_pt_weightSM,
    'h_jetFromW_eta_weightSM': h_jetFromW_eta_weightSM,
    'h_leading_jet_pt_weightSM' : h_leading_jet_pt_weightSM,
    'h_second_leading_jet_pt_weightSM' : h_second_leading_jet_pt_weightSM,
    "h_jet_multiplicity_last_copy_weightSM" : h_jet_multiplicity_last_copy_weightSM,
    "h_jet_multiplicity_hardprocess_weightSM" : h_jet_multiplicity_hardprocess_weightSM,
    "h_jet_multiplicity_ishardprocess_weightSM" : h_jet_multiplicity_ishardprocess_weightSM,
    "h_mtt_vs_LHEHT_weightSM" : h_mtt_vs_LHEHT_weightSM,
    "h_bquark_pt_weightSM" : h_bquark_pt_weightSM,
    "h_bquark_eta_weightSM": h_bquark_eta_weightSM,
    
    'h_leptonPt_ctGRe': h_leptonPt_ctGRe,
    'h_leptoneta_ctGRe': h_leptoneta_ctGRe,
    'h_leptonphi_ctGRe': h_leptonphi_ctGRe,
    'h_leptonFlavor_ctGRe': h_leptonFlavor_ctGRe,
    'h_electronPt_ctGRe': h_electronPt_ctGRe,
    'h_electroneta_ctGRe': h_electroneta_ctGRe,
    'h_muonPt_ctGRe': h_muonPt_ctGRe,
    'h_muoneta_ctGRe': h_muoneta_ctGRe,
    'h_hadronic_w_mass_ctGRe': h_hadronic_w_mass_ctGRe,
    'h_topPt_ctGRe': h_topPt_ctGRe,
    'h_topEta_ctGRe': h_topEta_ctGRe,
    'h_antitopPt_ctGRe': h_antitopPt_ctGRe,
    'h_antitopEta_ctGRe': h_antitopEta_ctGRe,
    'h_topMultiplicity_ctGRe': h_topMultiplicity_ctGRe,
    'h_antitopMultiplicity_ctGRe': h_antitopMultiplicity_ctGRe,
    'h_jetMultiplicity_fromW_ctGRe': h_jetMultiplicity_fromW_ctGRe,
    'h_invariantMass_ctGRe': h_invariantMass_ctGRe,
    'h_jetMultiplicity_ctGRe': h_jetMultiplicity_ctGRe,
    'h_nonTopMotherJets_ctGRe': h_nonTopMotherJets_ctGRe,
    'h_LHE_HT_ctGRe' : h_LHE_HT_ctGRe,
    'h_LHE_HT_0_500_ctGRe' : h_LHE_HT_0_500_ctGRe,
    'h_LHE_HT_500_750_ctGRe' : h_LHE_HT_500_750_ctGRe,
    'h_LHE_HT_750_1000_ctGRe' : h_LHE_HT_750_1000_ctGRe,
    'h_LHE_HT_1000_1500_ctGRe' : h_LHE_HT_1000_1500_ctGRe,
    'h_LHE_HT_1500Inf_ctGRe' : h_LHE_HT_1500Inf_ctGRe,
    'h_both_decays_ctGRe': h_both_decays_ctGRe,
    'h_jetFromW_pt_ctGRe': h_jetFromW_pt_ctGRe,
    'h_jetFromW_eta_ctGRe': h_jetFromW_eta_ctGRe,
    'h_leading_jet_pt_ctGRe' : h_leading_jet_pt_ctGRe,
    'h_second_leading_jet_pt_ctGRe' : h_second_leading_jet_pt_ctGRe,
    "h_jet_multiplicity_last_copy_ctGRe" : h_jet_multiplicity_last_copy_ctGRe,
    "h_jet_multiplicity_hardprocess_ctGRe" : h_jet_multiplicity_hardprocess_ctGRe,
    "h_jet_multiplicity_ishardprocess_ctGRe" : h_jet_multiplicity_ishardprocess_ctGRe,
    "h_mtt_vs_LHEHT_ctGRe" : h_mtt_vs_LHEHT_ctGRe,
    "h_bquark_pt_ctGRe" : h_bquark_pt_ctGRe,
    "h_bquark_eta_ctGRe": h_bquark_eta_ctGRe,  
    }
    
    # Executes function that processes particles in each event
    for ientry, entry in enumerate(tree):
        # print("EVENT: ", ientry)
        process_event(entry, histograms, relevant_pdgIds)
    file.Close()
    return histograms


def createCanvas(histogram, title, filename, logy=False, fillColor=None, lineColor=None):
    canvas = ROOT.TCanvas(title, title, 800, 600)
    if fillColor is not None:
        histogram.SetFillColor(fillColor)
    if lineColor is not None:
        histogram.SetLineColor(lineColor)
    histogram.Draw()
    if logy:
        ROOT.gPad.SetLogy(1)
    canvas_filepath = os.path.join(output_dir, filename)
    canvas.SaveAs(canvas_filepath)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python EFT_nanofiles_fully_semileptonic.py <input file>"
        sys.exit(1)

    input_filename = sys.argv[1]
    output_dir = "/nfs/dust/cms/user/ricardo/EFT/CMSSW_10_6_26/src/EFT_gen/EFT_samples/nanogen_folder/condor/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    histograms = analyze(input_filename)
    
    output_filename = os.path.basename(input_filename).replace('.root', '_histograms.root')
    output_file_path = os.path.join(output_dir, output_filename)
    output_file = ROOT.TFile(output_file_path, "RECREATE")
    for name, hist in histograms.items():
        hist.SetDirectory(output_file)
        hist.Write()
    output_file.Close()
    
    # for name, hist in histograms.items():
    #     canvas_title = "{} Canvas".format(name)
    #     canvas_filename = "{}.png".format(name)
    #     createCanvas(hist, canvas_title, canvas_filename, output_dir=output_dir)

    print "Processed: {}".format(input_filename) 

       
print "Total number of events:", int(totalEvents) 
