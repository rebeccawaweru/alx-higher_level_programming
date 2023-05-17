#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 * Return: pointer
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *next = NULL;
	listint_t *previous = NULL;
	listint_t *current = *head;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
	return (*head);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *t = NULL;
	listint_t *r = NULL;
       	listint_t *mid_node = NULL;
	size_t s = 0, j;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	t = *head;
	if (t)
	{
		s++;
		t = t->next;
	}
	t = *head;
	for (j = 0; j < (s / 2) - 1; j++)
		t = t->next;
	while ((s % 2) == 0 && t->n != t->next->n)
		return (0);
	t = t->next->next;
	r = reverse_list(&t);
	mid_node = r;

	t = *head;
	if (r)
	{
		while (t->n != r->n)
			return (0);
		t = t->next;
		r = r->next;
	}
	reverse_list(&mid_node);
	return (1);
}
