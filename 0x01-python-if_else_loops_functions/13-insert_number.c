#include "lists.h"
/**
 *insert_node - inserts a node
 *@head: sorted linked list;
 *@number: node data value
 *
 *Return: new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *node = malloc(sizeof(listint_t));

	if (!node)
		return(NULL);
	if (!*head)
		return (NULL);
	node->n = number;
	current = *head;
	if (number < current->n)
	{
		node->next = current;
		*head = node;
		return (*head);
	}
	if (!current->next && current->n != number)
	{
		(*head)->next = node;
		node->next = NULL;
		return (*head);
	}
	while (current->n < number && current->next)
	{
		if (current->next->n > number)
		{
			node->next = current->next;
			current->next = node;
			return (*head);
		}
		current = current->next;
	}
	if (node->n == current->n)
		return (*head);
	node->next = NULL;
	current->next = node;
	return (*head);
}
