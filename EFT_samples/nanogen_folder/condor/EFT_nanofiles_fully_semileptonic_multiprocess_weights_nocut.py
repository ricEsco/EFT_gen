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

## nominal (SM) histograms
h_topPt = ROOT.TH1F("h_topPt", "Top Quark; pT (GeV); Events", 100, 0, 2000)
h_topEta = ROOT.TH1F("h_topEta", "Top Quark; #eta; Events", 100, -5, 5)
h_topPhi = ROOT.TH1F("h_topPhi", "Top Quark; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_topMass = ROOT.TH1F("h_topMass", "Top Quark; Mass; Events", 50, 0, 500)

h_antitopPt = ROOT.TH1F("h_antitopPt", "Anti-Top Quark ; p_{T} [GeV]; Events", 100, 0, 2000)
h_antitopEta = ROOT.TH1F("h_antitopEta", "Anti-Top Quark; #eta; Events", 100, -5, 5)
h_antitopPhi = ROOT.TH1F("h_antitopPhi", "Anti-Top Quark; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_antitopMass = ROOT.TH1F("h_antitopMass", "Anti-Top Quark; Mass; Events", 50, 0, 500)

h_ttbarPt = ROOT.TH1F("h_ttbarPt", "ttbar system; pT (GeV); Events", 100, 0, 2000)
h_ttbarEta = ROOT.TH1F("h_ttbarEta", "ttbar system; #eta; Events", 100, -5, 5)
h_ttbarPhi = ROOT.TH1F("h_ttbarPhi", "ttbar system; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_ttbarMass = ROOT.TH1F("h_ttbarMass", "ttbar system; Mass (GeV); Events", 150, 0, 3000)

h_had_b_4vec_pt = ROOT.TH1F("h_had_b_4vec_pt", "b-quark from t_{Hadronic}; pT (GeV); Events", 50, 0, 1000)
h_had_b_4vec_eta = ROOT.TH1F("h_had_b_4vec_eta", "b-quark from t_{Hadronic}; #eta; Events", 100, -5, 5)
h_had_b_4vec_phi = ROOT.TH1F("h_had_b_4vec_phi", "b-quark from t_{Hadronic}; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass = ROOT.TH1F("h_had_b_4vec_mass", "b-quark from t_{Hadronic}; Mass; Events", 50, 0, 10)

h_lepton_pt = ROOT.TH1F("h_lepton_pt", "Lepton; pT (GeV); Events", 50, 0, 1000)
h_lepton_eta = ROOT.TH1F("h_lepton_eta", "Lepton; #eta; Events", 100, -5, 5)
h_lepton_phi = ROOT.TH1F("h_lepton_phi", "Lepton; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass = ROOT.TH1F("h_lepton_mass", "Lepton; Mass; Events", 50, 0, 10)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# ctu1 weighted histograms
h_ttbarMass_weight_ctu1 = ROOT.TH1F("h_ttbarMass_weight_ctu1", "ttbar system; Mass (GeV);Events", 150, 0, 3000)

h_had_b_4vec_pt_weight_ctu1  = ROOT.TH1F("h_had_b_4vec_pt_weight_ctu1", "b-quark from t_{Hadronic}; pT (GeV); Events", 50, 0, 1000)
h_had_b_4vec_eta_weight_ctu1 = ROOT.TH1F("h_had_b_4vec_eta_weight_ctu1", "b-quark from t_{Hadronic}; #eta; Events", 100, -5, 5)
h_had_b_4vec_phi_weight_ctu1 = ROOT.TH1F("h_had_b_4vec_phi_weight_ctu1", "b-quark from t_{Hadronic}; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass_weight_ctu1 = ROOT.TH1F("h_had_b_4vec_mass_weight_ctu1", "b-quark from t_{Hadronic}; Mass; Events", 50, 0, 10)

h_lepton_pt_weight_ctu1  = ROOT.TH1F("h_lepton_pt_weight_ctu1", "Lepton; pT (GeV); Events", 50, 0, 1000)
h_lepton_eta_weight_ctu1 = ROOT.TH1F("h_lepton_eta_weight_ctu1", "Lepton; #eta; Events", 100, -5, 5)
h_lepton_phi_weight_ctu1 = ROOT.TH1F("h_lepton_phi_weight_ctu1", "Lepton; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass_weight_ctu1 = ROOT.TH1F("h_lepton_mass_weight_ctu1", "Lepton; Mass; Events", 50, 0, 10)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# cQj11 weighted histograms
h_ttbarMass_weight_cQj11 = ROOT.TH1F("h_ttbarMass_weight_cQj11", "ttbar system; Mass (GeV);Events", 150, 0, 3000)

h_had_b_4vec_pt_weight_cQj11  = ROOT.TH1F("h_had_b_4vec_pt_weight_cQj11", "b-quark from t_{Hadronic}; pT (GeV); Events", 50, 0, 1000)
h_had_b_4vec_eta_weight_cQj11 = ROOT.TH1F("h_had_b_4vec_eta_weight_cQj11", "b-quark from t_{Hadronic}; #eta; Events", 100, -5, 5)
h_had_b_4vec_phi_weight_cQj11 = ROOT.TH1F("h_had_b_4vec_phi_weight_cQj11", "b-quark from t_{Hadronic}; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass_weight_cQj11 = ROOT.TH1F("h_had_b_4vec_mass_weight_cQj11", "b-quark from t_{Hadronic}; Mass; Events", 50, 0, 10)

h_lepton_pt_weight_cQj11  = ROOT.TH1F("h_lepton_pt_weight_cQj11", "Lepton; pT (GeV); Events", 50, 0, 1000)
h_lepton_eta_weight_cQj11 = ROOT.TH1F("h_lepton_eta_weight_cQj11", "Lepton; #eta; Events", 100, -5, 5)
h_lepton_phi_weight_cQj11 = ROOT.TH1F("h_lepton_phi_weight_cQj11", "Lepton; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass_weight_cQj11 = ROOT.TH1F("h_lepton_mass_weight_cQj11", "Lepton; Mass; Events", 50, 0, 10)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# ctu1 (quadratic) weighted histograms
h_ttbarMass_weight_ctu1_quad = ROOT.TH1F("h_ttbarMass_weight_ctu1_quad", "ttbar system; Mass (GeV);Events", 150, 0, 3000)

h_had_b_4vec_pt_weight_ctu1_quad  = ROOT.TH1F("h_had_b_4vec_pt_weight_ctu1_quad", "b-quark from t_{Hadronic}; pT (GeV); Events", 50, 0, 1000)
h_had_b_4vec_eta_weight_ctu1_quad = ROOT.TH1F("h_had_b_4vec_eta_weight_ctu1_quad", "b-quark from t_{Hadronic}; #eta; Events", 100, -5, 5)
h_had_b_4vec_phi_weight_ctu1_quad = ROOT.TH1F("h_had_b_4vec_phi_weight_ctu1_quad", "b-quark from t_{Hadronic}; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass_weight_ctu1_quad = ROOT.TH1F("h_had_b_4vec_mass_weight_ctu1_quad", "b-quark from t_{Hadronic}; Mass; Events", 50, 0, 10)

h_lepton_pt_weight_ctu1_quad  = ROOT.TH1F("h_lepton_pt_weight_ctu1_quad", "Lepton; pT (GeV); Events", 50, 0, 1000)
h_lepton_eta_weight_ctu1_quad = ROOT.TH1F("h_lepton_eta_weight_ctu1_quad", "Lepton; #eta; Events", 100, -5, 5)
h_lepton_phi_weight_ctu1_quad = ROOT.TH1F("h_lepton_phi_weight_ctu1_quad", "Lepton; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass_weight_ctu1_quad = ROOT.TH1F("h_lepton_mass_weight_ctu1_quad", "Lepton; Mass; Events", 50, 0, 10)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# cQj11 (quadratic) weighted histograms
h_ttbarMass_weight_cQj11_quad = ROOT.TH1F("h_ttbarMass_weight_cQj11_quad", "ttbar system; Mass (GeV);Events", 150, 0, 3000)

h_had_b_4vec_pt_weight_cQj11_quad  = ROOT.TH1F("h_had_b_4vec_pt_weight_cQj11_quad", "b-quark from t_{Hadronic}; pT (GeV); Events", 50, 0, 1000)
h_had_b_4vec_eta_weight_cQj11_quad = ROOT.TH1F("h_had_b_4vec_eta_weight_cQj11_quad", "b-quark from t_{Hadronic}; #eta; Events", 100, -5, 5)
h_had_b_4vec_phi_weight_cQj11_quad = ROOT.TH1F("h_had_b_4vec_phi_weight_cQj11_quad", "b-quark from t_{Hadronic}; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass_weight_cQj11_quad = ROOT.TH1F("h_had_b_4vec_mass_weight_cQj11_quad", "b-quark from t_{Hadronic}; Mass; Events", 50, 0, 10)

h_lepton_pt_weight_cQj11_quad  = ROOT.TH1F("h_lepton_pt_weight_cQj11_quad", "Lepton; pT (GeV); Events", 50, 0, 1000)
h_lepton_eta_weight_cQj11_quad = ROOT.TH1F("h_lepton_eta_weight_cQj11_quad", "Lepton; #eta; Events", 100, -5, 5)
h_lepton_phi_weight_cQj11_quad = ROOT.TH1F("h_lepton_phi_weight_cQj11_quad", "Lepton; #phi; Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass_weight_cQj11_quad = ROOT.TH1F("h_lepton_mass_weight_cQj11_quad", "Lepton; Mass; Events", 50, 0, 10)
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

# Functions checking status flags of particles
#FLAGS = ['isPrompt', 'isDecayedLeptonHadron', 'isTauDecayProduct', 'isPromptTauDecayProduct', 'isDirectTauDecayProduct', 'isDirectPromptTauDecayProduct', 'isDirectHadronDecayProduct', 
#         'isHardProcess', 'fromHardProcess', 'isHardProcessTauDecayProduct', 'isDirectHardProcessTauDecayProduct', 'fromHardProcessBeforeFSR', 'isFirstCopy', 'isLastCopy', 'isLastCopyBeforeFSR']
#
# statusFlags is a 16-bit integer, where each bit indicates a specific flag
# the expression (statusFlags & (1 << n)) != 0 checks if the nth bit is set to 1
def is_last_copy(statusFlags):
    try:
        status_flags_int = int(statusFlags)
        return (status_flags_int & (1 << 13)) != 0 # (1 << n) indicates (n+1)th element in the list
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
    
## Processing particles ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*
def process_event(entry, histograms):
    # Initialize variables
    is_last_copy_particles, ishardprocess_partons, fromhardprocess_partons = [], [], [] # list of (4vector, pdgId) tuples
    
    top_4vec = ROOT.TLorentzVector()
    antitop_4vec = ROOT.TLorentzVector()
    tops = [] # list of (4vector, pdgId) tuples
    
    w_bosons = [] # list of 4vectors
    w_quarks_indices = [] # list of indices for quarks from W decay

    el_4vec = ROOT.TLorentzVector()
    mu_4vec = ROOT.TLorentzVector()
    leptons = [] # list of (4vector, pdgId) tuples

    had_b_4vec = ROOT.TLorentzVector()
    lep_b_4vec = ROOT.TLorentzVector()
    b_quarks = [] # list of (4vector, from_hadronically_decaying_top_boolean) tuples

    ## Linear EFT weights
    # ctu1
    weight_ctu1 = getattr(entry, "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")
    # cQj11
    weight_cQj11 = getattr(entry, "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")

    ## Quadratic EFT weights
    # ctu1
    weight_ctu1_quad = getattr(entry, "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_2p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")
    # cQj11
    weight_cQj11_quad = getattr(entry, "LHEWeight_ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_2p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p")
    
    # 1st loop over particles
    for i in range(entry.nGenPart):
        # Get particle properties
        pdgId = entry.GenPart_pdgId[i]
        pt = entry.GenPart_pt[i]
        eta = entry.GenPart_eta[i]
        phi = entry.GenPart_phi[i]
        mass = entry.GenPart_mass[i]
        statusFlags = entry.GenPart_statusFlags[i]

        # Check particle's statusFlag
        if is_last_copy(statusFlags):
            parton_4vec = ROOT.TLorentzVector()
            parton_4vec.SetPtEtaPhiM(pt, eta, phi, mass)
            is_last_copy_particles.append((parton_4vec, entry.GenPart_pdgId[i])) 
        
        if ishardprocess(statusFlags):
            parton_4vec = ROOT.TLorentzVector()
            parton_4vec.SetPtEtaPhiM(pt, eta, phi, mass)
            ishardprocess_partons.append((parton_4vec, entry.GenPart_pdgId[i])) 
        
        if fromHardProcess(statusFlags): 
            parton_4vec = ROOT.TLorentzVector()
            parton_4vec.SetPtEtaPhiM(pt, eta, phi, mass)
            fromhardprocess_partons.append((parton_4vec, entry.GenPart_pdgId[i]))
        
        # Check for last_copy top quarks ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*
        if abs(pdgId) == 6 and is_last_copy(statusFlags):
            top_index = i
            from_hadronic_Wdecay = False
            if pdgId == 6:
                top_4vec.SetPtEtaPhiM(entry.GenPart_pt[top_index], entry.GenPart_eta[top_index], entry.GenPart_phi[top_index], entry.GenPart_mass[top_index]) # <<<-* top quark
                tops.append((top_4vec, pdgId)) 
            else:
                antitop_4vec.SetPtEtaPhiM(entry.GenPart_pt[top_index], entry.GenPart_eta[top_index], entry.GenPart_phi[top_index], entry.GenPart_mass[top_index]) # <<<-* top antiquark
                tops.append((antitop_4vec, pdgId)) 

            # 2nd loop over all particles
            for j in range(entry.nGenPart):
                # Check if (Mother of this particle is the top quark found above) and (if this particle is a W boson) ----------------------------------------------------------------------------------------------------------*
                if entry.GenPart_genPartIdxMother[j] == top_index and abs(entry.GenPart_pdgId[j]) == 24:
                    Wboson_index = j
                    w_4vec = ROOT.TLorentzVector()
                    w_4vec.SetPtEtaPhiM(entry.GenPart_pt[Wboson_index], entry.GenPart_eta[Wboson_index], entry.GenPart_phi[Wboson_index], entry.GenPart_mass[Wboson_index]) # <<<-*--* W bosons
                    w_bosons.append(w_4vec)

                    # 3rd loop over all particles
                    for k in range(entry.nGenPart):
                        Wdaughter_index = k

                        # Check if W decays leptonically 
                        if entry.GenPart_genPartIdxMother[Wdaughter_index] == Wboson_index and abs(entry.GenPart_pdgId[Wdaughter_index]) == 11:
                            el_4vec.SetPtEtaPhiM(entry.GenPart_pt[Wdaughter_index], entry.GenPart_eta[Wdaughter_index], entry.GenPart_phi[Wdaughter_index], entry.GenPart_mass[Wdaughter_index]) # <<<-*--*---* electron 4vector
                            leptons.append((el_4vec, entry.GenPart_pdgId[Wdaughter_index]))
                        elif entry.GenPart_genPartIdxMother[Wdaughter_index] == Wboson_index and abs(entry.GenPart_pdgId[Wdaughter_index]) == 13:
                            mu_4vec.SetPtEtaPhiM(entry.GenPart_pt[Wdaughter_index], entry.GenPart_eta[Wdaughter_index], entry.GenPart_phi[Wdaughter_index], entry.GenPart_mass[Wdaughter_index]) # <<<-*--*---* muon 4vector
                            leptons.append((mu_4vec, entry.GenPart_pdgId[Wdaughter_index]))
                            
                        # Check if W decays hadronically
                        elif entry.GenPart_genPartIdxMother[Wdaughter_index] == Wboson_index and abs(entry.GenPart_pdgId[Wdaughter_index]) in [1, 2, 3, 4]:
                            from_hadronic_Wdecay = True # Now that we know this top quark (with index i) has decayed hadronically
                            w_quarks_indices.append(Wdaughter_index)

            # 4th loop over all particles
            for l in range(entry.nGenPart):
                # Check if (Mother of this particle is the top quark found above) and (if this particle is a b quark) ----------------------------------------------------------------------------------------------------------*
                if entry.GenPart_genPartIdxMother[l] == top_index and abs(entry.GenPart_pdgId[l]) == 5:
                    b_daughter = l
                    # Check if this b quark decayed from hadronically decaying top-mother
                    if from_hadronic_Wdecay:
                        had_b_4vec.SetPtEtaPhiM(entry.GenPart_pt[b_daughter], entry.GenPart_eta[b_daughter], entry.GenPart_phi[b_daughter], entry.GenPart_mass[b_daughter]) # <<<-*--*---*-----* HADRONIC b quark
                        b_quarks.append((had_b_4vec, from_hadronic_Wdecay))
                    elif not from_hadronic_Wdecay:
                        lep_b_4vec.SetPtEtaPhiM(entry.GenPart_pt[b_daughter], entry.GenPart_eta[b_daughter], entry.GenPart_phi[b_daughter], entry.GenPart_mass[b_daughter]) # <<<-*--*---*-----* leptonic b quark
                        b_quarks.append((lep_b_4vec, from_hadronic_Wdecay))

        else: 
            continue  
    ## Finished processing particles -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*
        
    # Check the event for correct number of decay products
    if len(w_quarks_indices) == 2 and len(b_quarks) == 2 and len(leptons) == 1:
        ## Filling lab frame histograms #-*--*---*-----*--------*-------------*---------------------*----------------------------------*
   
        # Hadronic b quarks
        histograms['h_had_b_4vec_pt'].Fill(had_b_4vec.Pt())
        histograms['h_had_b_4vec_eta'].Fill(had_b_4vec.Eta())
        histograms['h_had_b_4vec_phi'].Fill(had_b_4vec.Phi())
        histograms['h_had_b_4vec_mass'].Fill(had_b_4vec.M())
        # linear effects of ctu1
        histograms['h_had_b_4vec_pt_weight_ctu1'].Fill(had_b_4vec.Pt(), weight_ctu1)
        histograms['h_had_b_4vec_eta_weight_ctu1'].Fill(had_b_4vec.Eta(), weight_ctu1)
        histograms['h_had_b_4vec_phi_weight_ctu1'].Fill(had_b_4vec.Phi(), weight_ctu1)
        histograms['h_had_b_4vec_mass_weight_ctu1'].Fill(had_b_4vec.M(), weight_ctu1)
        # linear effects of cQj11
        histograms['h_had_b_4vec_pt_weight_cQj11'].Fill(had_b_4vec.Pt(), weight_cQj11)
        histograms['h_had_b_4vec_eta_weight_cQj11'].Fill(had_b_4vec.Eta(), weight_cQj11)
        histograms['h_had_b_4vec_phi_weight_cQj11'].Fill(had_b_4vec.Phi(), weight_cQj11)
        histograms['h_had_b_4vec_mass_weight_cQj11'].Fill(had_b_4vec.M(), weight_cQj11)
        # quadratic effects of ctu1
        histograms['h_had_b_4vec_pt_weight_ctu1_quad'].Fill(had_b_4vec.Pt(), weight_ctu1_quad)
        histograms['h_had_b_4vec_eta_weight_ctu1_quad'].Fill(had_b_4vec.Eta(), weight_ctu1_quad)
        histograms['h_had_b_4vec_phi_weight_ctu1_quad'].Fill(had_b_4vec.Phi(), weight_ctu1_quad)
        histograms['h_had_b_4vec_mass_weight_ctu1_quad'].Fill(had_b_4vec.M(), weight_ctu1_quad)
        # quadratic effects of cQj11
        histograms['h_had_b_4vec_pt_weight_cQj11_quad'].Fill(had_b_4vec.Pt(), weight_cQj11_quad)
        histograms['h_had_b_4vec_eta_weight_cQj11_quad'].Fill(had_b_4vec.Eta(), weight_cQj11_quad)
        histograms['h_had_b_4vec_phi_weight_cQj11_quad'].Fill(had_b_4vec.Phi(), weight_cQj11_quad)
        histograms['h_had_b_4vec_mass_weight_cQj11_quad'].Fill(had_b_4vec.M(), weight_cQj11_quad)

        # Leptons
        for lep_4vec, pdgId in leptons:
            histograms['h_lepton_pt'].Fill(lep_4vec.Pt())
            histograms['h_lepton_eta'].Fill(lep_4vec.Eta())
            histograms['h_lepton_phi'].Fill(lep_4vec.Phi())
            histograms['h_lepton_mass'].Fill(lep_4vec.M())
            # linear effects of ctu1
            histograms['h_lepton_pt_weight_ctu1'].Fill(lep_4vec.Pt(), weight_ctu1)
            histograms['h_lepton_eta_weight_ctu1'].Fill(lep_4vec.Eta(), weight_ctu1)
            histograms['h_lepton_phi_weight_ctu1'].Fill(lep_4vec.Phi(), weight_ctu1)
            histograms['h_lepton_mass_weight_ctu1'].Fill(lep_4vec.M(), weight_ctu1)
            # linear effects of cQj11
            histograms['h_lepton_pt_weight_cQj11'].Fill(lep_4vec.Pt(), weight_cQj11)
            histograms['h_lepton_eta_weight_cQj11'].Fill(lep_4vec.Eta(), weight_cQj11)
            histograms['h_lepton_phi_weight_cQj11'].Fill(lep_4vec.Phi(), weight_cQj11)
            histograms['h_lepton_mass_weight_cQj11'].Fill(lep_4vec.M(), weight_cQj11)
            # quadratic effects of ctu1
            histograms['h_lepton_pt_weight_ctu1_quad'].Fill(lep_4vec.Pt(), weight_ctu1_quad)
            histograms['h_lepton_eta_weight_ctu1_quad'].Fill(lep_4vec.Eta(), weight_ctu1_quad)
            histograms['h_lepton_phi_weight_ctu1_quad'].Fill(lep_4vec.Phi(), weight_ctu1_quad)
            histograms['h_lepton_mass_weight_ctu1_quad'].Fill(lep_4vec.M(), weight_ctu1_quad)
            # quadratic effects of cQj11
            histograms['h_lepton_pt_weight_cQj11_quad'].Fill(lep_4vec.Pt(), weight_cQj11_quad)
            histograms['h_lepton_eta_weight_cQj11_quad'].Fill(lep_4vec.Eta(), weight_cQj11_quad)
            histograms['h_lepton_phi_weight_cQj11_quad'].Fill(lep_4vec.Phi(), weight_cQj11_quad)
            histograms['h_lepton_mass_weight_cQj11_quad'].Fill(lep_4vec.M(), weight_cQj11_quad)

        # Top quarks
        for top_4vec, pdgId in tops:
            # top quarks
            if pdgId == 6:
                histograms['h_topPt'].Fill(top_4vec.Pt())
                histograms['h_topEta'].Fill(top_4vec.Eta())
                histograms['h_topPhi'].Fill(top_4vec.Phi())
                histograms['h_topMass'].Fill(top_4vec.M())
            # top antiquarks
            elif pdgId == -6:
                histograms['h_antitopPt'].Fill(antitop_4vec.Pt())
                histograms['h_antitopEta'].Fill(antitop_4vec.Eta())
                histograms['h_antitopPhi'].Fill(antitop_4vec.Phi())
                histograms['h_antitopMass'].Fill(antitop_4vec.M())

        # ttbar system
        if top_4vec and antitop_4vec:
            ttbar = top_4vec + antitop_4vec
            histograms['h_ttbarPt'].Fill(ttbar.Pt())
            histograms['h_ttbarEta'].Fill(ttbar.Eta())
            histograms['h_ttbarPhi'].Fill(ttbar.Phi())
            histograms['h_ttbarMass'].Fill(ttbar.M())
            histograms['h_ttbarMass_weight_ctu1'].Fill(ttbar.M(), weight_ctu1) # linear effects of ctu1
            histograms['h_ttbarMass_weight_cQj11'].Fill(ttbar.M(), weight_cQj11) # linear effects of cQj11
            histograms['h_ttbarMass_weight_ctu1_quad'].Fill(ttbar.M(), weight_ctu1_quad) # quadratic effects of ctu1
            histograms['h_ttbarMass_weight_cQj11_quad'].Fill(ttbar.M(), weight_cQj11_quad) # quadratic effects of cQj11
        ## Done filling lab frame histograms #-*--*---*-----*--------*-------------*---------------------*----------------------------------*

        ## Boost to CM frame


        ## Rotate away theta and phi


        ## Boost to parent top quark rest frame
        

        ## Construct Spin Correlation variables
            

    return tops, leptons, b_quarks, is_last_copy_particles
    ## Done filling histograms #-*--*---*-----*--------*-------------*---------------------*----------------------------------*
## End of processing particles ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*

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
    
    histograms = {
        # top quark
        'h_topPt': h_topPt,
        'h_topEta': h_topEta,
        'h_topPhi': h_topPhi,
        'h_topMass': h_topMass,
        # top antiquark
        'h_antitopPt': h_antitopPt,
        'h_antitopEta': h_antitopEta,
        'h_antitopPhi': h_antitopPhi,
        'h_antitopMass': h_antitopMass,
        # ttbar system
        'h_ttbarPt': h_ttbarPt,
        'h_ttbarEta': h_ttbarEta,
        'h_ttbarPhi': h_ttbarPhi,
        'h_ttbarMass' : h_ttbarMass,
        'h_ttbarMass_weight_ctu1' : h_ttbarMass_weight_ctu1, # linear effects of ctu1
        'h_ttbarMass_weight_cQj11' : h_ttbarMass_weight_cQj11, # linear effects of ctu1
        'h_ttbarMass_weight_ctu1_quad' : h_ttbarMass_weight_ctu1_quad, # quadratic effects of ctu1
        'h_ttbarMass_weight_cQj11_quad' : h_ttbarMass_weight_cQj11_quad, # quadratic effects of cQj11
        # hadronic b-quark
        "h_had_b_4vec_pt" : h_had_b_4vec_pt,
        "h_had_b_4vec_eta" : h_had_b_4vec_eta,
        "h_had_b_4vec_phi" : h_had_b_4vec_phi,
        "h_had_b_4vec_mass" : h_had_b_4vec_mass,
        # linear effects of ctu1
        "h_had_b_4vec_pt_weight_ctu1" :h_had_b_4vec_pt_weight_ctu1,
        "h_had_b_4vec_eta_weight_ctu1" : h_had_b_4vec_eta_weight_ctu1,
        "h_had_b_4vec_phi_weight_ctu1" : h_had_b_4vec_phi_weight_ctu1,
        "h_had_b_4vec_mass_weight_ctu1" : h_had_b_4vec_mass_weight_ctu1,
        # linear effects of cQj11
        "h_had_b_4vec_pt_weight_cQj11" : h_had_b_4vec_pt_weight_cQj11,
        "h_had_b_4vec_eta_weight_cQj11" : h_had_b_4vec_eta_weight_cQj11,
        "h_had_b_4vec_phi_weight_cQj11" : h_had_b_4vec_phi_weight_cQj11,
        "h_had_b_4vec_mass_weight_cQj11" : h_had_b_4vec_mass_weight_cQj11,
        # quadratic effects of ctu1
        "h_had_b_4vec_pt_weight_ctu1_quad" : h_had_b_4vec_pt_weight_ctu1_quad,
        "h_had_b_4vec_eta_weight_ctu1_quad" : h_had_b_4vec_eta_weight_ctu1_quad,
        "h_had_b_4vec_phi_weight_ctu1_quad" : h_had_b_4vec_phi_weight_ctu1_quad,
        "h_had_b_4vec_mass_weight_ctu1_quad" : h_had_b_4vec_mass_weight_ctu1,
        # quadratic effects of cQj11
        "h_had_b_4vec_pt_weight_cQj11_quad" : h_had_b_4vec_pt_weight_cQj11_quad,
        "h_had_b_4vec_eta_weight_cQj11_quad" : h_had_b_4vec_eta_weight_cQj11_quad,
        "h_had_b_4vec_phi_weight_cQj11_quad" : h_had_b_4vec_phi_weight_cQj11_quad,
        "h_had_b_4vec_mass_weight_cQj11_quad" : h_had_b_4vec_mass_weight_cQj11_quad,
        # lepton
        "h_lepton_pt" : h_lepton_pt,
        "h_lepton_eta" : h_lepton_eta,
        "h_lepton_phi" : h_lepton_phi,
        "h_lepton_mass" : h_lepton_mass,
        # linear effects of ctu1
        "h_lepton_pt_weight_ctu1" : h_lepton_pt_weight_ctu1,
        "h_lepton_eta_weight_ctu1" : h_lepton_eta_weight_ctu1,
        "h_lepton_phi_weight_ctu1" : h_lepton_phi_weight_ctu1,
        "h_lepton_mass_weight_ctu1" : h_lepton_mass_weight_ctu1,
        # linear effects of cQj11
        "h_lepton_pt_weight_cQj11" : h_lepton_pt_weight_cQj11,
        "h_lepton_eta_weight_cQj11" : h_lepton_eta_weight_cQj11,
        "h_lepton_phi_weight_cQj11" : h_lepton_phi_weight_cQj11,
        "h_lepton_mass_weight_cQj11" : h_lepton_mass_weight_cQj11,
        # quadratic effects of ctu1
        "h_lepton_pt_weight_ctu1_quad" : h_lepton_pt_weight_ctu1_quad,
        "h_lepton_eta_weight_ctu1_quad" : h_lepton_eta_weight_ctu1_quad,
        "h_lepton_phi_weight_ctu1_quad" : h_lepton_phi_weight_ctu1_quad,
        "h_lepton_mass_weight_ctu1_quad" : h_lepton_mass_weight_ctu1_quad,
        # quadratic effects of cQj11
        "h_lepton_pt_weight_cQj11_quad" : h_lepton_pt_weight_cQj11_quad,
        "h_lepton_eta_weight_cQj11_quad" : h_lepton_eta_weight_cQj11_quad,
        "h_lepton_phi_weight_cQj11_quad" : h_lepton_phi_weight_cQj11_quad,
        "h_lepton_mass_weight_cQj11_quad" : h_lepton_mass_weight_cQj11_quad
    }
    
    # Executes process_event, which processes the particles in each event
    for ientry, entry in enumerate(tree):
        if (ientry%100 == 0):
            print "EVENT:", ientry
        process_event(entry, histograms)
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

    print "Processed: {}".format(input_filename) 

       
print "Total number of events:", int(totalEvents) 
