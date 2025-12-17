# define class, initialize with three variables: name, number of songs, artist
class Album:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        # this makes output readable
        output = "\n"
        for row in self.data:
            output += " " + str(row) + "\n"
        return output


# add five albums to class
albums1 = [["Dirt", "Alice in Chains", 13],
           ["Toxicity", "System of a Down", 15],
           ["Pretty Hate Machine", "Nine Inch Nails", 10],
           ["Sehnsucht", "Rammstein", 12],
           ["Kid A", "Radiohead", 11]]
albums_collection = Album(albums1)
print(f"Collection 1: \n{albums_collection}")

print()
albums1.sort(key=lambda sublist: sublist[2])
print(f"Sorted by number of songs: \n{Album(albums1)}")
print()
# swap positions of index 0 and index 1
albums1[0], albums1[1] = albums1[1], albums1[0]
print(f"Swapped: \n{Album(albums1)}")
print()

# create new list of albums
albums2 = [["In Utero", "Nirvana", 12],
           ["Mer De Noms", "A Perfect Circle", 12],
           ["Siamese Dream", "The Smashing Pumpkins", 13],
           ["Around the Fur", "Deftones", 10],
           ["Absolution", "Muse", 15]]
albums_collection_2 = Album(albums2)
print(f"Collection 2: \n{albums_collection_2}")
print()

# combine albums 1 and 2
albums2 = albums1 + albums2
print(f"Combined collection: \n{Album(albums2)}")
print()

# create variables for new songs, and add them to the collection
song1 = ["Dark Side of the Moon", "Pink Floyd", 9]
song2 = ["Oops!... I Did if Again", "Britney Spears", 16]

albums2.append(song1)
albums2.append(song2)

print(f"Complete Collection: \n{Album(albums2)}")
print()

# sort complete collection by album name (alphabetically)
albums2.sort(key=lambda sublist: sublist[0])
print(f"Sorted by Album name: \n{Album(albums2)}")
print()


# conduct binary search to find index of Dark Side of the Moon
def binary_search(target, items):
    low, high = 0, len(items) - 1
    while high >= low:
        mid = (low + high)//2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


target_item = ["Dark Side of the Moon", "Pink Floyd", 9]
search = binary_search(target_item, albums2)
print(f"Dark Side of the Moon is found at index: {search}")
