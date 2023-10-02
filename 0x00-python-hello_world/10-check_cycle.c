#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @head: head node
 *
 * Description: function find the loop in linked list
 * Return: @dress where we start./NULL.
 */

int check_cycle(listint_t *head)
{
	listint_t *hare;
	listint_t *tut;

	hare  = head;
	tut = head;
	if (hare && hare->next)
	{
		while (hare && hare->next)
		{
			tut = tut->next;
			hare = hare->next->next;
			if (hare == tut)
			{
				return (1);
			}
		}
	}
	return (0);
}
