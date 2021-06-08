#include "cloud_service.h"

void File::set_upload_size(int upload_size)
{
    this->uploaded_size = upload_size;
}

void File::print_uploaded_status(){
    cout << "The file's upload progress:" << to_string(uploaded_size*100/file_size)<<"%."<<endl;
}

void CloudService::set_upload_file_size(File& file, int size){
    file.set_upload_size(size);
}

void CloudService::get_upload_status(File& file){
    file.print_uploaded_status();
}

int main(){
    File file_a("FileA", 100);
    CloudService cloudService; 
    cloudService.set_upload_file_size(file_a, 35);
    cloudService.get_upload_status(file_a);
}