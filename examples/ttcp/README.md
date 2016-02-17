# TTCP

用来测试主机之间的吞吐量。

## 网络协议

一问一答。Client 每发送一段数据后，需要接收到 Server 返回的 ACK 后再接着发送。

## 测试结果

测试方法：

- Server: `python ttcp_blocking.py -r localhost -p 3333 -l {length} -n 100000`
- Client: `python ttcp_blocking.py -t localhost -p 3333 -l {length} -n 100000`

每次发送的数据包长度与吞吐量的关系：

| length | 吞吐量（MiB/s） |
| --- | --- |
| 1024 | 32.552 MiB/s |
| 2048 | 65.104 MiB/s |
| 20480 | 651.042 MiB/s |
| 40960 | 976.562 MiB/s |
| 81920 | 1302.083 MiB/s |

结论：

可以看到 length 在一定区间，吞吐量和数据包长度基本正比关系。这个测试反应，
TTCP 采用停等协议，当数据包越小时，传输延迟对吞吐量的影响就越大。

## Ref:

- [网络编程实践 - TTCP - 陈硕](http://boolan.com/course/4)
- [muduo ttcp example](https://github.com/chenshuo/muduo/tree/master/examples/ace/ttcp)
