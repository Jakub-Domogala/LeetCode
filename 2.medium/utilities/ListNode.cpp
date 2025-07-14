#include "ListNode.h"

void printList(ListNode *head)
{
    while (head != nullptr)
    {
        std::cout << head->val << " -> ";
        head = head->next;
    }
    std::cout << "nullptr" << std::endl;
}

ListNode *arr2List(vector<int> &arr)
{
    ListNode dummy;
    ListNode *current = &dummy;
    for (int val : arr)
    {
        current->next = new ListNode(val);
        current = current->next;
    }
    return dummy.next;
}

void freeList(ListNode *head)
{
    while (head)
    {
        ListNode *tmp = head;
        head = head->next;
        delete tmp;
    }
}