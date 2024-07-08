#include <stdio.h>
int main(){

int c=(int)(right+1)/2;

    int swapl;
    int swapr;
    for (left,right ; left>= right;)
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
        else{
            continue;
        }
    } 
    for (int i = 0; i <=right; i++)
    {
        printf("%d\t",a[i]);
    }
}