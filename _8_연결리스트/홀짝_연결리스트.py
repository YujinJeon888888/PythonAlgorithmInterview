

def oddEvenList(self,head: ListNode)->ListNode:
    #����ó��
    if head is None:
        return None

    odd=head
    even=head.next
    even_head=head.next


    #�ݺ��ϸ鼭 Ȧ¦ ��� ó��
    while even and even.next:
        odd.next,even.next: 
            odd.next,even.next=odd.next.next,even.next.next
            odd,even=odd.next,even.next
    #Ȧ�� ���� �������� ¦�� ���� ����
    odd.next=even_head
    return head