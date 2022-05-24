#include <sys/epoll.h>
#include <sys/wait.h>
#include "helper.hpp"
#include <stdio.h>


int size_of_arr = 4096;

int main(int argc, char* argv[]) {
    
    printf("Server is working");
    fflush(stdout);

    Helper my_helper = Helper(atoi(argv[1]));
    int fd = my_helper.fd;
    struct epoll_event array_this_events[size_of_arr];

    while (my_helper.flag_of_work) {
        int count_of_event_now =
                epoll_wait(fd, array_this_events, size_of_arr, -1);
        for (int i = 0; i < count_of_event_now; i++) {
            my_helper.obr_socket(array_this_events[i].data.fd);
        }
    }

    return 0;

}
