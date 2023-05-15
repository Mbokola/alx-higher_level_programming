#include "lists.h"
/**
 *is_palindrome - checks if linked list is a palindrome
 *@head: pointer to the first node
 *
 *Return: 1 if True 0 if False
 */
int is_palindrome(listint_t **head)
{
	int i, j;
	listint_t *ptr = *head, *tmp = *head, *save_link, *tmp1, *current = *head;

	if (!*head)
		return (1);
	for (i = 0; ptr->next; i++)
		ptr = ptr->next;
	if (ptr->n != (*head)->n)
		return (0);
	if (ptr == *head)
		return (1);
	j = i / 2;
	while (j)
	{
		tmp = tmp->next;
		j--;
	}
	save_link = tmp->next;
	tmp1 = save_link->next;
	tmp->next = NULL;
	save_link->next = tmp;
	while (tmp1->next)
	{
		tmp = save_link;
		save_link = tmp1;
		tmp1 = tmp1->next;
		save_link->next = tmp;
	}
	tmp1->next = save_link;
	j = i / 2;
	while (j)
	{
		if (current->n == tmp1->n)
		{
			current = current->next;
			tmp1 = tmp1->next;
			j--;
			continue;
		}
		return (0);
	}
	return (1);
}
