#include <TLorentzVector.h>
#include <TMath.h>
#include <TSystem.h>
#include <TSystemDirectory.h>
#include <TList.h>
#include <TFile.h>
#include <TTree.h>
#include <TH1F.h>
#include <TCanvas.h>

void fillTtbarMassHistogram(const char* filename, const char* treename, TH1F* histogram) {
    TFile* file = TFile::Open(filename);
    if (!file || file->IsZombie()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return;
    }

    TTree* tree = (TTree*)file->Get(treename);
    if (!tree) {
        std::cerr << "Error retrieving tree: " << treename << " from file: " << filename << std::endl;
        return;
    }

    const int maxParticles = 100; // Adjust as needed
    int nParticles;
    int pdgID[maxParticles];
    float px[maxParticles], py[maxParticles], pz[maxParticles], energy[maxParticles];

    tree->SetBranchAddress("nParticles", &nParticles);
    tree->SetBranchAddress("pdgID", pdgID);
    tree->SetBranchAddress("px", px);
    tree->SetBranchAddress("py", py);
    tree->SetBranchAddress("pz", pz);
    tree->SetBranchAddress("energy", energy);

    Long64_t nEvents = tree->GetEntries();
    for (Long64_t i = 0; i < nEvents; i++) {
        tree->GetEntry(i);
        
        TLorentzVector top, antitop;
        for (int j = 0; j < nParticles; j++) {
            if (pdgID[j] == 6) {  // PDG ID for top quark
                top.SetPxPyPzE(px[j], py[j], pz[j], energy[j]);
            } else if (pdgID[j] == -6) {  // PDG ID for anti-top quark
                antitop.SetPxPyPzE(px[j], py[j], pz[j], energy[j]);
            }
        }

        TLorentzVector ttbar = top + antitop;
        histogram->Fill(ttbar.M());  // Fill the histogram with the invariant mass
    }

    file->Close();
    delete file;
}

void plotTtbarMass(const char* dirPath, const char* treename) {
    TSystemDirectory dir(dirPath, dirPath);
    TList* files = dir.GetListOfFiles();

    // Define a histogram to store the ttbar masses (adjust bins and range as necessary)
    TH1F* hMass = new TH1F("hMass", "t#bar{t} Invariant Mass;Mass (GeV/c^{2});Events", 100, 0, 2000);

    if (files) {
        TSystemFile* sysFile;
        TString fname;
        TIter next(files);
        while ((sysFile = (TSystemFile*)next())) {
            fname = sysFile->GetName();
            if (!sysFile->IsDirectory() && fname.EndsWith(".root")) {
                TString fullPath = TString(dirPath) + "/" + fname;
                fillTtbarMassHistogram(fullPath.Data(), treename, hMass);
            }
        }
    }

    // Draw the histogram
    TCanvas* canvas = new TCanvas("canvas", "t#bar{t} Mass Distribution", 800, 600);
    hMass->Draw();
    canvas->SetLogy();  // Uncomment if you want a logarithmic y-axis

    // Save the histogram as an image
    canvas->SaveAs("ttbarMassDistribution.png");
}

// To run:
// .L plotTtbarMass.C
// plotTtbarMass("path/to/directory", "nameOfYourTree")
