# Linux Resources

## Tools

- **ag** - A code-searching tool similar to ack, but faster.
    - [ggreer/the_silver_searcher](https://github.com/ggreer/the_silver_searcher)

- **awk** - pattern scanning and processing language
    - Usage:
        * `awk -F "," '{print $2}' t.txt` 以逗号做分割从文件中提取数据
        * `awk '{sum += $2} END {print sum}' t.txt` 每行第二列数字之和
    - [AWK 简明教程 - 酷壳](http://coolshell.cn/articles/9070.html)

- **cheat** - linux 命令小抄，比 help 和 man 命令更容易理解，通过实例告诉你怎么使用。
    - [chrisallenlane/cheat](https://github.com/chrisallenlane/cheat)

- **cloc** - Count Lines of Code
    - [AlDanial/cloc](https://github.com/AlDanial/cloc)

- **curl** - transfer a URL
    - Usage:
        * `curl example.com`
        * `curl -A 'Baiduspider' example.com` 指定 User Agent
        * `curl -X POST --data "data=xxx" example.com` 使用 POST 方法
    - [curl 网站开发指南](http://www.ruanyifeng.com/blog/2011/09/curl.html)

- **dmesg** - display the system message buffer
    - [The dmesg Command](http://www.linfo.org/dmesg.html)

- **free** - Display amount of free and used memory in the system
    - Usage: `free -h` or `free -m` 查看内存使用情况
    - [Linux 的 free 命令详解](http://www.php-oa.com/2008/04/04/linux-free.html)

- **grep** - print lines matching a pattern
    - Usage:
        - `grep -B 3 -A 2 foo README.txt`
        - `grep -C 3 foo README.txt`, grep a file, but show several surrounding lines
        - `tail -f web.log | grep -E "\" 50[0-9] "`, grep 5xx from the tail of file
        - `tac web.log | grep -E "\" 50[0-9]"`, grep from file in reverse
    - [What's the difference between “grep -e” and “grep -E”](http://stackoverflow.com/a/17130337/3175815)
    - [‘grep’ regular expression syntax](https://www.gnu.org/software/findutils/manual/html_node/find_html/grep-regular-expression-syntax.html)

- **iostat** - input/output statistics
    - Usage: `iostat -k 1`
    - [Linux iostat 监测 IO 状态](http://www.orczhou.com/index.php/2010/03/iostat-detail/)
    - [实例讲解 iostat](http://www.php-oa.com/2009/02/03/iostat.html)

- **lsof** - list open files
    - Usage: `lsof -i TCP:80`, to find which program is using the port 80.

- **make** - GNU make utility to maintain groups of programs
    - [What does "./configure; make; make install" do?](http://askubuntu.com/questions/173088/what-does-configure-make-make-install-do)

- **netcat** - TCP/IP swiss army knife
    - Usage: Echo Server: `nc -l 1567`, Client: `nc localhost 1567`
    - [Linux Netcat 命令——网络工具中的瑞士军刀](http://www.oschina.net/translate/linux-netcat-command)

- **netstat** - prints information about the Linux networking subsystem
    - Usage:
        * `netstat -a | grep 2901` 查看某端口的网络连接情况
        * `netstat -a | grep TIME_WAIT | wc -l` 计算处于 TIME_WAIT 状态的连接数
    - [Linux netstat 命令详解](http://www.cnblogs.com/ggjucheng/archive/2012/01/08/2316661.html)

- **ps** - process status
    - `ps -ef`: UID PID PPID C STIME TTY TIME CMD

- **sar** - system activity information.（最全面的系统分析工具）
    - Usage: `sar -n DEV 1 2`, `sar -n TCP,ETCP 1 2` 检查网络接口的吞吐量
    - [Useful Sar (Sysstat) Examples for UNIX / Linux Performance Monitoring](http://www.thegeekstuff.com/2011/03/sar-examples/)

- **stat** - display file or file system status
    - [stat(1) - Linux man page](http://linux.die.net/man/1/stat)

- **tcpdump** - dump traffic on a network
    - Usage:
        * `tcpdump -i lo0 port 8000`, listen 8000 port on the lo0 interface.
        * `sudo tcpdump -A src port 8080`, print each pocket on 8080 port from src.
        * `sudo tcpdump -A dst port 8080`, print each pocket on 8080 port to dst.
    - [A tcpdump Primer with Examples](https://danielmiessler.com/study/tcpdump/)
    - [Linux tcpdump 命令详解](http://www.cnblogs.com/ggjucheng/archive/2012/01/14/2322659.html)

- **tmux** - terminal multiplexer
    - [Tmux：Linux 从业者必备利器](http://blog.jobbole.com/87562/)

- **vmstat** - Report virtual memory statistics
    - Usage: `vmstat 1`
    - [Linux 监控工具 vmstat 命令详解](http://www.ha97.com/4512.html)
    - [Linux 内存 buffer 和 cache 的区别](http://blog.csdn.net/tianlesoftware/article/details/6459044)


## Best Practices

- **How to find the largest files in linux?**
    - [Find All Large Files On A Linux System](http://linuxlookup.com/howto/find_all_large_files_linux_system)
        - Usage: `find / -type f -size +20M -exec ls -lh {} \; 2> /dev/null | awk '{ print $NF ": " $5 }' | sort -nk 2,2`
    - [http://www.cyberciti.biz/faq/how-do-i-sort-du-h-output-by-size-under-linux/](http://www.cyberciti.biz/faq/how-do-i-sort-du-h-output-by-size-under-linux/)

- **file encoding**
    - **file** - determine file type
        - Usage: `file a.csv`
    - **iconv** - Convert encoding of given files from one encoding to another
        - Usage: `iconv -f UTF8 -t GB18030 a.csv > b.csv`

- **listen host and port**
    - `lsof -i TCP:80`, to find which program is using the port 80.
    - `tcpdump -i lo0 port 8000`, listen 8000 port on the lo0 interface.

- **Linux 的性能诊断**
    - [Linux 性能分析的第一分钟](http://www.oschina.net/translate/linux-performance-analysis-in-60s)
    - [Linux Performance Analysis in 60,000 Milliseconds](http://techblog.netflix.com/2015/11/linux-performance-analysis-in-60s.html)

## References:

- [Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line)
- [Linux 工具快速教程](http://linuxtools-rst.readthedocs.org/zh_CN/latest/)
