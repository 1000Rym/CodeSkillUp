#include "cloud_service.h"

void UploadableFile::set_upload_size(int upload_size){
    uploaded_size = upload_size;
}

void CloudService::set_upload_file_size(UploadableFile& uploadable_file, int size){
    uploadable_file.set_upload_size(size);
}

void CloudService::get_upload_status(UploadableFile& uploadable_file){
    uploadable_file.print_uploaded_status();
}

void File::print_uploaded_status(){
    cout<< "File Name: " << file_name << endl; 
    cout<< "File size: " << file_size << endl;
    cout<< "Uploaded size: " << uploaded_size << endl; 
}

int main(){
    File file_a("FileA", 24);
    CloudService cloudService;
    cloudService.set_upload_file_size(file_a, 35);
    cloudService.get_upload_status(file_a);
}