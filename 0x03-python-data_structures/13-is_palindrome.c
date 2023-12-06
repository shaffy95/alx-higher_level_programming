#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *value1 = *head, *value2 = *head, *value3 = *head, *value4 = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		value2 = value2->next->next;
		if (!value2)
		{
			value4 = value1->next;
			break;
		}
		if (!value2->next)
		{
			value4 = value1->next->next;
			break;
		}
		value1 = value1->next;
	}

	reverse_listint(&value4);

	while (value4 && value3)
	{
		if (value3->n == value4->n)
		{
			value4 = value4->next;
			value3 = value3->next;
		}
		else
			return (0);
	}

	if (!value4)
		return (1);

	return (0);
}
