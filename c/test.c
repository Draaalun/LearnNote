   #include <stdio.h>
   #include <string.h>
   void quick_sort(int a[],int,int);
   int length;
   int main(){
       //int array[]={73,108,111,118,101,70,105,115,104,67,46,99,111,109};
   
       printf("plz input the array length:\n");
       scanf("%d",&length);
       printf("plz input array:\n");
       int array[length];
       for (int i = 0; i < length; i++)
       {
           scanf("%d",&array[i]);
       }
       for (int  count = 0; count<length; count++)
       {
       quick_sort(array,0,length-1);
       }
       for (int i = 0; i <length; i++)
       {
           printf("%d\t",array[i]);
       }
       return 0;
   }
   void quick_sort(int a[],int left,int right){
       int c=(int)(right+1)/2;
   
       int swapl=0;
       int swapr=0;
       do
       {
           int *l=&a[left];
           int *r=&a[right];
           if (*l>=a[c])
           {
               //l=&a[left];
               swapl=1;
           }
           else{
               left++;
               swapl=0;
           }
   
           if (a[right]<=a[c])
           {
               //r=&a[right];
               swapr=1;
           }
           else{
               right--;
               swapr=0;
           }
           if(swapl==1&&swapr==1){
               int temp;
               temp=*l;
               *l=*r;
               *r=temp;
           }  
       } 
       while (left<right);
   }
