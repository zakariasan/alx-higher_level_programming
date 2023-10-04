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
	if (!current)
	{
		*head = new;
		return (new);
	}
	while (current != NULL)
	{
		if (current->n >= new->n)
		{
			new->next = current;
			*head = new;
			return (new);
		}
		else if (!current->next)
			return (add_nodeint_end(head, number));
		else if ((current->n <= new->n))
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}
