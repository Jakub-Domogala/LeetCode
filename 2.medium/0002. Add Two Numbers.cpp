#include "utilities/ListNode.h"

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        int rest = 0;
        ListNode dummy;
        dummy.next = new ListNode(0);
        ListNode *rj = &dummy;
        ListNode *j1 = l1;
        ListNode *j2 = l2;
        while (j1 || j2 || rest > 0)
        {
            rest = rest + (j1 ? j1->val : 0) + (j2 ? j2->val : 0);
            // rest = j1->val + j2->val + rest;
            rj->next = new ListNode(rest % 10);
            rj = rj->next;
            rest /= 10;

            if (j1)
                j1 = j1->next;
            if (j2)
                j2 = j2->next;
        }
        return dummy.next;
    }
};

int main()
{
    Solution sol;

    vector<int> a = {2, 4, 5};
    vector<int> b = {5, 6, 4};
    ListNode *l1 = arr2List(a);
    ListNode *l2 = arr2List(b);
    ListNode *result = sol.addTwoNumbers(l1, l2);
    printList(result);

    a = {0};
    b = {1};
    l1 = arr2List(a);
    l2 = arr2List(b);
    result = sol.addTwoNumbers(l1, l2);
    printList(result);

    // Free memory
    freeList(l1);
    freeList(l2);
    freeList(result);

    return 0;
}