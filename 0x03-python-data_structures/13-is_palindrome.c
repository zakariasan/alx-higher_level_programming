#include "lists.h"
/**
 * main - check the code for
 *
 * Return: Always 0.
 */

int is_palindrome(listint_t **head)
{ 
	listint_t *tmp = *head;
	listint_t *last = tmp;
	listint_t *half = NULL;

	while(last && last->next)
	{
		tmp = tmp->next;
		last= last->next->next;
	}

	last = NULL;
	while(tmp)
	{
		half = tmp->next;
		tmp->next = last;
		last = tmp;
		tmp = half;
	}
	half = *head;
	tmp = last;

	while (half && tmp)
	{
		if (half->n != tmp->n)
			return (0);
		half = half->next;
		tmp = tmp->next;
	}
	return (1);
} 
