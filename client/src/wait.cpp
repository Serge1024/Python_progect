#include "wait.hpp"
#include "Client_obr.hpp"
#include "Server_obr.hpp"
#include <arpa/inet.h>
#include <errno.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/epoll.h>
#include <sys/signalfd.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

const int size_of_array = 20;
const int size_of_queue = 128;
const int size_of_buffer = 8192;

int flag_of_work = 1;
void wait(Connector server, int server_socket) {
    int user_socket = 0;// to read
    int user_socket_write = 1;
    Client_obr client_obr(0);
    Server_obr server_obr(server);
    int flag = fcntl(server_socket, F_GETFL);
    flag = flag | FIOSETOWN;
    fcntl(server_socket, F_SETFL, flag);
    flag = fcntl(user_socket, F_GETFL);
    flag = flag | FIOSETOWN;
    fcntl(user_socket, F_SETFL, flag);
    int fd = epoll_create1(0);
    struct epoll_event my_epoll;
    my_epoll.events = EPOLLIN;
    struct epoll_event array_this_events[size_of_array];
    my_epoll.data.fd = server_socket;
    epoll_ctl(fd, EPOLL_CTL_ADD, server_socket, &my_epoll);
    my_epoll.data.fd = user_socket;
    epoll_ctl(fd, EPOLL_CTL_ADD, user_socket, &my_epoll);
    while (flag_of_work) {
        int count_of_event_now =
                epoll_wait(fd, array_this_events, size_of_array, -1);
        for (int i = 0; i < count_of_event_now; i++) {
            if (array_this_events[i].data.fd == server_socket) {
                server_obr.work(user_socket_write);
            } else {
                if (client_obr.work(server) == 1) {
                    flag_of_work = 0;
                }
            }
        }
    }
    close(fd);
    close(server_socket);
}
