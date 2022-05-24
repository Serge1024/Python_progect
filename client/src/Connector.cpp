#include "Connector.hpp"
Connector::Connector(Reader my_reader, int socket) : my_reader(my_reader), socket(socket) {}
Connector::Connector(const Connector &my_connector) : my_reader(my_connector.my_reader), socket(my_connector.socket) {}
int Connector::read(char *buffer, int size_of_buffer) {
    return my_reader.read_inf(buffer, size_of_buffer);
}
void Connector::write(char *buffer, int size_of_buffer) {
    my_reader.write_inf(buffer, size_of_buffer);
}
void Connector::write(std::string message) {
    this->write(&message[0], message.size());
}
std::string Connector::read() {
    const int size_of_buffer = 4096;
    std::string ans;
    char buffer[size_of_buffer];
    int count_of_read_byte = 0;
    count_of_read_byte = this->read(buffer, size_of_buffer);
    ans += std::string(buffer, count_of_read_byte);
    return ans;
}
void Connector::write_message(std::string message) {
    int len = message.size();
    std::string packet;
    packet += char(2);
    packet += char(len);
    packet += message;
    this->write(packet);
}
void Connector::make_init(std::string name) {
    int len = name.size();
    std::string packet;
    packet += char(0);
    packet += char(len);
    packet += name;
    this->write(packet);
}
void Connector::break_connection() {
    std::string packet;
    packet += char(3);
    packet += char(0);
    this->write(packet);
}
