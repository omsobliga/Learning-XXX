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


int main()
{
    int i;
    int listenfd, connfd, sockfd, maxfd;
    struct sockaddr_in addr;
    char buffer[BUFFER_SIZE] = "";
    fd_set rfds, allfds;
    struct timeval tv;
    int maxi, clients[FD_SETSIZE];
    int nready;
    ssize_t read;

    listenfd = get_listenfd();
    // create listen socket failed
    if (listenfd < 0)
    {
        return -1;
    }

    /* Watch sock addr to see when it has been read. */
    FD_ZERO(&allfds);
    FD_SET(listenfd, &allfds);

    /* Wait up to five seconds. */
    tv.tv_sec = 5;
    tv.tv_usec = 0;

    for (i = 0; i < FD_SETSIZE; i++)
        clients[i] = -1;

    maxfd = listenfd;  /* initialize */
    maxi = -1;  /* index into clients[] array */

    for(;;)
    {
        rfds = allfds;
        nready = select(maxfd + 1, &rfds, NULL, NULL, &tv);
        /* Don't rely on the value of tv now! */

        if (FD_ISSET(listenfd, &rfds))  /* new client connection */
        {
            struct sockaddr_in client_addr;
            socklen_t clilen = sizeof(client_addr);
            connfd = accept(listenfd, (struct sockaddr *)&client_addr, &clilen);

            for (i = 0; i < FD_SETSIZE; i++)
            {
                if (clients[i] < 0)
                {
                    clients[i] = connfd;
                    break;
                }
            }

            if (i == FD_SETSIZE)
            {
                perror("too many clients");
                return -1;
            }

            FD_SET(connfd, &allfds);

            if (connfd > maxfd)
                maxfd = connfd;  /* for select maxfd */

            if (i > maxi)
                maxi = i;  /* max index in clients[] arrar */

            if (--nready < 0)
                continue;  /* no more readable descriptors */

        }

        for (i = 0; i <= maxi; i++)
        {
            if ( (sockfd = clients[i]) < 0)
                continue;

            if (FD_ISSET(sockfd, &rfds))
            {
                printf("sockfd = %d\n", sockfd);
                // Receive message from client socket
                read = recv(sockfd, buffer, BUFFER_SIZE, 0);

                if (read < 0)
                {
                    perror("read error");
                } else if (read == 0)
                {
                    close(sockfd);
                    FD_CLR(sockfd, &allfds);
                    clients[i] = -1;
                } else
                {
                    printf("recv message: %s", buffer);
                    send(sockfd, buffer, read, 0);
                }
            }
            if (--nready < 0)
                break;  /* no more readable descriptors */
        }
    }
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

/* 参考：man select 和《UNIX 网络编程》 */
