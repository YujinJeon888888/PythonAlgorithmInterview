import collections


def groupAnagrams(self,strs:list[str])->list[list[str]]:
    anagrams=collections.defaultdict(list)

    for word in strs:
        #�����Ͽ� ��ųʸ��� �߰�
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.value())