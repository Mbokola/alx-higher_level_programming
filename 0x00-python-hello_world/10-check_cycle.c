#include "lists.h"
/**
 *check_cycle - checks if list is circular
 *@list: list in context
 *
 *Return: 1 if true 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *current = NULL;

	current = list->next;
	list->next = NULL;
	tmp = current;
	while (tmp->next)
	{
		if (tmp->next == list && !tmp->next->next)
		{
			list->next = current;
			return (1);
		}
		tmp = tmp->next;
	}
	list->next = current;
	return (0);
}
