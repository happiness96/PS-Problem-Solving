#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
/*
 ---------------------------- 
 | Created by happiness96   | 
 | Year 2020                | 
 | Month 08                 | 
 | Day 02                   | 
 | 2822 점수 계산             | 
 ---------------------------- 
*/

int main(){
    vector <pair <int, int>> scores;

    for(int i = 1; i < 9; i ++){
        int sc;

        cin >> sc;

        scores.push_back(make_pair(sc, i));
    }

    sort(scores.begin(), scores.end());

    int total = 0;
    int index[5];

    for(int i = 3; i < 8; i ++){
        total += scores[i].first;
        index[i - 3] = scores[i].second;
    }

    sort(index, index + 5);

    cout << total << '\n';
    for(auto ind : index) cout << ind << " ";

    return 0;
}
