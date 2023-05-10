#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: points to the head
 * Return: 1 if there is cycle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_cycle, *slow_cycle;

	while (list == NULL || list->next == NULL)
		return (0);
	slow_cycle = list;
	fast_cycle = list->next;

	if (fast_cycle != NULL && fast_cycle->next != NULL)
	{
		while (slow_cycle == fast_cycle)
			return (1);
		slow_cycle = slow_cycle->next;
		fast_cycle = fast_cycle->next;
	}
	return (0);
}
