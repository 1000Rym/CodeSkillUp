#include <iostream>
using namespace std; 

//First, there is a file class, the file could be upload to cloud service. 
class File{
    private: 
        string name;
        int file_size; 
        int uploaded_size;  
    public: 
        File(string name, int file_size): name(name), file_size(file_size), uploaded_size(0){};
        void set_upload_size(int upload_size);
        void print_uploaded_status();
};

//And then,  we want a music class, which can also upload to cloud service.
class CloudService{
    public: 
        void set_upload_file_size(File& file, int size);
        void get_upload_status(File& file);
};
