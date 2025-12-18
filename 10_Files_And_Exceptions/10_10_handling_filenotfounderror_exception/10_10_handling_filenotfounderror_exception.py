# We can create pre handled excetions for file not found errors similar below.
# count_words() function takes the path of a book we define, and it checks if there is a book in the path first.
def count_words(path):
    from pathlib import Path
    book = Path(f"{path}")
    try:
        contents = book.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("file not found!")
    else:
        num_of_words = contents.split()
        print(len(num_of_words))

count_words("../../python_work/text_files/asd.txt") # File not found error raised
count_words("../../python_work/text_files/illiad.txt")
count_words("../../python_work/text_files/guest_book.txt")