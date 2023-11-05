from asyncio import ProactorEventLoop
from lib2to3.pytree import Node
from math import nextafter
from msilib import PID_REVNUMBER
from pickle import NONE
from types import NoneType


class Solution:
    #연결리스트 뒤집기
    def reverseList(self,head: ListNode)->ListNode:
        node,prev=head,None

        while node:
            next, node.next=node.next,prev
            prev,node=node,next

        return prev

    #연결 리스트를 파이썬 리스트로 변환
    def toList(self,node : ListNode) ->List:
        list:List=[]
        while node:
            list.append(node.val)
            node=node.next
        return list
    #파이썬 리스트를 연결 리스트로 변환
    def toReversedLikedList(self,result:str)->ListNode:
        prev:ListNode = None
        for r in result:
            node=ListNode(r)
            node.next=prev
            prev=node

        return node

    #두 연결 리스트의 덧셈
    def addTwoNumbers(self,l1:ListNode,l2:ListNode)->ListNode:
        a=self.toList(self.reverseList(l1))
        b=self.toList(self,reverseList(l2))

        resultStr=int(''.join(str(e) for e in a))+\
                    int(''.join(str(e) for e in b)

        #최종계산결과 연결리스트로 변환
        return self.toReversedLinkedList(str(resultStr))