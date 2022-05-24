#include "map.hpp"
#include <stdio.h>
#include <iostream>

std::map<int, int64_t>  map::my_map;

int map::count_of_copy = 0;

map::map(){
    count_of_copy += 1;
}

void map::insert(int socket, Connector connector) {
    Connector* my_ptr = new Connector(connector);
    my_map.insert({socket, (int64_t)my_ptr});
}

bool map::is_here(int socket) {
    return !(my_map.find(socket) == my_map.end());
}

Connector map::get(int socket) {
    return *((Connector*)my_map[socket]);
}


void map::erase(int socket) {
    delete (Connector*)my_map[socket];
    my_map.erase(socket);
}

map::~map(){
    count_of_copy -= 1;
    if (count_of_copy == 0) {
        for (auto i = my_map.begin(); i !=my_map.end(); i++) {
            delete (Connector*)(i->second);
        }
    }
}

void map::set_name(int socket, std::string name) {
    ((Connector*)my_map[socket])->set_name(name);
}

std::string map::get_name(int socket) const{
    return ((Connector*)my_map[socket])->get_name();
}
