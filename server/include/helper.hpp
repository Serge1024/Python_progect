#include "Obr2.hpp"
#include "obr1.hpp"
#include "map.hpp"
#ifndef ___HELPER___
#define ___HELPER___

class Helper{
    public:
        Helper(int port);
        void add_client(int socket);
	~Helper();
	void obr_socket(int socket);
//    private:
	int get_sock_for_SIGTERM();
	int get_main_sock(int port);
	int main_sock;
	int fd;
	int signal_fd;
        Obr1 obr1;
        Obr2 obr2;
        map Users_server;
	int flag_of_work = 1;

};
#endif
