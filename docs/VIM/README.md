# VIM Resources

## Basic Usages

* **:help** - VIM help file

## Best Practices

* VIM 分屏
    - <http://coolshell.cn/articles/1679.html>
    - `:split` 水平分屏
    - `:vsplit` 垂直分屏
    - `Ctrl + W + h/l/k/j` 把光标移动到左屏/右屏/上屏/下屏
    - `Ctrl + W + =` 让所有屏幕一样大

* How to navigate multiple ctags matches in Vim?
    - <http://stackoverflow.com/questions/14465383/how-to-navigate-multiple-ctags-matches-in-vim>
    - `ctrl + ]`

* Replace Tab with Spaces in VIM
    - <http://stackoverflow.com/questions/426963/replace-tab-with-spaces-in-vim>
    - `:retab`

* VIM 直接跳转到系统函数（C 语言版）
    - <http://www.vim.org/scripts/script.php?script_id=1553>
    - `ctags -R -f ~/.vim/systags --c-kinds=+p /usr/include /usr/local/include`

* VIM 括号匹配
    - <http://blog.csdn.net/bigshady/article/details/6019963>
    - `%`

* 按键映射
    - <http://haoxiang.org/2011/09/vim-modes-and-mappin/>
    - `:map <C-a> a` 令 Ctrl + a 对应到 a

## References

* [Amir Salihefendic's vimrc](http://amix.dk/vim/vimrc.html)
* [The ultimate Vim configuration: vimrc](https://github.com/amix/vimrc)
* [My vimrc](https://github.com/omsobliga/profile/blob/master/.vimrc)
* [k-vim](https://github.com/wklken/k-vim)
