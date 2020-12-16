#include "lists.h"

/**
* reverse_listint- Reverses a singly-linked listint_t list
* @head: Pointer to the starting node of the list to reverse
* Return: Pointer to the head of the reversed list
*/

listint_t *reverse_listint(listint_t **head)
{
listint_t *nod = *head, *next, *p = NULL;

while (nod)
{
next = nod->next;
nod->next = p;
p = nod;
nod = next;
}
*head = p;
return (*head);
}

/**
* is_palindrome- Checks if a singly linked list is a palindrome
* @head: Pointer to the head of the linked list
* Return: 0 (If list is not a palindrome) or 1 (If list is a palindrome)
*/

int is_palindrome(listint_t **head)
{
listint_t *temp, *r, *m;
size_t size = 0, i;

if (*head == NULL || (*head)->next == NULL)
return (1);

temp = *head;
while (temp)
{
size++;
temp = temp->next;
}

temp = *head;
for (i = 0; i < (size / 2) - 1; i++)
temp = temp->next;

if ((size % 2) == 0 && temp->n != temp->next->n)
return (0);

temp = temp->next->next;
r = reverse_listint(&temp);
m = r;

temp = *head;
while (r)
{
if (temp->n != r->n)
return (0);
temp = temp->next;
r = r->next;
}
reverse_listint(&m);
return (1);
}
