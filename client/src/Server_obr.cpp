#include "Server_obr.hpp"
#include <iostream>
#include <string>
#include <unistd.h>

int size_buffer = 4096;
Server_obr::Server_obr(Connector connector) : my_connector(connector){};
int Server_obr::work(int user_fd) {
    //Place to play
    std::cout << my_connector.read() << "\n";
    return 0;
}
