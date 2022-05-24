#include "Obr2.hpp"
#include <string>
#include "unistd.h"
#include <stdio.h>
#include "map.hpp"
#include "Connector.hpp"
#include <iostream>

int Obr2::obr_connector(int socket) {
    int flag_for_server;
    int count_of_byte;
    std::string row_message;
    map Users_Obr2;
    Connector my_connector = Users_Obr2.get(socket);
    row_message = my_connector.read();
    flag_for_server = (int)(row_message[0]);
    count_of_byte = (int)(row_message[1]);
    std::string obr_message = std::string(&row_message[2], count_of_byte);
    if (flag_for_server == 0) {
        Users_Obr2.set_name(socket, obr_message);
        std::cout << "\n"<<  obr_message << " has connected";
        fflush(stdout);
        play.step(socket, "___has connected___");
    }
    if (flag_for_server == 2) {
        if (count_of_byte != obr_message.size()) {
            throw "Problems in protocol size_of_buffer != count_of_read_byte";
        }
        play.step(socket, obr_message);
    }
    if (flag_for_server == 3) {
        std::string name = Users_Obr2.get_name(socket);
        std::cout << "\n"<< name << " has disconnected";
        play.step(socket, "___has disconnected___");
        fflush(stdout);
        return 1;
    }
    return 0;
}

