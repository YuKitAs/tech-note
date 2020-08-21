# Starvation and Livelock

Starvation is a situation when shared resources are occupied by "greedy" threads for a long period, e.g. when a synchronized method takes a long time to return and other threads that need to frequently access the same object will often be blocked.

Livelock happens when threads are busy responding each other to resume work. The difference between livelock and deadlock is that the threads are not blocked, their states are constantly changing with regard to each other.
