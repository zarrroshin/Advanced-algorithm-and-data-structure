#include <bits/stdc++.h>
using namespace std;

void sort(int a[], int n)
{
    if (n == 0)
        return;
    sort(a, n - 1);
    int p = n - 1;
    while (p > 0 && a[p] < a[p - 1])
    {
        swap(a[p], a[p - 1]);
        p--;
    }
}

int main()
{
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
        cin >> a[i];

    sort(a, n);
    for (int i = 0; i < n; i++)
        cout << a[i] << ' ';
    cout << endl;
}

// #include <iostream>
// using namespace std;

// int main()
// {
//     int n;
//     cin >> n;
//     int a[n];
//     for (int i = 0; i < n; i++)
//     {
//         cin >> a[i];
//     }

//     for (int i = 0; i < n; i++)
//     {
//         int p = i;
//         while (p > 0 && a[p] < a[p - 1])
//         {
//             swap(a[p], a[p - 1]);
//             p = p - 1;
//         }
//     }
//     for (int i = 0; i < n; i++)
//     {
//         cout << a[i] << " ";
//     }
//     return 0;
// }