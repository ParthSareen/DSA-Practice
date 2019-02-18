"""
constant time lookups
always optimize things with this
value -> hash function -> hash value(index)
common -> take last few numbers of big value, take the remainder
(56/10 = 5) rem = 6
last few digits are the most random
---
collisions:
when we get the same hash value for two inputs
first: change value or hash function
second: change strucutre of array: create a bucket(collection)
instead
bucket system: might be O(n) n-> size list
load factor: how full a hash table is
Load Factor = Number of Entries / Number of Buckets
rehash when Load Factor --> 0
if Load Factor > 1 == collision gaurantee
---
Hash Maps
maps have keys and values, --> hash, give bucket
algos: Hash maps

string keys converted to ascii
<30 words
s[0]*31^(n-1) + s[1] *31^(n-2)+...+s[n-1]
31 is great for hashing -> convention

Hash Val = (ASCII val of First lett *100) + ASCII val of second letter
ord() -> ascii val of letter
chr() -> letter with ascii val
"""
word = "hello"
for i in word:
    print(i)
w2 = "UDACITY"
print(ord(w2[8]))
"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hashVal = self.calculate_hash_value(string)
        if hashVal != -1:
            if self.table[hashVal] != None:
                self.table[hashVal].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hashVal = self.calculate_hash_value(string)
        if hashVal != -1:
            if self.table[hashVal] != None:
                if string in self.table[hashVal]:
                    return hashVal
        return -1

    def calculate_hash_value(self, string):
        total = 0
        total = ord(string[0]) * 100 + ord(string[1])
        return total

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
