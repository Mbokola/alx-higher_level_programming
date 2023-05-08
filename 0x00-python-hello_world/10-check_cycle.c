#include "lists.h"
/**
 *check_cycle - checks if list is circular
 *@list: list in context
 *
 *Return: 1 if true 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t  *tmp, *current = NULL;

	current = list;
	tmp = list;
	while (current && tmp && tmp->next)
	{
		current = current->next;
		tmp = tmp->next->next;
		if (current == tmp)
			return (1);
	}
	return (0);
}
