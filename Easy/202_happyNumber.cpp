//circle, different step length, if the same value is 1, then isHappy=true

int digitSquareSum(int n) {
    int sum = 0, tmp;
    while (n) {
        tmp = n % 10;
        sum = sum + tmp*tmp;
        n = n/10;
    }
    return sum;
}

bool isHappy(int n) {
    int i1 = n, i2 = digitSquareSum(n);
    while (i1 != i2) {
        i1 = digitSquareSum(i1);
        i2 = digitSquareSum(digitSquareSum(i2));
    }
    return i2 == 1;
}
    