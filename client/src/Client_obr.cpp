#include "Client_obr.hpp"
#include <iostream>
#include <string>
#include <unistd.h>

Client_obr::Client_obr(int socket_for_read) : fd_for_read(socket_for_read) {}
int Client_obr::work(Connector server) {
    std::string users_message;
    std::cin >> users_message;
    if (users_message[0] == '_') {
        server.break_connection();
        return 1;
    }
    // place to play
    server.write_message(users_message);
    return 0;
}
