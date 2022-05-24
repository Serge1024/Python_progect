#include "Connector.hpp"
class Client_obr {
public:
    Client_obr(int socket_for_read);
    int work(Connector server);

private:
    int fd_for_read;
};
