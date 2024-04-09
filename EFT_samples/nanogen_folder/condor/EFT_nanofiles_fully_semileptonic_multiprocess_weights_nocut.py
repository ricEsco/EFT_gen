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
h_topPt = ROOT.TH1F("h_topPt", "Top Quark pT ; pT (GeV);Events", 100, 0, 2000)
h_topEta = ROOT.TH1F("h_topEta", "Top Quark #eta ;#eta;Events", 100, -5, 5)
h_topPhi = ROOT.TH1F("h_topPhi", "Top Quark #phi ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_topMass = ROOT.TH1F("h_topMass", "Top Quark Mass ;Mass;Events", 50, 0, 500)

h_antitopPt = ROOT.TH1F("h_antitopPt", "Anti-Top Quark p_{T} ; p_{T} [GeV];Events", 100, 0, 2000)
h_antitopEta = ROOT.TH1F("h_antitopEta", "Anti-Top Quark #eta ;#eta;Events", 100, -5, 5)
h_antitopPhi = ROOT.TH1F("h_antitopPhi", "Anti-Top Quark #phi ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_antitopMass = ROOT.TH1F("h_antitopMass", "Anti-Top Quark Mass ;Mass;Events", 50, 0, 500)

h_ttbarPt = ROOT.TH1F("h_ttbarPt", "ttbar pT ; pT (GeV);Events", 100, 0, 2000)
h_ttbarEta = ROOT.TH1F("h_ttbarEta", "ttbar #eta ;#eta;Events", 100, -5, 5)
h_ttbarPhi = ROOT.TH1F("h_ttbarPhi", "ttbar #phi ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_ttbarMass = ROOT.TH1F("h_ttbarMass", "ttbar Mass; M (GeV);Events", 150, 0, 3000)

h_had_b_4vec_pt = ROOT.TH1F("h_had_b_4vec_pt", "Hadronic b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_had_b_4vec_eta = ROOT.TH1F("h_had_b_4vec_eta", "Hadronic b-quark #eta  ;#eta;Events", 100, -5, 5)
h_had_b_4vec_phi = ROOT.TH1F("h_had_b_4vec_phi", "Hadronic b-quark #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass = ROOT.TH1F("h_had_b_4vec_mass", "Hadronic b-quark Mass  ;Mass;Events", 50, 0, 10)

h_lepton_pt = ROOT.TH1F("h_lepton_pt", "Lepton pT ;pT (GeV);Events", 50, 0, 1000)
h_lepton_eta = ROOT.TH1F("h_lepton_eta", "Lepton #eta  ;#eta;Events", 100, -5, 5)
h_lepton_phi = ROOT.TH1F("h_lepton_phi", "Lepton #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass = ROOT.TH1F("h_lepton_mass", "Lepton Mass  ;Mass;Events", 50, 0, 10)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# ctu1 weighted histograms
h_ttbarMass_weight_ctu1 = ROOT.TH1F("h_ttbarMass_weight_ctu1", "ttbar Mass; M (GeV);Events", 150, 0, 3000)

h_had_b_4vec_pt_weight_ctu1  = ROOT.TH1F("h_had_b_4vec_pt_weight_ctu1", "Hadronic b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_had_b_4vec_eta_weight_ctu1 = ROOT.TH1F("h_had_b_4vec_eta_weight_ctu1", "Hadronic b-quark #eta  ;#eta;Events", 100, -5, 5)
h_had_b_4vec_phi_weight_ctu1 = ROOT.TH1F("h_had_b_4vec_phi_weight_ctu1", "Hadronic b-quark #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass_weight_ctu1 = ROOT.TH1F("h_had_b_4vec_mass_weight_ctu1", "Hadronic b-quark Mass  ;Mass;Events", 50, 0, 10)

h_lepton_pt_weight_ctu1  = ROOT.TH1F("h_lepton_pt_weight_ctu1", "Lepton pT ;pT (GeV);Events", 50, 0, 1000)
h_lepton_eta_weight_ctu1 = ROOT.TH1F("h_lepton_eta_weight_ctu1", "Lepton #eta  ;#eta;Events", 100, -5, 5)
h_lepton_phi_weight_ctu1 = ROOT.TH1F("h_lepton_phi_weight_ctu1", "Lepton #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass_weight_ctu1 = ROOT.TH1F("h_lepton_mass_weight_ctu1", "Lepton Mass  ;Mass;Events", 50, 0, 10)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# cQj11 weighted histograms
h_ttbarMass_weight_cQj11 = ROOT.TH1F("h_ttbarMass_weight_cQj11", "ttbar Mass; M (GeV);Events", 150, 0, 3000)

h_had_b_4vec_pt_weight_cQj11  = ROOT.TH1F("h_had_b_4vec_pt_weight_cQj11", "Hadronic b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_had_b_4vec_eta_weight_cQj11 = ROOT.TH1F("h_had_b_4vec_eta_weight_cQj11", "Hadronic b-quark #eta  ;#eta;Events", 100, -5, 5)
h_had_b_4vec_phi_weight_cQj11 = ROOT.TH1F("h_had_b_4vec_phi_weight_cQj11", "Hadronic b-quark #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass_weight_cQj11 = ROOT.TH1F("h_had_b_4vec_mass_weight_cQj11", "Hadronic b-quark Mass  ;Mass;Events", 50, 0, 10)

h_lepton_pt_weight_cQj11  = ROOT.TH1F("h_lepton_pt_weight_cQj11", "Lepton pT ;pT (GeV);Events", 50, 0, 1000)
h_lepton_eta_weight_cQj11 = ROOT.TH1F("h_lepton_eta_weight_cQj11", "Lepton #eta  ;#eta;Events", 100, -5, 5)
h_lepton_phi_weight_cQj11 = ROOT.TH1F("h_lepton_phi_weight_cQj11", "Lepton #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass_weight_cQj11 = ROOT.TH1F("h_lepton_mass_weight_cQj11", "Lepton Mass  ;Mass;Events", 50, 0, 10)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# ctu1 (quadratic) weighted histograms
h_ttbarMass_weight_ctu1_quad = ROOT.TH1F("h_ttbarMass_weight_ctu1_quad", "ttbar Mass; M (GeV);Events", 150, 0, 3000)

h_had_b_4vec_pt_weight_ctu1_quad  = ROOT.TH1F("h_had_b_4vec_pt_weight_ctu1_quad", "Hadronic b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_had_b_4vec_eta_weight_ctu1_quad = ROOT.TH1F("h_had_b_4vec_eta_weight_ctu1_quad", "Hadronic b-quark #eta  ;#eta;Events", 100, -5, 5)
h_had_b_4vec_phi_weight_ctu1_quad = ROOT.TH1F("h_had_b_4vec_phi_weight_ctu1_quad", "Hadronic b-quark #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass_weight_ctu1_quad = ROOT.TH1F("h_had_b_4vec_mass_weight_ctu1_quad", "Hadronic b-quark Mass  ;Mass;Events", 50, 0, 10)

h_lepton_pt_weight_ctu1_quad  = ROOT.TH1F("h_lepton_pt_weight_ctu1_quad", "Lepton pT ;pT (GeV);Events", 50, 0, 1000)
h_lepton_eta_weight_ctu1_quad = ROOT.TH1F("h_lepton_eta_weight_ctu1_quad", "Lepton #eta  ;#eta;Events", 100, -5, 5)
h_lepton_phi_weight_ctu1_quad = ROOT.TH1F("h_lepton_phi_weight_ctu1_quad", "Lepton #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass_weight_ctu1_quad = ROOT.TH1F("h_lepton_mass_weight_ctu1_quad", "Lepton Mass  ;Mass;Events", 50, 0, 10)
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------#

# cQj11 (quadratic) weighted histograms
h_ttbarMass_weight_cQj11_quad = ROOT.TH1F("h_ttbarMass_weight_cQj11_quad", "ttbar Mass; M (GeV);Events", 150, 0, 3000)

h_had_b_4vec_pt_weight_cQj11_quad  = ROOT.TH1F("h_had_b_4vec_pt_weight_cQj11_quad", "Hadronic b-quark pT ;pT (GeV);Events", 50, 0, 1000)
h_had_b_4vec_eta_weight_cQj11_quad = ROOT.TH1F("h_had_b_4vec_eta_weight_cQj11_quad", "Hadronic b-quark #eta  ;#eta;Events", 100, -5, 5)
h_had_b_4vec_phi_weight_cQj11_quad = ROOT.TH1F("h_had_b_4vec_phi_weight_cQj11_quad", "Hadronic b-quark #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_had_b_4vec_mass_weight_cQj11_quad = ROOT.TH1F("h_had_b_4vec_mass_weight_cQj11_quad", "Hadronic b-quark Mass  ;Mass;Events", 50, 0, 10)

h_lepton_pt_weight_cQj11_quad  = ROOT.TH1F("h_lepton_pt_weight_cQj11_quad", "Lepton pT ;pT (GeV);Events", 50, 0, 1000)
h_lepton_eta_weight_cQj11_quad = ROOT.TH1F("h_lepton_eta_weight_cQj11_quad", "Lepton #eta  ;#eta;Events", 100, -5, 5)
h_lepton_phi_weight_cQj11_quad = ROOT.TH1F("h_lepton_phi_weight_cQj11_quad", "Lepton #phi  ;#phi;Events", 30, -ROOT.TMath.Pi(), ROOT.TMath.Pi())
h_lepton_mass_weight_cQj11_quad = ROOT.TH1F("h_lepton_mass_weight_cQj11_quad", "Lepton Mass  ;Mass;Events", 50, 0, 10)
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
def process_event(entry, histograms):
    # Initialize variables
    top_count, antitop_count = 0, 0
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
    lep_4vec = ROOT.TLorentzVector()
    jets =[]
    top_4vec = None
    antitop_4vec = None
    top_related_parton_indices = set()

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

    ## Processing particless ------------------------------------------------------------------------------------------------------------------------------------------------------*
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
        if abs(pdgId) == 6 and is_last_copy(statusFlags):  # Check if particle is a (last_copy) top or antitop quark
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
    
            # For leptonically decaying top quarks -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------*
            if has_leptonic_w_decay:

                # Loop over all particles, again again
                for k in range(entry.nGenPart):

                    # Check if Mother of kth-particle is the W boson found above ---------------------------------------------------------------------------------------------------------------------------------------------*
                    if entry.GenPart_genPartIdxMother[k] == w_daughter:
                        top_related_parton_indices.add(k)

                        # Check if the kth-particle is an electron or muon ---------------------------------------------------------------------------------------------------------------------------------------*
                        if abs(entry.GenPart_pdgId[k]) in [11, 13]:
                            lep_4vec.SetPtEtaPhiM(entry.GenPart_pt[k], entry.GenPart_eta[k], entry.GenPart_phi[k], entry.GenPart_mass[k]) # <<<-*--*---*-----* lepton 4vector
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
                    # hadronic_w_mass = (quark1_vec + quark2_vec).M()
                    # if 65 < hadronic_w_mass < 95: # I include this line to ensure that the events are indeed hadronic W decays
                    #     histograms['h_hadronic_w_mass'].Fill(hadronic_w_mass)
                    #     histograms['h_hadronic_w_mass_weightSM'].Fill(hadronic_w_mass, weight_0)
                    #     histograms['h_hadronic_w_mass_ctGRe'].Fill(hadronic_w_mass, weight_ctGRe)
                        
        
            # b-quarks ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*
            if b_daughter is not None:
                b_vector = ROOT.TLorentzVector()
                b_vector.SetPtEtaPhiM(entry.GenPart_pt[b_daughter], entry.GenPart_eta[b_daughter], entry.GenPart_phi[b_daughter], entry.GenPart_mass[b_daughter])   
        
        else: 
            continue  
    ## Finished processing particles ---------------------------------------------------------------------------------------------------------------------------------------------*
        
    ## Filling histograms --------------------------------------------------------------------------------------------------------------------------------------------------------*
    if len(w_quarks_indices) == 2 and len(b_quarks) == 2:

        ## Plot coordinates of spin analysers in lab frame
        
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
                top_count += 1
                histograms['h_topPt'].Fill(top_4vec.Pt())
                histograms['h_topEta'].Fill(top_4vec.Eta())
                histograms['h_topPhi'].Fill(top_4vec.Phi())
                histograms['h_topMass'].Fill(top_4vec.M())
            # top antiquarks
            elif pdgId == -6:
                antitop_count += 1
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
            

    return tops, hadronic_top_pt, leptons, b_quarks, w_quarks1, w_quarks2, last_copy_partons
### End of process_event
#-*--*---*-----*--------*-------------*---------------------*----------------------------------*-------------------------------------------------------*-----------------------------------------------------------------------------------------#

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
        # if (ientry%100 == 0):
        #     print "EVENT:", ientry
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
