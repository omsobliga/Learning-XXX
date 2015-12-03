# Linux Resources

## Basic Syntax

- **dmesg** - display the system message buffer
    - [The dmesg Command](http://www.linfo.org/dmesg.html)

- **grep**
    - [Grep a file, but show several surrounding lines?](http://stackoverflow.com/questions/9081/grep-a-file-but-show-several-surrounding-lines)



- **make**
    - [What does "./configure; make; make install" do?](http://askubuntu.com/questions/173088/what-does-configure-make-make-install-do)

- **stat** - display file or file system status
    - [stat(1) - Linux man page](http://linux.die.net/man/1/stat)

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

## References:

- [Master the command line, in one page](https://github.com/jlevy/the-art-of-command-line)
- [Linux 工具快速教程](http://linuxtools-rst.readthedocs.org/zh_CN/latest/)
