#include<bits/stdc++.h>

using namespace std;

int main() {
    int a;
    cin >> a;
    long long sum = 0;
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < a; j++) {
            sum++;
        }
    }
    cout << sum << endl;
}