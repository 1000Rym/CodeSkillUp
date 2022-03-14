/*
This code is made for learning bucket functions used by unordered_set, unordered_multiset, etc.
- 1. bucket_count
- 2. max_bucket_count
- 3. bucket_size
- 4. bucket

- What is the bucket?
    - Bucket is a slot in the container's internal hash table, which elements are assigned based on their hash value.
*/
#include <iostream>
#include <unordered_set>

using namespace std;

int main(){
    unordered_set<string> my_set = {"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    
    // >  Uranus Venus Mars Jupiter Earth Neptune Saturn Mercury (Unordered set stores values with unordered)
    for (auto element : my_set){
        cout << element << " "; 
    }
    cout << endl;
    
    // 1.bucket_count: Return count of the bucket.
    // > bucket_count:11
    int bucket_count = my_set.bucket_count();
    cout << "bucket_count:" << bucket_count << endl;

    /* Print the bucket status: 
        > bucket #0:
        > bucket #1:Venus Mars Jupiter 
        > bucket #2:
        > bucket #3:
        > bucket #4:Uranus 
        > bucket #5:
        > bucket #6:
        > bucket #7:Neptune Saturn Mercury 
        > bucket #8:Earth 
        > bucket #9:
        > bucket #10
    */
    for (int i = 0 ; i < bucket_count; i ++){
        cout << "bucket #" << i << ":";
        for(auto it = my_set.begin(i); it!= my_set.end(i); it++){
            cout << *it << " ";
        }
        cout << endl;
    }


    // 2. max_bucket_count: Return the maximum number of the buckets that the container might have.
    // > max_bucket_count: 461168601842738790
    cout << "max_bucket_count: "<< my_set.max_bucket_count() << endl;
    
    /* 3. bucket_size: Return the number of the elements in the bucket(n)
        > bucket #0's zie:0
        > bucket #1's zie:3
        > bucket #2's zie:0
        > bucket #3's zie:0
        > bucket #4's zie:1
        > bucket #5's zie:0
        > bucket #6's zie:0
        > bucket #7's zie:3
        > bucket #8's zie:1
        > bucket #9's zie:0
        > bucket #10's zie:0
    */
    for(int i = 0 ; i < bucket_count; i ++){
        cout << "bucket #" << i << "'s zie:"<< my_set.bucket_size(i)<< endl;        
    }

    /* 4. bucket: Return the bucket number where the element is located.
        > Uranus is located in bucket #4
        > Venus is located in bucket #1
        > Mars is located in bucket #1
        > Jupiter is located in bucket #1
        > Earth is located in bucket #8
        > Neptune is located in bucket #7
        > Saturn is located in bucket #7
        > Mercury is located in bucket #7
    */
    for (string element : my_set){
        cout << element << " is located in bucket #" << my_set.bucket(element) << endl;    
    }
}