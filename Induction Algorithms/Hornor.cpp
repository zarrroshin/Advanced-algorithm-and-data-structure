#include <iostream>
using namespace std;

const int MOD = 1e9 + 7;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n >> x;

    int a[n + 1];
    for (int i = 0; i <= n; i++)
        cin >> a[i];

    int value = 0;
    for (int i = 0; i <= n; i++)
        value = (1LL * value * x + a[i]) % MOD;

    cout << (value + MOD) % MOD << '\n';
    return 0;
}