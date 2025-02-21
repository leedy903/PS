#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define False 0
#define True 1

typedef struct Node {
	int data;
	struct Node* next;
}Node;

typedef struct Queue {
	Node* front,* rear;
	int size;
}Queue;

void InitQueue(Queue* queue);
int IsEmpty(Queue* queue);
int QueueSize(Queue* queue);
int QueueFront(Queue* queue);
int QueueBack(Queue* queue);
void Enqueue(Queue* queue, int input_data);
int Dequeue(Queue* queue);

int main(void) {
	int i = 0;
	int N = 0, x = 0;
	char c[10];
	Queue queue;

	scanf("%d", &N);

	InitQueue(&queue);

	while (N--) {
		memset(c, 0, sizeof(c));
		scanf("%s", c);
		if (!strcmp(c, "push")) {
			scanf("%d", &x);
			Enqueue(&queue, x);
		}
		else if (!strcmp(c, "pop")) {
			printf("%d\n", Dequeue(&queue));
		}
		else if (!strcmp(c, "size")) {
			printf("%d\n", QueueSize(&queue));
		}
		else if (!strcmp(c, "empty")) {
			printf("%d\n", IsEmpty(&queue));
		}
		else if (!strcmp(c, "front")) {
			printf("%d\n", QueueFront(&queue));
		}
		else if (!strcmp(c, "back")) {
			printf("%d\n", QueueBack(&queue));
		}
		else {
			break;
		}
	}
	return 0;
}

void InitQueue(Queue* queue) {
	queue->front = queue->rear = NULL;
	queue->size = 0;
}

int IsEmpty(Queue* queue) {
	return queue->size == 0;
}

int QueueSize(Queue* queue) {
	return queue->size;
}

int QueueFront(Queue* queue) {
	if (IsEmpty(queue)) return -1;
	else return queue->front->data;
}

int QueueBack(Queue* queue) {
	if (IsEmpty(queue)) return -1;
	else return queue->rear->data;
}

void Enqueue(Queue* queue, int input_data) {
	Node* new = (Node*)malloc(sizeof(Node));
	new->data = input_data;
	new->next = NULL;

	if (IsEmpty(queue)) {
		queue->front = new;
	}
	else {
		queue->rear->next = new;
	}
	queue->rear = new;
	queue->size++;
}

int Dequeue(Queue* queue) {
	int data = -1;
	Node* temp;
	if (IsEmpty(queue)) return data;
	temp = queue->front;
	data = temp->data;
	queue->front = temp->next;
	free(temp);
	queue->size--;
	return data;
}