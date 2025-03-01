#include <stdio.h>
#include <string.h>

#define MAX 100000

typedef struct stack_arr {
	int top;
	int Data[MAX];
} Stack;

void stack_init(Stack* pstack);
void push(Stack* pstack, int x);
void pop(Stack* pstack);

int main(void) {
	int k, x = 0;
	unsigned int total = 0;
	Stack stack;
    
	scanf("%d", &k);
	
    stack_init(&stack);
	
    while (k--) {
		scanf("%d", &x);
		if (x) push(&stack, x);
		else pop(&stack);
	}
	
    while (stack.top != -1) {
		total += (unsigned int)stack.Data[stack.top--];
	}
	
    printf("%u", total);
	
    return 0;
}

void stack_init(Stack* pstack) {
	pstack->top = -1;
	memset(pstack->Data, 0, sizeof(pstack->Data));
}
void push(Stack* pstack, int x) {
	pstack->top++;
	pstack->Data[pstack->top] = x;
}
void pop(Stack* pstack) {
	pstack->top--;
}