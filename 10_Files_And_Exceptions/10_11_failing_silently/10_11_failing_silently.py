# In some cases we would like to catch the specific error but continue operations without any intervention or outputs.
# In these cases we use the "pass" statement in our except block. Everything else is same from the previous example.
def count_words(path):
    from pathlib import Path
    book = Path(f"{path}")
    try:
        contents = book.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        num_of_words = contents.split()
        print(len(num_of_words))

count_words("../../python_work/text_files/asd.txt") # File not found error is not raised, because we have used "pass" statement.
count_words("../../python_work/text_files/illiad.txt")
count_words("../../python_work/text_files/guest_book.txt")