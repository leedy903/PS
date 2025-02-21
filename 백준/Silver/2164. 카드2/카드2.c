#include <stdio.h>
#include <stdlib.h>

typedef struct Card {
	int num;
	struct Card* next;
} Card;

typedef struct Queue {
	Card* front,* rear;
	int size;
} Queue;

void InitQueue(Queue* queue) {
	queue->front = queue->rear = NULL;
	queue->size = 0;
}

int IsEmtpy(Queue* queue) {
	return queue->size == 0;
}

void Enqueue(Queue* queue, int data) {
	Card* card = (Card*)malloc(sizeof(Card));
	if (!card) return -1;
	card->num = data;
	card->next = NULL;

	if (IsEmtpy(queue)) {
		queue->front = card;
	}
	else {
		queue->rear->next = card;
	}
	queue->rear = card;
	queue->size++;
}

int Dequeue(Queue* queue) {
	int data = -1;
	Card* temp;
	if (IsEmtpy(queue)) return data;
	temp = queue->front;
	data = temp->num;
	queue->front = temp->next;
	free(temp);
	queue->size--;
	return data;
}

int main(void) {
	int N = 0;
	int i = 0, deq = 0;
	Queue queue;

	scanf("%d", &N);
	
	InitQueue(&queue);
	for (i = 0; i < N; i++) Enqueue(&queue, i + 1);
	
	while (queue.size != 1) {
		Dequeue(&queue);
		deq = Dequeue(&queue);
		Enqueue(&queue, deq);
	}
	
	printf("%d", queue.front->num);

	return 0;
}

