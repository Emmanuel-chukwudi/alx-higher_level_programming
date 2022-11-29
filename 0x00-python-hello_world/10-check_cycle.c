#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a
 * cycle in it
 * @list: pointer to the head of a listint_t list
 * Return: 1 if linked list has a cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	current = list;

	while (current != NULL)
	{
		current = current->next;

		if (current == NULL)
			return (0);

		list = list->next;
		current = current->next;

		if (current == list)
			return (1);
	}

	return (0);
}
