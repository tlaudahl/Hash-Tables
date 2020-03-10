import random

def collisions(buckets, loops=1):
    """
    Roll random hashes indexes into buckets and prints
    how many rolls before a collision

    Run loops times
    """
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                # We found a collision
                break

        print(f"{buckets} buckets, {tries} hashes before collision. ({tries/buckets * 100:.1f}%)")



collisions(100, 10)