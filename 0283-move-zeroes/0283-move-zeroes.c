void moveZeroes(int* nums, int numsSize) {
    int i=0,j;
    int temp = 0;
    
    for(i=0;i<numsSize;i++){
        if(nums[i] != 0){
            temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            j++;
        }
    }
}