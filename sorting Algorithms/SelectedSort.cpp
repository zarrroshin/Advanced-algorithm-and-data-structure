#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];

    for (int i = 0; i < n; i++)
    {
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
            if (a[min_idx] > a[j])
                min_idx = j;

        swap(a[i], a[min_idx]);
    }

    for (int i = 0; i < n; i++)
        cout << a[i] << " \n"[i == n - 1];

    return 0;
}