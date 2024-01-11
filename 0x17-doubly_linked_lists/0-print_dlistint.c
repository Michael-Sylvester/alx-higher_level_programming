#include "lists.h"
/**
 *size_t print_dlistint - prints all the elements of a list
 * @h : the head of the list
 * 
 * Return: nothing
 */
size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *temp = (dlistint_t *)h;
	int count = 0;
	
	if (h == NULL)
		return (0);
	else
	{
		printf("%d\n", h->n);
		count++;
		temp = h->next;
	}
	while (temp != NULL)
	{
		printf("%d\n", temp->n);
		temp = temp->next;
		count++;
	}
	

	return count;
}
