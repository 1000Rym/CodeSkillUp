#include <iostream>
using namespace std; 


class UploadableFile{
    protected: 
        int uploaded_size;
      
    public: 
        UploadableFile (int size) : uploaded_size(0){};

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
        int size; 
    public: 
        File(string name, int size): name(name),size(size), 
        UploadableFile(size){};
        //override function from the Uploadable File. 
        void print_uploaded_status();
};

//Second, we Created music.
class Music : public UploadableFile{
    private: 
        string album_name; 
        int album_size; 
    public: 
        Music(string album_name, int album_size): album_name(album_name), album_size(album_size), 
        UploadableFile(album_size){};
        void print_uploaded_status();
};
