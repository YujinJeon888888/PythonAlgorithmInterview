from curses.ascii import isdigit

def reorderLogFiles(self,logs:list[str])->list[str]:
    letters,digits=[],[]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    #2���� Ű�� ���� ǥ�������� ����
    letters.sort(key=lambda x:(x.split()[1:],x.split()[0]))
    return letters+digits

#���� ǥ����: �ĺ��� ���� ���� ������ �Լ�. �Լ� ���� ���̵� �ϳ��� ������ �Լ��� �ܼ��ϰ� ǥ���� �� �ִ�.
#���� ǥ������ �ڵ尡 ������� map�̳� filter�� �Բ� ��� ����ϱ� �����ϸ� �������� �ſ� ������ �� �����Ƿ� ���ǰ� �ʿ��ϴ�.
