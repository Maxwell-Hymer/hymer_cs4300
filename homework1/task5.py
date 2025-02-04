def favorite_books_demo():
    # DISCLAIMER: I don't want these books to be of any worry/issue if so please reach out to me (Max Hymer) and I can
    #             further elaborate as to why these are some of my favorite books

    favorite_books = [
        {"title": "ATTACHMENT THEORY A Guide to Strengthening the Relationships in Your Life", "author": "Thais Gibson"},
        {"title": "THE BODY KEEPS THE SCORE", "author": "Bessel Van Der Kolk, M.D."},
        {"title": "The Freedom Model", "author": "Michelle Dunbar, Mark Scheeren, Steven Slate"}
    ]
    # Gets books via slicing
    first_three_books = favorite_books[:3]
    return first_three_books

def student_database_demo():
    student_database = {
        "student1" : {"name": "Max", "student_id": "00001"},
        "student2" : {"name": "Jim", "student_id": "00002"},
        "student3" : {"name": "Steve", "student_id": "00003"}
    }
    return student_database