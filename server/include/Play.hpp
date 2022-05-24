#ifndef ___PLAY___
#define ___PLAY___
#include <set>
#include <string>
class Play {
    public:
        void step(int socket, std::string message);
    private:
        std::set<int> users;
};
#endif
