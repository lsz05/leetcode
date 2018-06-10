int maxSubArray(vector<int>& nums) {
    int n=nums.size();
    if (n==0) return 0;
    int tmp,maxn;
    tmp=maxn=nums[0];
    for (int i=1;i<n;i++) {
       tmp = max(nums[i],tmp+nums[i]);
        maxn = max(tmp,maxn);
    }
    return maxn;
}