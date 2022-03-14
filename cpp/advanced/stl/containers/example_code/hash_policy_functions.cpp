/*
    This code is made for learning hash policy functions used by unordered_set, unordered_multiset, etc.
    1. load_factor
    2. max_load_factor
    3. rehash
    4. reserve

    - What is the load factor?
        - The load facotor is the ratio between the number of elements and the number of buckets.
            - load_factor = element_size/bucket_count
            - Higher load_factor higher probability of collision in hash table.
*/

#include<iostream>
#include<unordered_set>

using namespace std;

int main(){
    unordered_set<string> my_set = {"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    
    // 1. load_factor: Return the load factor.
    // > load_factor: 0.727273
    cout << "load_factor: " << my_set.load_factor() << endl;

    // 2. max_load_factor: Get or Set the maximum load factor(By default max_load_factor is 1.0).
    // 2.1 Get the max load factor.
    // > max_load_factor: 1
    my_set = {};
    float current_max_load_factor = my_set.max_load_factor(); 
    cout << "max_load_factor: " << current_max_load_factor << endl;

    // 2.2 Set the max load factor.
    // > changed max_load_factor: 0.5
    my_set.max_load_factor(current_max_load_factor/2);
    cout << "changed max_load_factor: " << my_set.max_load_factor() << endl;

    /* 3. rehash:  Set the number of the buckets in the container.
        > bucket_count original: 23
        > bucket_count after rehash(30): 31 (Bucket size increased to value+1)
    */
    my_set = {"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    cout << "bucket_count original: " << my_set.bucket_count() << endl;
    my_set.rehash(30);
    cout << "bucket_count after rehash(30): " << my_set.bucket_count() << endl;

    // 4. reserve: Set the number of buckets to the most appropriate to contain at lease n elements.
    // > bucket count after reserve(8): 17 (2n +1)
    my_set.reserve(8);
    cout << "bucket count after reserve(8): " << my_set.bucket_count() << endl;

}


