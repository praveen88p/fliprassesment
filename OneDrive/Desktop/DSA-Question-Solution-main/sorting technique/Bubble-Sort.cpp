#include <bits/stdc++.h>
using namespace std;

int Bubble_Sort(int arr[] ,int n){

    for(int i = n-1;i>=0;i--){
        for(int j = 0;j<=i-1;j++){
        if(arr[j]>arr[j+1]){
            int temp = arr[j];
            arr[j]=arr[j+1];
            arr[j+1] = temp;
        }
        }
    }
}



int main() {
   


  int arr[5]={10,8,45,52,3};

    Bubble_Sort(arr,5);
    for(int i =0;i<5;i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}
