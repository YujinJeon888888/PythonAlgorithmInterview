#���Ḯ��Ʈ�� �Ӹ���� �������� �Ǻ��϶�
#pop()�Լ��� �ε����� ������ ���ϴ� ��ġ�� �����Ӱ� ���Ⱑ��

from tkinter.tix import ListNoteBook


def isPalindrome(self,head: ListNode) ->bool:
        q:list=[]

        if not head:
            return True

        node =head
        #����Ʈ��ȯ
        while node is not None:
            q.append(node.val)
            node=node.next

        #�Ӹ���� �Ǻ�
        while len(q)>1:
            if q.pop(0)!=q.pop():#q.pop(0) : �� ��ҵ��� �� ĭ�� ������ �������Ƿ� O(n)�߻�
                return False
        return True
