#include "Beginner.hpp"
#include "Connector.hpp"
#include "Init_connection.hpp"
#include "Obr1.hpp"
#include "wait.hpp"

int main(int argc, char *argv[]) {
    int socket = beginner(argv);
    Obr1 my_obr;
    Connector my_connector = my_obr.make_connection(socket);
    while (init_connection(my_connector)) {}
    wait(my_connector, socket);
}
