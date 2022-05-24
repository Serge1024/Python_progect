#include "Connector.hpp"
#include "Obr2.hpp"
#include "map.hpp"
#include "obr1.hpp"
#include <arpa/inet.h>
#include <errno.h>
#include <fcntl.h>
#include <iostream>
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
#include "helper.hpp"
const int size_of_array = 20;
const int size_of_queue = 128;
const int size_of_buffer = 8192;

int Helper::get_sock_for_SIGTERM() {
    sigset_t set_these_signal;
    sigemptyset(&set_these_signal);
    sigaddset(&set_these_signal, SIGTERM);
    sigprocmask(SIG_SETMASK, &set_these_signal, NULL);
    return signalfd(-1, &set_these_signal, SFD_NONBLOCK);
}

int Helper:: get_main_sock(int port) {
    char IP[] = "127.0.0.1";
    struct sockaddr_in adr;
    memset(&adr, 0, sizeof(adr));
    int main_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (main_sock == -1) {
        perror("Problem these opening socket");
        _exit(1);
    }
    adr.sin_family = AF_INET;
    adr.sin_port = htons(port);
    adr.sin_addr.s_addr = inet_addr(IP);
    if (bind(main_sock, (struct sockaddr *) &adr, sizeof(adr)) != 0) {
        perror("Problem these bind");
        _exit(1);
    }
    if (listen(main_sock, size_of_queue) != 0) {
        perror("Problem these listen");
        _exit(1);
    }
    int flag = fcntl(main_sock, F_GETFL);
    flag = flag | FIOSETOWN;
    fcntl(main_sock, F_SETFL, flag);
    return main_sock;
}

Helper::Helper(int port) {
    char buffer[size_of_buffer];
    int signal_fd = get_sock_for_SIGTERM();
    int main_sock = get_main_sock(port);
    int fd = epoll_create1(0);
    struct epoll_event my_epoll;
    my_epoll.events = EPOLLIN;
    struct epoll_event array_this_events[size_of_array];
    my_epoll.data.fd = main_sock;
    epoll_ctl(fd, EPOLL_CTL_ADD, main_sock, &my_epoll);
    int sock_for_add;
    my_epoll.data.fd = signal_fd;
    epoll_ctl(fd, EPOLL_CTL_ADD, signal_fd, &my_epoll);
    this->fd = fd;
    this->main_sock = main_sock;
    this->signal_fd = signal_fd;
}

Helper::~Helper() {
    close(fd);
    close(main_sock);	
}

void Helper::add_client(int sock_for_add) {
    struct epoll_event my_epoll;
    my_epoll.events = EPOLLIN;
    my_epoll.data.fd = sock_for_add;
    int flag_for_fd = fcntl(sock_for_add, F_GETFL);
    flag_for_fd |= O_NONBLOCK;
    fcntl(sock_for_add, F_SETFL, flag_for_fd);
    epoll_ctl(fd, EPOLL_CTL_ADD, sock_for_add, &my_epoll);
}

void Helper::obr_socket(int socket) {
    int sock_for_add;
    if (socket == main_sock) {
        while (-1 != (sock_for_add = accept(main_sock, NULL, NULL))) {
        add_client(sock_for_add);
        Users_server.insert(sock_for_add, obr1.make_connection(sock_for_add));
    }
    } else if (socket == signal_fd) {
        flag_of_work = 0;
    } else {
        int result = obr2.obr_connector(socket);
        if (result == 1) {
            Users_server.erase(socket);
            close(socket);
        }
    }
}
