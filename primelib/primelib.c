#include "primelib.h"

#include "math.h"

__declspec(dllexport) int __cdecl is_prime(unsigned long long x)
{
	if (x == 1) return 0;
	return smallest_divisor(x) == x;
}

__declspec(dllexport) unsigned long long __cdecl smallest_divisor(unsigned long long x)
{
	if (x < 4) return x;
	unsigned long long max_divisor = (unsigned long long)sqrt((float)x) + 1;
	for (unsigned long long i = 2; i < max_divisor; i++) {
		if (x % i == 0) return i;
	}
	return x;
}
