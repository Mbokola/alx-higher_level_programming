#include "lists.h"
/**
 *check_cycle - checks if list is circular
 *@list: list in context
 *
 *Return: 1 if true 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *current = NULL;

	current = list->next;
	while (current->next)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return (0);
}
