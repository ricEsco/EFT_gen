#include <TSystem.h>
#include <TSystemDirectory.h>
#include <TList.h>
#include <TFile.h>
#include <TTree.h>

void countEventsInFile(const char* filename, const char* treename, Long64_t &totalEvents) {
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

    Long64_t nEvents = tree->GetEntries();
    totalEvents += nEvents;

    std::cout << "File: " << filename << ", Number of events in tree " << treename << ": " << nEvents << std::endl;

    file->Close();
    delete file;
}

void countAllEvents(const char* dirPath, const char* treename) {
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
                countEventsInFile(fullPath.Data(), treename, totalEvents);
            }
        }
    }

    std::cout << "\nTotal events in " << treename << " across all files: " << totalEvents << std::endl;
}
