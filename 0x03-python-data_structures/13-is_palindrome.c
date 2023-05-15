#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 * Return: pointer
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *next = NULL;
	listint_t *prev = NULL;
	listint_t *current = head;

	if (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *ptr_slow = *head;
	listint_t *ptr_fast = *head;
	listint_t *prev_slow = *head;
	listint_t *mid_node = NULL;
	int is_palindrome = 1;

	while (ptr_fast != NULL && ptr_fast->next != NULL)
	{
		ptr_fast = ptr_fast->next->next;
		prev_slow = ptr_slow;
		ptr_slow = ptr_slow->next;
	}
	if (ptr_fast != NULL)
	{
		mid_node = ptr_slow;
		ptr_slow = ptr_slow->next;
	}
	listint_t *second_half = ptr_slow;
	prev_slow->next = NULL;
	second_half = reverse_list(second_half);

	listint_t *ptr1 = *head;
	listint_t *ptr2 = second_half;

	while (ptr2 != NULL)
	{
		if (ptr1->n != ptr2->n)
		{
			is_palindrome = 0;
			break;
		}
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}
	second_half = reverse_list(second_half);
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	} else
	{
		prev_slow->next = second_half;
	}
	return (is_palindrome);
}
