// Author: Forest.1000
// Date: 2021.01.18
// Description: This code is made for learning associative containers. 

#include <iostream>
#include <set>
#include <map>

using namespace std; 

void testSet(){
    set<int> sset; //instantiation a integer type set container
    sset.insert(80);
    sset.insert(70);
    sset.insert(60);
    sset.insert(100);
    sset.insert(70);
    sset.insert(90);

    sset.erase(60); //erase 60.

    set<int> :: iterator miterator;
    
    //70 80 90 100 
    for (miterator = sset.begin() ; miterator != sset.end(); miterator ++){
        cout << *miterator << " "; 
    }
    cout <<endl;
}

void testMultiSet(){
    multiset<int> mset; //instantiation a integer type set container
    mset.insert(80);
    mset.insert(70);
    mset.insert(60);
    mset.insert(60);
    mset.insert(100);
    mset.insert(70);
    mset.insert(90);

    set<int> :: iterator miterator;
    
    //60 60 70 70 80 90 100 
    for (miterator = mset.begin() ; miterator != mset.end(); miterator ++){
        cout << *miterator << " "; 
    }
    cout <<endl;
}

void testMap(){
    map <string, int> scoreBoard; 
    pair <string, int>  person1("forest", 80);
    pair <string, int>  person2("carl",90);
    pair <string, int>  person3 = make_pair("maggie", 100);
    scoreBoard["maria"] = 95; 
    scoreBoard["forest"] = 90; //reset socre of forest.
    scoreBoard.insert(person1);
    scoreBoard.insert(person2);
    scoreBoard.insert(person3);

    map< string, int >::iterator iter; 
    for (iter = scoreBoard.begin() ; iter!=scoreBoard.end(); iter++){
        cout << iter->first<<":" <<iter->second<<endl; //print key values
    }

}

void testMultiMap(){
    multimap <string, int> scoreBoard; 
    pair <string, int>  person1("forest", 80);
    pair <string, int>  person2("carl",90);
    pair <string, int>  person3 = make_pair("maggie", 100);
    pair <string, int>  person4 = make_pair("carl", 100);
    pair <string, int>  person5 = make_pair("maria", 80);

    //scoreBoard["maria"] = 95;  not working

    //carl:90
    //carl:100
    //forest:80
    //maggie:100
    //maria:80
  
    scoreBoard.insert(person1);
    scoreBoard.insert(person2);
    scoreBoard.insert(person3);
    scoreBoard.insert(person4);
    scoreBoard.insert(person5);

    map< string, int >::iterator iter; 
    for (iter = scoreBoard.begin() ; iter!=scoreBoard.end(); iter++){
        cout << iter->first<<":" <<iter->second<<endl; //print key values
    }

}


int main(){ 
    cout<<"Testing Associative Containers."<<endl;
    //testSet();
    //testMultiSet();
    //testMap();
    testMultiMap();
}