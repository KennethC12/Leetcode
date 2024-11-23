class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # So the output is going to be a group of the anagrams, So we can create a hashmap that contains all of the words, so we compare the lengths of the words together, if they all have the same length, then you now compare the letters and the after comparting group them by the least anagrams to the most from left to right.
        # Fist we initialize the hashmap 
        anagram_map = {}

        for words in strs:
            sorted_words = tuple(sorted(words)) #Tuple seperates the word in to letters         
            #If sorted words are in the map append it
            if sorted_words in anagram_map:
                anagram_map[sorted_words].append(words)
            else:
                # If the key is not present, create a new list with the current word
                anagram_map[sorted_words] = [words]

        # Return all the groups of anagrams as a list of lists
        return list(anagram_map.values())