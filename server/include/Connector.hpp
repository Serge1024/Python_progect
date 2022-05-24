#include "Reader.hpp"
#include <string>
#ifndef ___CONNECTOR___
#define ___CONNECTOR___


class Connector
{
    public:
        Connector (Reader my_reader, int socket);
        Connector (const Connector& my_connector);
        
        std::string read();

        void write(std::string message);
       
        std::string get_name() const;

        void set_name(std::string name);

   private:
        int read(char* buffer, int size_of_buffer);

        void write(char* buffer, int size_of_buffer);

        int get_socket();

        Reader my_reader;
        int socket;
        std::string name = "Define name";
};
#endif
