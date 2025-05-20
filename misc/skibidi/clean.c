#include <stdio.h>
#include <string.h>

#define FLAG_LEN 70

// Function to print validation error
int validate_rule(int check) {
    printf("Condition %d failed!\n", check);
    return 0;
}

// Function to validate flag from 21 to 29
int validate_dependencies(const char *flag) {
    if (flag[21] != (flag[5] & flag[4])) { return 0; }
    if (flag[22] != (flag[6] & flag[5])) { return 0; }
    if (flag[23] != (flag[7] | flag[6])) { return 0; }
    if (flag[24] != ((flag[8] & flag[7]) | (flag[8] ^ flag[7]))) { return 0; }
    if (flag[25] != (flag[10] | flag[9])) { return 0; }
    if (flag[26] != (flag[11] & flag[10])) { return 0; }
    if (flag[27] != (flag[12] | flag[11])) { return 0; }
    if (flag[28] != ((flag[13] & flag[12]) | (flag[13] ^ flag[12]))) { return 0; }
    if (flag[29] != (flag[14] | flag[13])) { return 0; }
    return 1;
}

int main() {
    char flag[FLAG_LEN + 1];
    int valid = 1;
    
    printf("Enter the flag: ");
    fgets(flag, FLAG_LEN + 1, stdin);

    // Remove newline character if present
    int len = strlen(flag);
    if (flag[len - 1] == '\n') {
        flag[len - 1] = '\0';
        len--;
    }
    // Check flag length
    if (len != FLAG_LEN) {
        validate_rule(0);
        valid = 0;
    }
    // Check flag prefix
    if (strncmp(flag, "defensys{_", strlen("defensys{_")) != 0) {
        validate_rule(1);
        valid = 0;
    }
    // '_' every 10 chars to separate words
    if (flag[10] != 0x5f || flag[30] != 0x5f || flag[41] != 0x5f) {
	validate_rule(2);
	valid = 0;
    }

    // Check specific condition between index 10 to 20 (shift)
    for (int i = 10; i < 20; i++) {
	    if (flag[i+1] != (char)((int)flag[i] - 5)) {
            validate_rule(3);
            valid = 0;
            break;
        }
    }

    // Check manually defined character constraints 21-29
	if(!validate_dependencies(flag)){
		validate_rule(4);
		valid = 0;
	}

    // XOR validation with predefined key for chars 30-40
    char xor_key1[] = {0x05, 0x12, 0x03, 0x10, 0x07, 0x15, 0x08, 0x20, 0x09, 0x11};
    char target[] = "bwwOfJdIot";
    for (int i = 31; i <= 40; i++) {
        if ((flag[i] ^ xor_key1[i - 31]) != target[i - 31]) {
            validate_rule(5);
            valid = 0;
            break;
        }
    }

    // Ensure chars from 42 to 50 match reversed chars from 17 to 25
    for (int i = 42, j = 25; i < 50; i++, j--) {
        if (flag[i] != flag[j]) {
            validate_rule(6);
            valid = 0;
            break;
        }
    }

    // XOR validation with predefined key for chars 50-64
    char xor_key2[] = {0x21, 0x34, 0x02, 0x15, 0x30, 0x12, 0x10, 0x25, 0x17, 0x33, 0x19, 0x29, 0x09, 0x10};
    char target2[] = "~Gi|R{tLHApSsO";
    for (int i = 50; i < 64; i++) {
        if ((flag[i] ^ xor_key2[i - 50]) != target2[i - 50] ) {
            validate_rule(7);
            valid = 0;
            break;
        }
    }
    
    // Calculate sum of ASCII values of brain_rot word
    int somme2 = 0;
    for (int i = 64;i<69;i++) {
        somme2 += (int)flag[i];

    }
    // Check if sum equals 529
    if (somme2 != 529) {
        validate_rule(8);
        int validate = 0;
    }   

    // Check flag suffix '}'
    if (flag[len - 1] != 0x7d) {
        validate_rule(9);
        valid = 0;
    }
    if (valid) {
        printf("Flag is correct!\n");
    } else {
        printf("Flag is incorrect!\n");
    }
    return 0;
}

