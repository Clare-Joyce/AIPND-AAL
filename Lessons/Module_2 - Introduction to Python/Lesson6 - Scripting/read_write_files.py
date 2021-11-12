f = open("file.txt", 'r')
content = f.read()
f.close()

# use the with keyword which auto-closes the file
with open("file.txt", 'r') as f:
    content = f.read()

# no need to close the file
# f is only accessible within the with block
# content is accessible in and outside the block


# Calling read() with an integer

with open("camelot.txt", 'r') as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())