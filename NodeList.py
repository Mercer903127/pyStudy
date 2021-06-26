#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(self, pHead):
    cur = None
    pre = pHead
    while pre:
        temp = pre.next
        pre.next = cur
        cur = pre
        pre = temp
    return cur