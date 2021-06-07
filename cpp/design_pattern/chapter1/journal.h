#include <iostream>
#include <vector>
#include <fstream>

using namespace std;
struct Journal
{
    string title;
    int count = 0; 
    vector<string> entries;

    void add(const string& entry);
    //void save();
    explicit Journal(const string& title) : title(title){}
};

struct Writer
{
    Journal journal; 
    void save();
    explicit Writer(const Journal journal) : journal(journal){}
};

