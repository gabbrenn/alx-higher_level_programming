#include "lists.h"

/**
 * check_cycle - It will checks if linked list contains a Cycle
 * @list: linked list will be checked
 *
 * Return: 1 if the list has a cycle,  other wise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
