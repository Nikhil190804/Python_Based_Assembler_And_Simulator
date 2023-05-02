#include <stdio.h>
int partition(int A[],int low,int high){
    int pivot=A[low];
    int i =low+1;
    int j=high;
    int temp;
    do{

    
        while (A[i]<=pivot){
            i++;

        }
        while (A[j]<=pivot){
            j--;

        }
        if (i<j){
            temp=A[i];
            A[i]=A[j];
            A[j]=temp;
        }
    }while (j>i);
    temp=A[low];
    A[low]=A[j];
    A[j]=temp;
    return j;
}
void quicksort(int A[],int low,int high ){
    int partition_index;
    if (low<high){
        partition_index=partition(A,low,high);
        quicksort(A,low,partition_index-1);
        quicksort(A,partition_index+1,high); 

    }
    
}
int main(){
    int A[]={1,4,2,3,7,5,9,8,10};
    int n=9;
    int low=0;
    int high=n-1;
    quicksort(A,low,high);
    for (int l=0;l<9;l++){
        printf("%d",A[l]);
    }
}