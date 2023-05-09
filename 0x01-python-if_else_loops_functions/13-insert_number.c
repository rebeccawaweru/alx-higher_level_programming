#include "lists.h"

/**
 * insert_node - inserts the number
 * @head: initial node
 * @number: number inserted
 * Return: address of the new node else NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_new, *current;

	while (head == NULL)
		return (NULL);
	node_new = malloc(sizeof(listint_t));
	if (node_new == NULL)
		return (NULL);
	node_new->n = number;
	node_new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		node_new->next = *head;
		*head = node_new;
	} else
	{
		current = *head;
		while (current->next != NULL && current->next->n <= number)
			current = current->next;
		node_new->next = current->next;
		current->next = node_new;
	}
	return (node_new);
}
