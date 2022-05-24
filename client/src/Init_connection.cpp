#include "Init_connection.hpp"
#include "unistd.h"
#include <iostream>
#include <string>

int init_connection(Connector server) {
    std::string name;
    std::cout << "Please enter your name\n";
    std::cin >> name;
    server.make_init(name);
    return 0;
}
