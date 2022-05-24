cmake_minimum_required(VERSION 3.16)

project(Project)

add_executable(ServerBinary server/main.cpp
        server/src/Connector.cpp
        server/src/map.cpp
        server/src/obr1.cpp
        server/src/Obr2.cpp
        server/src/Play.cpp
        server/src/Reader.cpp
        server/src/helper.cpp)
target_include_directories(ServerBinary PRIVATE server/include)

add_executable(ClientBinary client/main.cpp
        client/src/Beginner.cpp
        client/src/Client_obr.cpp
        client/src/Connector.cpp
        client/src/Init_connection.cpp
        client/src/Obr1.cpp
        client/src/Reader.cpp
        client/src/Server_obr.cpp
        client/src/wait.cpp)
target_include_directories(ClientBinary PRIVATE client/include)
