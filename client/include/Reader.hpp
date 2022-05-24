#ifndef ___READER___
#define ___READER___
class Reader {
public:
    Reader(int fd);
    int read_inf(char *buffer, int size_of_buffer);
    void write_inf(char *buffer, int size_of_buffer);

private:
    int fd;
};
#endif
