#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * create_node - create a new node to insert
 * @number: integer
 */
listint_t *create_node(int number)//insert new node
{
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;
    return (new_node);
}
/**
 * insert_node - insert node in a linked list
 * @head: points to the head of the node
 * @number: an integer
 */
listint_t *insert_node(listint_t **head, int number)//insert node in a linked list
{
    listint_t *new_node = create_node(number);
1   if (new_node == NULL)
        return (NULL);
    if (*head == NULL || (*head)->n >= number)//list is empty or new node should be inserted at the beginning
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }
    listint_t *current = *head;//traverse list to find proper insertion point
    while(current->next != NULL && current->next->n < number)
    {
        current = current->next;
    }
    new_node->next = current->next;//insert new node in the correct position
    current->next = new_node;
    return (new_node);
}
/**
 * print_list - print the list
 * @head: points to the head of the node
 */
void print_list(const listint_t *head)//prints the list for testing
{
    while (head != NULL)
    {
        printf("%d -> ", head->n);
        head = head->next;
    }
    printf("NULL\n");
}
