#ifndef LISTS_H
#define LISTS_H
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number);
void print_list(const listint_t *head);
listint_t *create_node(int number);
#endif