# Greenlet Learning Note

## 1. 为解决什么问题？

处理并发问题，提供一种不同于多线程的思路。

网上看到一段讲「多线程弊端」的文章，觉得很好，直接贴过来了：

> 用多线程来实现异步最大的弊病，是它真的是并发的。采用线程实现的异步，即使不存在多核并行，线程执行的先后仍然是不可预知的。操作系统课程上我们也学到过，称之为不可再现性。究其原因，线程的调度毕竟是调度器来完成的，无论是系统级的调度还是用户级的调度，调度器都会因为 IO 操作、时间片用完等诸多的原因，而强制夺取某个线程的控制权。这种不可再现性给线程编程带来了极大的麻烦。如果是上段中的简单代码还没什么，若是情况更加复杂一些，在单独的线程中操作了某共享资源，那么这个共享资源就会成为危险的临界资源，一时疏忽忘记加锁就会带来数据不一致问题。而加锁本身是把对资源的并行访问串行化，所以锁往往又是拖慢系统效率的罪魁祸首，由此又发展出了多种复杂的锁机制。[4]

## 2. 提供了那些吸引人的特性？

greenlet 是更原始的没有复杂的系统调度的微线程，即协程（coroutines）。
这对用户可准确控制代码的运行是非常有用的。你可以在「父 greenlet」中对微线程（子 greenlet）进行调度。

> A “greenlet”, on the other hand, is a still more primitive notion of micro-thread with no implicit scheduling; coroutines, in other words. This is useful when you want to control exactly when your code runs. You can build custom scheduled micro-threads on top of greenlet; [2]

## 3. Demo

```
from greenlet import greenlet

def test1():
print 12
gr2.switch()
print 34

def test2():
print 56
gr1.switch()
print 78

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
```

依次打印：
```
12
56
34
```

打印完 34 后，test1 结束，gr1 死掉。执行回到最初的 gr1.switch()，需要注意的是 78 不会被打印。

## 4. 实现原理

### Parents:
让我们来看下 greenlet 死掉之后执行会回到那里。每一个 greenlet 都有一个「父 greenlet」。
「父 greenlet」是最初 greenlet 被创建所在的 greenlet。当一个 greenlet 死掉，执行会回到「父 greenlet」那里。
因此，greenlets 被组织成一棵树。顶层的代码并不再用户创建的 greenlet 中运行，
在一个被叫做「main greenlet」中运行（树的根节点）。[2]

在 Demo 的例子中，gr1 和 gr2 的「父 greenlet」都是 main greenlet，不管哪个死掉，
都会回到 main greenlet。（这就是为什么 78 不会再打印）

### 数据结构：

每一个 greenlet 其实就是一个函数，以及保存这个函数执行时的上下文。
TODO

## 5. Reference:

* [1][用 greenlet 协程处理异步事件](https://blog.tonyseek.com/post/event-manage-with-greenlet/)
* [2][greenlet: Lightweight concurrent programming](https://greenlet.readthedocs.org/en/latest/)
* [3][greenlet: 轻量级并发编程](http://gashero.yeax.com/?p=112)
* [4][python greenlet 背景介绍与实现机制](http://blog.jobbole.com/77240/)
