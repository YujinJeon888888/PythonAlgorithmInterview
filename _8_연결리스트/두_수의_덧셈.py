from asyncio import ProactorEventLoop
from lib2to3.pytree import Node
from math import nextafter
from msilib import PID_REVNUMBER
from pickle import NONE
from types import NoneType


class Solution:
    #���Ḯ��Ʈ ������
    def reverseList(self,head: ListNode)->ListNode:
        node,prev=head,None

        while node:
            next, node.next=node.next,prev
            prev,node=node,next

        return prev

    #���� ����Ʈ�� ���̽� ����Ʈ�� ��ȯ
    def toList(self,node : ListNode) ->List:
        list:List=[]
        while node:
            list.append(node.val)
            node=node.next
        return list
    #���̽� ����Ʈ�� ���� ����Ʈ�� ��ȯ
    def toReversedLikedList(self,result:str)->ListNode:
        prev:ListNode = None
        for r in result:
            node=ListNode(r)
            node.next=prev
            prev=node

        return node

    #�� ���� ����Ʈ�� ����
    def addTwoNumbers(self,l1:ListNode,l2:ListNode)->ListNode:
        a=self.toList(self.reverseList(l1))
        b=self.toList(self,reverseList(l2))

        resultStr=int(''.join(str(e) for e in a))+\
                    int(''.join(str(e) for e in b)

        #��������� ���Ḯ��Ʈ�� ��ȯ
        return self.toReversedLinkedList(str(resultStr))