int arrangeCoins(int n) {
    int i=1;
    while (n-i>=0){
        n=n-i;
        i+=1;
    }
    return  i-1;
}