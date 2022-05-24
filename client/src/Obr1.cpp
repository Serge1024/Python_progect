#include "Obr1.hpp"
#include "Reader.hpp"
#include <fcntl.h>
#include <sys/epoll.h>
#include <unistd.h>

Connector Obr1::make_connection(int sock_for_add) {
    Reader my_reader(sock_for_add);
    Connector ans(my_reader, sock_for_add);
    return ans;
}
