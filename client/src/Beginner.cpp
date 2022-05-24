#include <arpa/inet.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int beginner(char *argv[]) {
    char *IP = argv[1];
    int port = atoi(argv[2]);
    int soc = socket(AF_INET, SOCK_STREAM, 0);
    if (soc == -1) {
        perror("Can't create a socket");
        _exit(1);
    }
    struct sockaddr_in my_struct;
    my_struct.sin_family = AF_INET;
    my_struct.sin_port = htons((short) port);
    my_struct.sin_addr.s_addr = inet_addr(IP);
    int connect_result = connect(soc, (struct sockaddr *) &my_struct,
                                 sizeof(my_struct));
    if (connect_result == -1) {
        perror("Can't connect to the server");
        _exit(1);
    }
    //    char buffer[100];
    //    int flag_for_server = 2;
    //    int64_t count_of_byte = 1;
    //    buffer[0] = (char)(2);
    //    buffer[1] = (char)(3);
    //    buffer[2] = 'h';
    //    buffer[3] = 'e';
    //    buffer[4] = 'l';
    //    write(soc, buffer, 5);
    //    buffer[0] = char(3);
    //    buffer[1] = char(1);
    //    write(soc, buffer, 2);
    //    close(soc);
    return soc;
}
