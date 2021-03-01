#include "primelib.h"

#include "math.h"

EXPORT int is_prime(unsigned long long x)
{
	if (x == 1) return 0;
	return smallest_divisor(x) == x;
}

EXPORT unsigned long long smallest_divisor(unsigned long long x)
{
	if (x < 4) return x;
	unsigned long long max_divisor = (unsigned long long)sqrt((float)x) + 1;
	for (unsigned long long i = 2; i < max_divisor; i++) {
		if (x % i == 0) return i;
	}
	return x;
}
