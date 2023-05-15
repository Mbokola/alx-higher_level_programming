#include "lists.h"
/**
 *is_palindrome - checks if linked list is a palindrome
 *@head: pointer to the first node
 *
 *Return: 1 if True 0 if False
 */
int is_palindrome(listint_t **head)
{
	int i, j, *arr;
	listint_t *ptr;

	if (!*head)
		return (1);
	ptr = *head;
	for (i = 0; ptr->next; i++)
		ptr = ptr->next;
	ptr = *head;
	j = i;
	arr = malloc(sizeof(int) * i);
	if (!arr)
		exit(1);
	while (i)
	{
		arr[i] = ptr->n;
		ptr = ptr->next;
		i--;
	}
	arr[i] = ptr->n;
	ptr = *head;
	while (i < j)
	{
		if (arr[i] == ptr->n)
		{
			ptr = ptr->next;
			i++;
			continue;
		}
		free(arr);
		return (0);
	}
	free(arr);
	return (1);
}
