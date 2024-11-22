#include <iostream>
#include <climits>  // For INT_MIN and INT_MAX

class Solution {
public:
    int reverse(int x) {
        int sign = 1;
        if (x < 0) {
            sign = -1;
        }

        int final = 0;
        int digit;
        while (x != 0) {
            digit = x % 10;
            // Check if reversing will cause overflow
            if (final > INT_MAX / 10 || (final == INT_MAX / 10 && digit > 7)) {
                return 0;  // Return 0 if overflow would occur
            }
            if (final < INT_MIN / 10 || (final == INT_MIN / 10 && digit < -8)) {
                return 0;  // Return 0 if overflow would occur
            }
            final = final * 10 + digit;
            x = x / 10;
        }
        int num=final*sign;
        return num*sign;
    }
};
