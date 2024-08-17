#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    char input;
    scanf("%c", &input);
    int n = atoi(&input);
    if (n % 2 == 0 && n > 2) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    return 0;
}