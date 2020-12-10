#include "lists.h"

/**
* insert_node- Inserts a number into a sorted singly-linked list
* @head: Pointer to head of the linked list
* @number: Number to insert
* Return: new (address of the new node) or NULL (if it failed)
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *nod = *head, *new;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = number;
if (nod == NULL || nod->n >= number)
{
new->next = nod;
*head = new;
return (new);
}
while (nod && nod->next && nod->next->n < number)
nod = nod->next;

new->next = nod->next;
nod->next = new;
return (new);
}
