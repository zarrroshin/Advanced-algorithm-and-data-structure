#include <iostream>

using namespace std;

long long gcd(long long a, long long b)
{
    return (b == 0LL ? a : gcd(b, a % b));
}

int main()
{
    long long a, b;
    cin >> a >> b;
    cout << gcd(a, b) << '\n';
    return 0;
}