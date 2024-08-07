from collections import Counter
def groupAnagrams(strs):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Solution 1:
        # from collections import defaultdict
        # def_dict = defaultdict(list)
        # for x in strs:
        #     a = [0] * 26
        #     for c in x:
        #         a[ord(c) - ord('a')] += 1
        #     print(a)
        #     def_dict[tuple(a)].append(x)
        # return def_dict.values()

        # Solution 2(best):
        wordmap={}
        for s in strs:
            sorted_word = ''.join(sorted(s))
            if sorted_word in wordmap:
                wordmap[sorted_word].append(s)
            else:
                wordmap[sorted_word]=[s]
        return list(wordmap.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))