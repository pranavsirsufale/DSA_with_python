#include<iostream>
#include<queue>
using namespace std;

void showPriorityQueue(priority_queue<int>pq){
    priority_queue<int> q = pq;
    while (!q.empty())
    {   
        /* code */
        cout <<q.top() << " ";
        q.pop();
    }
    cout<<endl;
}



int main(){
priority_queue<int>q;
q.push(10);
q.push(-3);
q.push(7);
q.push(8);

showPriorityQueue(q);

}