#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *scrub, *shrub;

	if (list == NULL || list->next == NULL)
		return (0);

	scrub = list->next;
	shrub = list->next->next;

	while (scrub && shrub && shrub->next)
	{
		if (scrub == shrub)
			return (1);

		scrub = scrub->next;
		shrub = shrub->next->next;
	}

	return (0);
}
