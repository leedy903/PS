#include <stdio.h>
#define MAX_ELEMENTS 100000
#define HEAP_FULL(n) (n == MAX_ELEMENTS - 1)
#define HEAP_EMPTY(n) (!n)
typedef struct {
	int key;
} element;
element heap[MAX_ELEMENTS];
int n = 0;
int abs(int a) {
	return a > 0 ? a : a * -1;
}
void insert_max_heap(element item, int *n) {
	int i;
	if (HEAP_FULL(*n)) {
		printf("The heap is full.\n");
	}
	i = ++(*n);
	while (((i != 1) && (abs(item.key) < abs(heap[i / 2].key))) || ((abs(item.key) == abs(heap[i / 2].key)) && (item.key <= heap[i / 2].key))) {   //원상태 item.key > heap[i / 2].key
		heap[i] = heap[i / 2];
		i /= 2;
	}
	heap[i] = item;
}
element delete_max_heap(int *n) {
	element item, tmp;
	if (HEAP_EMPTY(*n)) {
		item.key = 0;
		return item;
	}
	item = heap[1];
	tmp = heap[(*n)--];
	int parent = 1;
	int child = 2;
	while (child <= *n) {
		if (((child < *n) && (abs(heap[child].key) > abs(heap[child + 1].key)))
			|| ((abs(heap[child].key) == abs(heap[child + 1].key) && heap[child].key > heap[child + 1].key))) {   //원상태 heap[child].key < heap[child + 1].key
			child++;
		}
		if ((abs(tmp.key) < abs(heap[child].key)) || ((abs(tmp.key))== (abs(heap[child].key)) && tmp.key < heap[child].key)){      //원상태 tmp.key >= heap[child].key
			break;
		}
		heap[parent] = heap[child];
		parent = child;
		child *= 2;
	}
	heap[parent] = tmp;
	return item;
}
int main(void) {
	int T, i;
	element x;
	scanf("%d", &T);
	for (i = 0; i < T; i++) {
		scanf("%d", &x.key);
		if (x.key != 0) {
			insert_max_heap(x, &n);
		}
		else {
			printf("%d\n", delete_max_heap(&n));
		}
	}
	return 0;
}