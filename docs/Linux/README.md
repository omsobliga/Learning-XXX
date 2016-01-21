# Linux Resources

## Tools

- **ag** - A code-searching tool similar to ack, but faster.
    - [Github](https://github.com/ggreer/the_silver_searcher)

- **cheat** - linux 命令小抄，比 help 和 man 命令更容易理解，通过实例告诉你怎么使用。
    - [Github](https://github.com/chrisallenlane/cheat)

- **cloc** - Count Lines of Code
    - [AlDanial/cloc](https://github.com/AlDanial/cloc)

- **curl**
    - [curl 网站开发指南](http://www.ruanyifeng.com/blog/2011/09/curl.html)

- **dmesg** - display the system message buffer
    - [The dmesg Command](http://www.linfo.org/dmesg.html)

- **grep**
    - [Grep a file, but show several surrounding lines?](http://stackoverflow.com/questions/9081/grep-a-file-but-show-several-surrounding-lines)

- **make**
    - [What does "./configure; make; make install" do?](http://askubuntu.com/questions/173088/what-does-configure-make-make-install-do)

- **stat** - display file or file system status
    - [stat(1) - Linux man page](http://linux.die.net/man/1/stat)

- **tcpdump** - dump traffic on a network
    - [A tcpdump Primer with Examples](https://danielmiessler.com/study/tcpdump/)
    - Usage: `tcpdump -i lo0 port 8000`, Listen 8000 port on the lo0 interface

## Best Practices

- **How to find the largest files in linux?**
    - <http://linuxlookup.com/howto/find_all_large_files_linux_system>
        - `find / -type f -size +20M -exec ls -lh {} \; 2> /dev/null | awk '{ print $NF ": " $5 }' | sort -nk 2,2`
    - <http://www.cyberciti.biz/faq/how-do-i-sort-du-h-output-by-size-under-linux/>
    - <http://www.cyberciti.biz/faq/how-do-i-find-the-largest-filesdirectories-on-a-linuxunixbsd-filesystem/>

- **file encoding**
    - **file** - determine file type
        - `file a.csv`
    - **iconv** - Convert encoding of given files from one encoding to another
        - `iconv -f UTF8 -t GB18030 a.csv > b.csv`

- **Linux 的性能诊断**
    - [Linux 性能分析的第一分钟](http://www.oschina.net/translate/linux-performance-analysis-in-60s)
    - [Linux Performance Analysis in 60,000 Milliseconds](http://techblog.netflix.com/2015/11/linux-performance-analysis-in-60s.html)

## References:

- [Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line)
- [Linux 工具快速教程](http://linuxtools-rst.readthedocs.org/zh_CN/latest/)
