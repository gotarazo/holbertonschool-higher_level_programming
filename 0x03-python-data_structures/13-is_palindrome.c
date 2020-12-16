#include "lists.h"

/**
* reverse_listint - reverses a singly-linked listint_t list.
* @head: A pointer to the starting node of the list to reverse.
* Return: A pointer to the head of the reversed list.
*/

listint_t *reverse_listint(listint_t **head)
{
listint_t *node = *head, *next, *pr = NULL;

while (node)
{
next = node->next;
node->next = pr;
pr = node;
node = next;
}
*head = pr;
return (*head);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome
* @head: A pointer to the head of the linked list
* Return: If the list is not a palindrome 0 If the list is a palindrome 1
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
r = rerse_listint(&temp);
m = r;

temp = *head;
while (r)
{
if (temp->n != r->n)
return (0);
temp = temp->next;
r = r->next;
}
rerse_listint(&m);
return (1);
}
