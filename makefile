# Compiler and flags
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++11 -O2

# Source files
SRCS = main.cpp add.cpp subtract.cpp multiply.cpp divide.cpp

# Object files
OBJS = $(SRCS:.cpp=.o)

# Executable name
TARGET = calculator

.PHONY: all clean run

# Default target: build the executable
all: $(TARGET)

# Link object files to create executable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compile source files to object files
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up build files
clean:
	rm -f $(OBJS) $(TARGET)

# Build and run the program
run: all
	./$(TARGET)
