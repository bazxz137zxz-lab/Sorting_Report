#include <bits/stdc++.h>
using namespace std;
using namespace chrono;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Đọc từ file gentest.txt thay cho stdin
    freopen("gentest.txt", "r", stdin);

    int T = 10;   // test muốn chạy (1 → 10)
    string line;

    // Bỏ qua các test trước đó
    for (int i = 1; i < T; ++i) {
        if (!getline(cin, line)) {
            cerr << "Khong du du test trong file\n";
            return 1;
        }
    }

    // Đọc test T
    if (!getline(cin, line)) {
        cerr << "Khong doc duoc test T\n";
        return 1;
    }

    // ===============================
    // Parse dữ liệu
    // ===============================
    vector<double> a;
    a.reserve(1'000'000);

    char* ptr = const_cast<char*>(line.c_str());
    while (*ptr) {
        char* end;
        double x = strtod(ptr, &end);
        if (ptr == end) {
            ++ptr;        // bỏ ký tự không hợp lệ
        } else {
            a.push_back(x);
            ptr = end;
        }
    }

    // ===============================
    // Đo thời gian sort
    // ===============================
    auto start = high_resolution_clock::now();
    sort(a.begin(), a.end());
    auto stop = high_resolution_clock::now();

    cout << "Test " << T << '\n';
    cout << "So phan tu: " << a.size() << '\n';
    cout << "Sort time: "
         << duration_cast<milliseconds>(stop - start).count()
         << " ms\n";

    return 0;
}
