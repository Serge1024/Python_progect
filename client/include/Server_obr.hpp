#include "Connector.hpp"

class Server_obr {
public:
    Server_obr(Connector connector);
    int work(int user_fd);

private:
    Connector my_connector;
};
