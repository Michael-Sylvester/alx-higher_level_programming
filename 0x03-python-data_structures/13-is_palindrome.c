#include "lists.h"

/**
 *is_palindrome - checks if the values in a linked list form a palindrome
 *@head : double pointer to the head of the list
 *Return : 1 if yes, 0 if no
*/
int is_palindrome(listint_t **head)
{
	int members[100];
	listint_t *temp = *head;
	int end = 0;
	int backward = 0;
	int forward = 0;
	
	if (*head == NULL)
		return (1);
	for (backward = 0; temp != NULL; backward++)
	{
		members[backward] = temp->n;
		temp = temp->next;
	}
	end = backward;
	backward--;

	while ( forward < end)
	{
		if (members[forward] != members[backward])
			return (0);
		forward++;
		backward--;
	}
	return (1);
}
