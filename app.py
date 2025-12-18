# app.py

import streamlit as st
from library import Book, Library

st.set_page_config(page_title="Digital Library", layout="centered")
st.title("📚 Digital Library Management System")

if "library" not in st.session_state:
    st.session_state.library = Library()

library = st.session_state.library

menu = st.sidebar.radio(
    "Select Option",
    [
        "Add Book",
        "Search by Title",
        "Search by Author",
        "Borrow Book",
        "Return Book",
        "View All Books",
        "Borrowed Records",
    ],
)

# ---------------- ADD BOOK ----------------
if menu == "Add Book":
    st.header("Add New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    book_id = st.text_input("Book ID")
    copies = st.number_input("Total Copies", min_value=1, step=1)

    if st.button("Add Book"):
        book = Book(title, author, book_id, copies)
        st.success(library.add_book(book))

# ---------------- SEARCH TITLE ----------------
elif menu == "Search by Title":
    st.header("Search by Title")
    title = st.text_input("Enter title")
    if st.button("Search"):
        results = library.search_by_title(title)
        if results:
            for b in results:
                st.write(f"{b.book_id} | {b.title} | {b.author} | {b.available_copies}/{b.total_copies}")
        else:
            st.warning("No book found")

# ---------------- SEARCH AUTHOR ----------------
elif menu == "Search by Author":
    st.header("Search by Author")
    author = st.text_input("Enter author")
    if st.button("Search"):
        results = library.search_by_author(author)
        if results:
            for b in results:
                st.write(f"{b.book_id} | {b.title} | {b.author} | {b.available_copies}/{b.total_copies}")
        else:
            st.warning("No book found")

# ---------------- BORROW ----------------
elif menu == "Borrow Book":
    st.header("Borrow Book")
    user = st.text_input("Your Name")
    book_id = st.text_input("Book ID")
    if st.button("Borrow"):
        st.success(library.borrow_book(book_id, user))

# ---------------- RETURN ----------------
elif menu == "Return Book":
    st.header("Return Book")
    user = st.text_input("Your Name")
    book_id = st.text_input("Book ID")
    if st.button("Return"):
        st.success(library.return_book(book_id, user))

# ---------------- VIEW ALL ----------------
elif menu == "View All Books":
    st.header("All Books")
    if library.books:
        for b in library.books.values():
            st.write(f"{b.book_id} | {b.title} | {b.author} | {b.available_copies}/{b.total_copies}")
    else:
        st.info("No books available")

# ---------------- RECORDS ----------------
elif menu == "Borrowed Records":
    st.header("Borrowed Records")
    if library.borrowed_records:
        for r in library.borrowed_records:
            st.write(f"User: {r[0]} | Book: {r[1]}")
    else:
        st.info("No records found")
