#include "Reader.hpp"
#include <unistd.h>

Reader::Reader(int fd) : fd(fd) {}
int Reader::read_inf(char *buffer, int size_of_buffer) {
    return read(fd, buffer, size_of_buffer);
}
void Reader::write_inf(char *buffer, int size_of_buffer) {
    write(fd, buffer, size_of_buffer);
}
