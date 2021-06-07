#include "journal.h"

void Journal::add(const string& entry){ 
    this->count ++;
    this->entries.push_back(entry);
}

/*
Move Journal's save part to writer based on single responsibilty principle. 
void Journal::save(){
    ofstream ofs(this->title);
    for(auto& s : entries)
        ofs << s << endl; 
}
*/

void Writer::save(){
    ofstream ofs(this->journal.title);
    for(auto& s : journal.entries)
        ofs << s << endl;
}

int main(){
    cout<<"print journal"<<endl;
    Journal journal("MyDiary");
    journal.add("This");
    journal.add("is");
    journal.add("my");
    journal.add("diary.");
    Writer writer(journal);
    writer.save();
}