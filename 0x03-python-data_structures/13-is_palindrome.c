#include "lists.h"
/**
 *is_palindrome- check if the singly list is palindrome
 *@head: head node
 *Return: 1 on failure, 0 on success
 */

int is_palindrome(listint_t **head)
{
	listint_t *value1 = *head;
	listint_t *value2 = *head;
	listint_t *prev  = NULL;
	listint_t *nextnode = NULL;
	int value = 0;

	while (value1 != NULL && value1->next != NULL)
	{	value1 = value1->next->next;
		value2 = value2->next;
		nextnode = value2->next;
		value2->next = prev;
		prev = value2;
		value2 = nextnode;
		value++;
	}

	if (value2 != NULL)
	{
		value2 = value2->next;
	}

	while (value2 != NULL)
	{
		if (value2->value != prev->value)
		{
			return (0);
		}
		value2 = value2->next;
		prev = prev->next;
	}
	return (1);
}
