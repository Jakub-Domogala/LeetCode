#ifndef LISTNODE_H
#define LISTNODE_H

#include <iostream>
#include <vector>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void printList(ListNode *head);
ListNode *arr2List(vector<int> &arr);
void freeList(ListNode *head);
#endif // LISTNODE_H
