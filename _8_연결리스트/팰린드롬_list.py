#연결리스트가 팰린드롬 구조인지 판별하라
#pop()함수에 인덱스를 지정해 원하는 위치를 자유롭게 추출가능

from tkinter.tix import ListNoteBook


def isPalindrome(self,head: ListNode) ->bool:
        q:list=[]

        if not head:
            return True

        node =head
        #리스트변환
        while node is not None:
            q.append(node.val)
            node=node.next

        #팰린드롬 판별
        while len(q)>1:
            if q.pop(0)!=q.pop():#q.pop(0) : 뒤 요소들이 한 칸씩 앞으로 땡겨지므로 O(n)발생
                return False
        return True
