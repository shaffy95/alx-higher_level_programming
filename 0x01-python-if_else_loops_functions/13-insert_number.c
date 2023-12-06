#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pynode = *head, *valuenode;

	valuenode = malloc(sizeof(listint_t));
	if (valuenode == NULL)
		return (NULL);
	valuenode->n = number;

	if (pynode == NULL || pynode->n >= number)
	{
		valuenode->next = pynode;
		*head = valuenode;
		return (valuenode);
	}

	while (pynode && pynode->next && pynode->next->n < number)
		pynode = pynode->next;

	valuenode->next = pynode->next;
	pynode->next = valuenode;

	return (valuenode);
}
