import collections
from gc import collect


def mostCommonWord(self,paragraph:str,banned:list[str])->str:
    words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]

    counts=collections.Counter(words)
    #���� ���ϰ� �����ϴ� �ܾ��� ù ��° �ε��� ����
    return counts.most_common(1)[0][0]

