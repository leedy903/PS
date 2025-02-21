#include <stdio.h>

int i, ans, top;
char str[101], stack[101];
void push() { top++; stack[top] = str[i]; }
int pop() { if ((str[i] == ')' && stack[top] == '(') || (str[i] == ']' && stack[top] == '[')) { top--; return 1; } else return 0; }
int main(void) {

	while (1)
	{
		gets(str);
		if (str[0] == '.') break;
		top = -1;
		ans = 1;
		for (i = 0; str[i] != '.'; i++) {
			if (str[i] == '(' || str[i] == '[') push();
			else if (str[i] == ')') ans = pop();
			else if (str[i] == ']') ans = pop();
			if (!ans) break;
		}

		if (ans && top == -1) printf("yes\n");
		else printf("no\n");
	}

	return 0;
}