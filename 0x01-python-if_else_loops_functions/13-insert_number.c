#include "lists.h"
/**
 * insert_node - Adds a new node to the head of the list
 * @head: double pointer to the head
 * @number: data to be placed in node
 * Return: NULL or the pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *temp = *head, *next_node = temp->next;

	if (new == NULL)
		return (NULL);
	
	new->n = number;
	
	if (*head == NULL || head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
		else if (number < temp->n)
		{
			new->next = temp;
			*head = new;
		}
	else
	{
		while (number > next_node->n)
		{
			temp = next_node;
			next_node = temp->next;
			if (next_node == NULL)
				break;
		}
		temp->next = new;
		new->next = next_node;
	}
	return (new);
}
