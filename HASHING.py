
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 2002, 'COLE')
insert(HashTable, 2005, 'STEPH')
insert(HashTable, 1998, 'BENJE')
insert(HashTable, 2002, 'IHANNA')
insert(HashTable, 2002, 'REM')
insert(HashTable, 2001, 'MITCH')

display_hash(HashTable)
