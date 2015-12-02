#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#define PORT_NO 3033
#define BUFFER_SIZE 1024

int get_listenfd();


int main() {
    int i, n;
    struct sockaddr_in addr, client_addr;
    int conn_sock, sockfd;
    char buffer[BUFFER_SIZE] = "";
    ssize_t recv_msg;
    socklen_t addrlen = sizeof(addr);

    int listenfd = get_listenfd();
    // create listen socket failed
    if (listenfd < 0)
    {
        return -1;
    }

    while (1)
    {
        conn_sock = accept(listenfd, (struct sockaddr *)&client_addr, &addrlen);
        while (1)
        {
            sockfd = conn_sock;
            printf("sockfd = %d\n", sockfd);
            // Receive message from client socket
            recv_msg = recv(sockfd, buffer, BUFFER_SIZE, 0);

            if (recv_msg < 0)
                perror("recv_msg error");
            else if (recv_msg == 0) {
                close(sockfd);
                break;
            }
            else {
                printf("recv message: %s\n", buffer);
                send(sockfd, buffer, recv_msg, 0);
            }
        }
    }
    close(listenfd);
    return 0;
}


int get_listenfd()
{
    int listenfd;
    struct sockaddr_in addr;
    int addr_len = sizeof(addr);
    // Create server socket
    if( (listenfd = socket(PF_INET, SOCK_STREAM, 0)) < 0 )
    {
        perror("socket error");
        return -1;
    }

    bzero(&addr, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT_NO);
    addr.sin_addr.s_addr = INADDR_ANY;

    // Bind socket to address
    if (bind(listenfd, (struct sockaddr*) &addr, sizeof(addr)) != 0)
    {
        perror("bind error");
    }

    // Start listing on the socket
    if (listen(listenfd, 2) < 0)
    {
        perror("listen error");
        return -1;
    }
    return listenfd;
}
