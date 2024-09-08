#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 *
 * Return: 0 f there's no cycle, 1 if there's a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;// move slow by one step
        fast = fast->next->next;// move fast two steps
        if (slow == fast)// if the pointers meet there's a cycle
        {
            return (1);
        }
    }
    return (0);// no cycle detected
}