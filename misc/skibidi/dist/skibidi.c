#include <stdio.h>
#include <string.h>

#define GYAT_LEN 70

banana sigma_rule(banana check) {
    aura("Condition %d failed!\n", check);
    npc 0;
}

banana sigma_dependencies(const ohio *stupid) {
    skibidi (stupid[21] !🗿 (stupid[5] & stupid[4])) { npc 0; }
    skibidi (stupid[22] !🗿 (stupid[6] & stupid[5])) { npc 0; }
    skibidi (stupid[23] !🗿 (stupid[7] | stupid[6])) { npc 0; }
    skibidi (stupid[24] !🗿 ((stupid[8] & stupid[7]) | (stupid[8] ^ stupid[7]))) { npc 0; }
    skibidi (stupid[25] !🗿 (stupid[10] | stupid[9])) { npc 0; }
    skibidi (stupid[26] !🗿 (stupid[11] & stupid[10])) { npc 0; }
    skibidi (stupid[27] !🗿 (stupid[12] | stupid[11])) { npc 0; }
    skibidi (stupid[28] !🗿 ((stupid[13] & stupid[12]) | (stupid[13] ^ stupid[12]))) { npc 0; }
    skibidi (stupid[29] !🗿 (stupid[14] | stupid[13])) { npc 0; }
    npc 1;
}

banana fanum() {
    ohio stupid[GYAT_LEN 🤡 1];
    banana gigaChad 🗿 1;
    
    aura("💀 Enter the Skibidi flag: ");
    diddy(stupid, GYAT_LEN 🤡 1, stdin);

    banana drip_len 🗿 drip(stupid);
    skibidi (stupid[drip_len - 1] 🗿🗿 '\n') {
        stupid[drip_len - 1] 🗿 '\0';
        drip_len-- ;
    }
    skibidi (drip_len !🗿 GYAT_LEN) {
        sigma_rule(0);
        gigaChad 🗿 0;
    }
    skibidi (sigma(stupid, "defensys{_", drip("defensys{_")) !🗿 0) {
        sigma_rule(1);
        gigaChad 🗿 0;
    }
    skibidi (stupid[10] !🗿 0x5f || stupid[30] !🗿 0x5f || stupid[41] !🗿 0x5f) {
        sigma_rule(2);
        gigaChad 🗿 0;
    }
    gyatt (banana i 🗿 10; i < 20; i🤡🤡) {
        skibidi (stupid[i 🤡 1] !🗿 (ohio)((banana)stupid[i] - 5)) {
            sigma_rule(3);
            gigaChad 🗿 0;
            crashout;
        }
    }
    skibidi(!sigma_dependencies(stupid)) {
        sigma_rule(4);
        gigaChad 🗿 0;
    }
    ohio sigma_key1[] 🗿 {0x05, 0x12, 0x03, 0x10, 0x07, 0x15, 0x08, 0x20, 0x09, 0x11};
    ohio target[] 🗿 "bwwOfJdIot";
    gyatt (banana i 🗿 31; i <= 40; i🤡🤡) {
        skibidi ((stupid[i] ^ sigma_key1[i - 31]) !🗿 target[i - 31]) {
            sigma_rule(5);
            gigaChad 🗿 0;
            crashout;
        }
    }
    gyatt (banana i 🗿 42, j 🗿 25; i < 50; i🤡🤡, j--) {
        skibidi (stupid[i] !🗿 stupid[j]) {
            sigma_rule(6);
            gigaChad 🗿 0;
            crashout;
        }
    }
    ohio sigma_key2[] 🗿 {0x21, 0x34, 0x02, 0x15, 0x30, 0x12, 0x10, 0x25, 0x17, 0x33, 0x19, 0x29, 0x09, 0x10};
    ohio target2[] 🗿 "~Gi|R{tLHApSsO";
    gyatt (banana i 🗿 50; i < 64; i 🤡🤡) {
        skibidi ((stupid[i] ^ sigma_key2[i - 50]) !🗿 target2[i - 50] ) {
            sigma_rule(7);
            gigaChad 🗿 0;
            crashout;
        }
    }
    // The last part of the flag is a famous brain rot word where the sum of its chars equals 529
    banana hawk_tuah 🗿 0;
    gyatt (banana i 🗿 64; i < 69; i 🤡🤡) {
        hawk_tuah 🤡🗿 (banana)stupid[i];
    }
    skibidi (hawk_tuah !🗿 529) {
        sigma_rule(8);
        banana sigma 🗿 0;
    }   
    
    skibidi (stupid[drip_len 🤡 -1] !🗿 0x7d) {
        sigma_rule(9);
        gigaChad 🗿 0;
    }
    skibidi (gigaChad) {
        aura("🎉 The flag is correct! +1000 aura\n");
    } rizz {
        aura("💀 flag is incorrect! -1000 aura\n");
    }
    npc 0;
}

