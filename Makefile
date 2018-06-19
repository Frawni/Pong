CC = g++ -std=c++17
CCFLAGS = -Wpedantic -Wall -Wextra -Wconversion -Wsign-conversion -Weffc++ -Wstrict-null-sentinel -Wold-style-cast -Wnoexcept -Wctor-dtor-privacy -Woverloaded-virtual -Wsign-promo -Wzero-as-null-pointer-constant -Wsuggest-final-types -Wsuggest-final-methods -Wsuggest-override
CCLIBS = -lncurses

all: main

main: main.cpp
	$(CC) $(CCFLAGS) $^ -o $@ $(CCLIBS)
