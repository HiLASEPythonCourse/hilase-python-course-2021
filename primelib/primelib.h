#ifndef PRIMELIB_H
#define PRIMELIB_H

__declspec(dllexport) int __cdecl is_prime(unsigned long long x);
__declspec(dllexport) unsigned long long __cdecl smallest_divisor(unsigned long long x);

#endif