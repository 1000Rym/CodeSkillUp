#include <iostream>
using namespace std; 


class UploadableFile{
    protected: 
        int uploaded_size;
        string file_name; 
        int file_size; 
      
    public: 
        UploadableFile (string file_name, int size)
            :file_name(file_name), file_size(size), uploaded_size(0){};

        void set_upload_size(int upload_size);
        virtual void print_uploaded_status() = 0;
};

//Here is the cloud service which can directly mange the server to up load the file.
class CloudService{
    public: 
        void set_upload_file_size(UploadableFile& file, int size);
        void get_upload_status(UploadableFile& file);
};


//First, there is a file class, the file could be upload to cloud service. 
class File : public UploadableFile{
    private: 
        string name;
        int file_size; 
    public: 
        File(string name, int file_size): UploadableFile(name, file_size){};
        //override function from the Uploadable File. 
        void print_uploaded_status();
};




