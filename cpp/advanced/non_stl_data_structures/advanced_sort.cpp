#include <iostream>
#include <time.h>

using namespace std;

 //Generate number from 1~100, 10 times
void generateNumbers(int *numbers, int array_size){ 
    for (int i = 0 ; i< array_size; i++){
        numbers[i] = rand()%100 +1;
    }
}

// Display numbers.  
void displayNumbers(int *numbers, int array_size){
    for(int i=0; i< array_size; i ++){
        cout << numbers[i] << " ";
    }
    cout<< endl; 
}

void selectionSort(int *numbers, int array_size){
    for (int i =0; i < array_size; i ++){
        int smallestNumber = numbers[i];
        int position = i; 
        for(int j = i+1 ; j<array_size; j++){
            // If current number is smaller than previous smaller number, 
            // So change, smallest number and position.
            if(numbers[j] < smallestNumber) {
                position = j;
                smallestNumber = numbers[j];
             
            }
        }
        // Smallest number found in above process.
        // swap process is required. 
        if(i != position){
            numbers[position] = numbers[i];
            numbers[i] = smallestNumber;
        } 
        displayNumbers(numbers, array_size); 
    }  
}

//Insertion sort algorithm
void insertionSort(int *numbers, int array_size){
    int temp = 0; // will use extra O(1) space.
    for (int i =1 ; i  < array_size ; i++){
        // sort part. 
        for(int j = i ; j > 0 ; j--){
            //If current number is greater than previous number exchange 
            if (numbers[j] < numbers[j-1]){  
                temp = numbers[j];
                numbers[j] = numbers[j-1];
                numbers[j-1] = temp;
            }else{ // no need to exchange.
                break;  
            }
        }
    } 
}

//Bubble sort algorithm
void bubbleSort(int *numbers, int array_size){
    int temp = 0;
    for (int i = 0 ; i< array_size; i ++) {
        for (int j = 0; j< array_size; j ++){
            if(numbers[j] > numbers[j+1]){
                temp = numbers[j];
                numbers[j] = numbers[j+1];
                numbers[j+1] = temp;
            }
        }
    }
}

//void shell sort algorithm
void shellSort(int *numbers, int array_size){
    int temp = 0; // will use extra O(1) space.
    int gap = array_size;
    while(gap != 1) {
        gap /=2;  // gap sequentially reduce by half.

        for (int i = 0 ; i < array_size-gap; i++){
            // swap node and node+gap 
            if(numbers[i] > numbers[i+gap]){
                temp = numbers[i];
                numbers[i] = numbers[i+gap];
                numbers[i+gap] = temp;
            }
        }
    } 
}

void merge(int *numbers,int array_size,int first_pos, int middle_pos ,int end_pos){
    int sort_numbers[array_size]; // temp extra memeory is required.

    int i = first_pos; 
    int j = middle_pos+1; 
    int k = first_pos;

    // When value i is smaller than middle posistion. 
    // Compare divided two group put larger element in the sorted_numbers.
    while(i<=middle_pos && j<end_pos) {
        if(numbers[i] < numbers[j]){
            sort_numbers[k++] = numbers[i++];
        }else{
            sort_numbers[k++] = numbers[j++];
        }
    }

    // Copy remain value.
    // If first group i remained, i should be less than middle. 
    while (i<=middle_pos) {
        sort_numbers[k++] = numbers[i++];
    }
    // If second goup j is remained, j should be less than end position.
    while (j< end_pos){
        sort_numbers[k++] = numbers[j++];
    }

    // If all process ends, swap sorted_numbers with original numbers. 
    for (int l = first_pos ; l < end_pos; l++){
        numbers[l] = sort_numbers[l];
    }
}

// merge sort
void mergeSort(int *numbers, int array_size, int first_pos, int end_pos){
    int middle_pos;

    if(first_pos < end_pos){
        // Divide if first position is larger than last.
        middle_pos = (first_pos + end_pos)/2;
        mergeSort(numbers, array_size ,first_pos, middle_pos);
        mergeSort(numbers, array_size ,middle_pos+1, end_pos);
        merge(numbers,array_size ,first_pos, middle_pos, end_pos);
    }

}

int main(){
    const int array_size = 10; 
    int numbers[array_size]; 
    srand(time(NULL));
    generateNumbers(numbers, array_size);
    displayNumbers(numbers, array_size);
    //selectionSort(numbers, array_size);
    //insertionSort(numbers, array_size);
    //bubbleSort(numbers, array_size);
    //shellSort(numbers, array_size);
    mergeSort(numbers, array_size, 0, array_size);
    displayNumbers(numbers, array_size);
}