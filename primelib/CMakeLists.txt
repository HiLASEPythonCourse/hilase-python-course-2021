cmake_minimum_required (VERSION 3.8)
project ("primelib")
add_library (primelib SHARED "primelib.c" "primelib.h")

if (NOT WIN32)
	target_link_libraries(primelib m)
endif()
