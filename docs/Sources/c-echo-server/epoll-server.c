#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/epoll.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#define PORT_NO 3033
#define BUFFER_SIZE 1024
#define MAX_EVENTS 10

int get_listenfd();


int main() {
    int i, n;
    struct sockaddr_in addr, client_addr;
    struct epoll_event ev, events[MAX_EVENTS];
    int conn_sock, nfds, epollfd, sockfd;
    char buffer[BUFFER_SIZE] = "";
    ssize_t recv_msg;
    socklen_t addrlen = sizeof(addr);

    int listenfd = get_listenfd();
    // create listen socket failed
    if (listenfd < 0)
    {
        return -1;
    }

    epollfd = epoll_create(10);
    if (epollfd == -1) {
        perror("epoll_create");
        exit(EXIT_FAILURE);
    }

    ev.events = EPOLLIN;
    ev.data.fd = listenfd;
    if (epoll_ctl(epollfd, EPOLL_CTL_ADD, listenfd, &ev) == -1) {
        perror("epoll_ctl: listenfd");
        exit(EXIT_FAILURE);
    }

    for (;;) {
        nfds = epoll_wait(epollfd, events, MAX_EVENTS, -1);
        if (nfds == -1) {
            perror("epoll_pwait");
            exit(EXIT_FAILURE);
        }

        for (n = 0; n < nfds; ++n) {
            if (events[n].data.fd == listenfd) {
                conn_sock = accept(listenfd, (struct sockaddr *)&client_addr,
                                   &addrlen);
                if (conn_sock == -1) {
                    perror("accept");
                    exit(EXIT_FAILURE);
                }
                // TODO: setnonblocking(conn_sock);
                ev.events = EPOLLIN | EPOLLET;
                ev.data.fd = conn_sock;
                if (epoll_ctl(epollfd, EPOLL_CTL_ADD, conn_sock,
                              &ev) == -1) {
                    perror("epoll_ctl: conn_sock");
                    exit(EXIT_FAILURE);
                }
            } else {
                sockfd = events[n].data.fd;

                printf("sockfd = %d\n", sockfd);
                // Receive message from client socket
                recv_msg = recv(sockfd, buffer, BUFFER_SIZE, 0);

                if (recv_msg < 0)
                    perror("recv_msg error");
                else if (recv_msg == 0)
                    close(sockfd);
                else {
                    printf("recv message: %s\n", buffer);
                    send(sockfd, buffer, recv_msg, 0);
                }
            }
        }
    }
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

/* man epoll */
