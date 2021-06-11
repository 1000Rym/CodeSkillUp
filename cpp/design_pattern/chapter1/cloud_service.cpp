#include "cloud_service.h"

void UploadableFile::set_upload_size(int upload_size){
    this->uploaded_size = upload_size;
}

void CloudService::set_upload_file_size(UploadableFile& uploadable_file, int size){
    uploadable_file.set_upload_size(size);
}

void CloudService::get_upload_status(UploadableFile& uploadable_file){
    uploadable_file.print_uploaded_status(); 
}

void File::print_uploaded_status(){
    cout << "The file is uploaded about:"<<to_string(uploaded_size*100/size)<<endl;
}

void Music::print_uploaded_status(){
    cout << "The album is uploaded about:"<<to_string(uploaded_size*100/album_size)<<endl;
}

int main(){
    File file_a("FileA", 100);
    Music music_a("MusicA", 10);
    CloudService cloudService;
    cloudService.set_upload_file_size(file_a, 35);
    cloudService.get_upload_status(file_a);
    cloudService.set_upload_file_size(music_a, 5);
    cloudService.get_upload_status(music_a);
}