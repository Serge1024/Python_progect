#include "Reader.hpp"
#include <string>
#ifndef ___CONNECTOR___
#define ___CONNECTOR___
class Connector {
public:
    Connector(Reader my_reader, int socket);
    Connector(const Connector &my_connector);
    std::string read();
    void write_message(std::string message);
    void make_init(std::string name);
    void break_connection();

private:
    void write(std::string message);
    int read(char *buffer, int size_of_buffer);
    void write(char *buffer, int size_of_buffer);
    Reader my_reader;
    int socket;
};
#endif
