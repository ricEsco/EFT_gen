#include <TSystem.h>
#include <TSystemDirectory.h>
#include <TList.h>
#include <TFile.h>
#include <TTree.h>
#include <TH1F.h>
#include <TCanvas.h>

Long64_t countEventsInFile(const char* filename, const char* treename) {
    TFile* file = TFile::Open(filename);
    if (!file || file->IsZombie()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return 0;
    }

    TTree* tree = (TTree*)file->Get(treename);
    if (!tree) {
        std::cerr << "Error retrieving tree: " << treename << " from file: " << filename << std::endl;
        return 0;
    }

    Long64_t nEvents = tree->GetEntries();
    file->Close();
    delete file;

    return nEvents;
}

void countAllEvents_hist(const char* dirPath, const char* treename) {
    TSystemDirectory dir(dirPath, dirPath);
    TList* files = dir.GetListOfFiles();

    Long64_t totalEvents = 0;

    if (files) {
        TSystemFile* sysFile;
        TString fname;
        TIter next(files);
        while ((sysFile = (TSystemFile*)next())) {
            fname = sysFile->GetName();
            if (!sysFile->IsDirectory() && fname.EndsWith(".root")) {
                TString fullPath = TString(dirPath) + "/" + fname;
                totalEvents += countEventsInFile(fullPath.Data(), treename);
            }
        }
    }

    // Now create a histogram with that data
    TH1F* hEvents = new TH1F("hEvents", "Total Number of Events; ;Number of Events", 1, 0, 1);
    hEvents->SetBinContent(1, totalEvents);

    // Draw the histogram
    TCanvas* canvas = new TCanvas("canvas", "Events Histogram", 800, 600);
    hEvents->Draw();

    // Save it as an image file
    canvas->SaveAs("totalEvents.png");
}
