#!/usr/bin/env python3
"""Stack and queue from scratch."""
class Stack:
    def __init__(self):self.items=[]
    def push(self,v):self.items.append(v)
    def pop(self):return self.items.pop()
    def peek(self):return self.items[-1]
    def is_empty(self):return len(self.items)==0
class Queue:
    def __init__(self):self.items=[]
    def enqueue(self,v):self.items.append(v)
    def dequeue(self):return self.items.pop(0)
    def is_empty(self):return len(self.items)==0
