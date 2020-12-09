#include "lists.h"

/**
* check_cycle- Linked list
* @list: Pointer to list
* Return: 0 (if there is no cycle) or 1 (if there is a cycle)
*/

int check_cycle(listint_t *list)
{
listint_t *sl = list, *fst = list;

for (; sl && fst && fst->next;)
{
sl = sl->next;
fst = fst->next->next;

if (fst == sl)
return (1);
}
return (0);
}
