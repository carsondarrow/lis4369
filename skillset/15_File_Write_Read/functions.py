import os

def get_requirements():
    print("Program Requirements:")
    print("1. Create write_read_file subdirectory with two files: main.py and functions.py.")
    print("2. Use President Abraham Lincoln's Gettysburg Address: Full Text")
    print("3. Write address to file.")
    print("4. Read address from same file.")
    print("5. Create Python Docstrings for functions in functions.py file.")
    print("6. Display Python Docstrings for each function in functions.py file.")
    print("7. Display full file path.")
    print("8. Replicate display below.")

    print("\nHelp on function write_read_file in module functions: ")
    print("Write_read file()")
    print("\tUsage: Calls two functions:")
    print("\t 1. file write() # writes to file")
    print("\t 2. file read() # reads from file")
    print("\tParameters: none")
    print("\tReturns: none")
    print("\nHelp on function file write in module functions:")
    print("file write()")
    print("\tUsage: creates file, and writes contents of global variable to file")
    print("\tParameters: none")
    print("\tReturns: none")
    print("\nHelp on function file_read in module functions:")
    print("file_read()")
    print("\tUsage: reads contents of written file")
    print("\tParameters: none")
    print("\tReturns: none\n")

def file_write():

    f = open("tests.txt", "w")
    f.write("President Abraham Lincoln's Gettysburg Address: \nFourscore and seven years ago our fathers brought forth, on this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived, and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting-place for those who here gave their lives, that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we cannot dedicate, we cannot consecrate—we cannot hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they here gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth.")
    f.write("\n\nFull File Path: ")
    f.write(os.path.realpath(f.name))
    f.close()

def file_read():
    f = open("tests.txt", "r")
    print(f.read())

def write_read_file():
    file_write()
    file_read()
