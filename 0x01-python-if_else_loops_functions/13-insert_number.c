#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a nbr in sorted list listint_t list
 * @head: pointer to head of list
 * @number: number
 * Return: adress of nodes or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	while (current != NULL)
	{
		if ((current->n <= new->n && current->next->n > new->n) ||
				!current->next)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}


