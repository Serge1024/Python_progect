#include <map>
#include "Connector.hpp"
#include <string>
#ifndef ___MAP___
#define ___MAP___
class map
{
    public:
    map();
    void insert(int socket, Connector);
    Connector get(int socket);
    void erase(int socket);
    bool is_here(int socket);
    void set_name(int socket, std::string name);
    std::string get_name(int socket) const;
    ~map();
    private:
        static std::map<int, int64_t>  my_map;
        static int count_of_copy;
};
#endif
