#include "Play.hpp"
#include "Connector.hpp"
#include "map.hpp"
#include "unistd.h"
#include <iostream>


void Play::step(int socket, std::string massege) {
        // Cherez 4 goda zdec budet gorod sad i normalnay logica igr
    map Users_Play;
    if (users.find(socket) == users.end()) {
        users.insert(socket);
    }
    std::string name = Users_Play.get_name(socket);
    for (auto i : users) {
        if (i != socket) {
            if (Users_Play.is_here(i)) {
                Connector my_connector = Users_Play.get(i);
                my_connector.write(name + " : " + massege + "\n");
            } else {
                users.erase(i);
            }
        }
    }
}
