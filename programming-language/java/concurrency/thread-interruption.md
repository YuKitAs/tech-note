# Thread Interruption

In Java, every thread has a Boolean property that represents its interrupted status. A thread cannot stop another thread, it can only request another thread to stop by calling `interrupt()`. If the interrupted thread is executing methods like `Thread.sleep()`, `Thread.join()` or `Object.wait()`, it would throw `InterruptedException`, which should be re-thrown or handled properly in `catch (InterruptedException e)`.

Reference: [Dealing with InterruptedException](https://www.ibm.com/developerworks/library/j-jtp05236/index.html), IBM.
