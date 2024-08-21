#include <iostream>
using namespace std;

const int MAXN = 1e5;
int a[MAXN];

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(0);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> a[i];

    long long int maxsum = a[0], ans = a[0];
    for (int i = 1; i < n; i++)
    {
        maxsum = max(maxsum + a[i], 1LL * a[i]);
        ans = max(ans, maxsum);
    }

    cout << ans << endl;
    return 0;
}