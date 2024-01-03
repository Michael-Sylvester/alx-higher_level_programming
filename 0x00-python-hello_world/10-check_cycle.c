#include "lists.h"
/**
 *check_cycle - checks if a singly linked list has a cycle in it
 *@list: Pointer to the first member of the list
 *
 *Return: 1 is there isa cycle and 0 if not
  */
int check_cycle(listint_t *list)
{
	listint_t *head_link = list;
	listint_t *temp = list;
	listint_t *next_link = temp->next;

	while (next_link != NULL)
	{
		if (next_link == head_link)
			return (1);
		temp = next_link;
		next_link = temp->next;
	}

	return (0);
}
