# Users Table
users_db = {
    "81b075b3-f571-45de-aff0-3e667e8f6af4": {
        "username": "Alee",
        "full_name": "Alee Ta",
        "email": "ta@ta.com",
        "is_active": True,
    },
    "dab19b42-565d-49e2-a43f-8a948360f52b": {
        "username": "Desayo",
        "full_name": "Desayo lol",
        "email": "desayo@gmail.com",
        "is_active": True,
    },
    "f0722861-4ba5-49a7-b16a-ff7b71373df5": {
        "username": "Chidi",
        "full_name": "Chidi tofu",
        "email": "chidi@gmail.com",
        "is_active": False,
    },
    "c21d40af-117a-4373-88b3-b9ec63bc3d20": {
        "username": "Daniel",
        "full_name": "Daniel tolong",
        "email": "de@ta.com",
        "is_active": False,
    },
    "e8b0c7b3-2fbf-4a96-8f27-fd8e9e4c7d33": {
        "username": "Mattew",
        "full_name": "Mattew tolu",
        "email": "mattew@gmail.com",
        "is_active": True,
    },
    "fbad3e4b-df28-4f63-82d9-5d7b1d8f8d71": {
        "username": "Aminah",
        "full_name": "Aminah Ogala",
        "email": "aminah@gmail.com",
        "is_active": False,
    },
    "53f5c25c-8616-4a59-b2a4-0f4196733e71": {
        "username": "Alex",
        "full_name": "Alex udoh",
        "email": "alex@gmail.com",
        "is_active": True,
    },
}

# Books Table
books = {
    "7e8b4dfc-9a5a-4c2b-87bb-873cf9c6b2f3": {
        "title": "Heart stopper",
        "author": "Alice Oseman",
        "is_available": True,
    },
    "e5b6d127-8f90-4326-9358-f9d3b2ef3c5d": {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "is_available": True,
    },
    "3a1e92d1-86ed-4e37-bf36-f2a2b6b5d5b0": {
        "title": "The subtle art of not giving a f*ck",
        "author": "Mark Manson",
        "is_available": True,
    },
    "b0b0d128-9f31-4cfb-87af-ffbc1c1e5a9b": {
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "is_available": False,
    },
    "9a9e17e9-0d64-41e5-9fc3-7c2e3b2c7b98": {
        "title": "Everything is F*cked",
        "author": "Mark Manson",
        "is_available": False,
    },
    "fbad3e4b-df28-4f63-82d9-5d7b1d8f8d71": {
        "title": "Vampires Dires",
        "author": "L.J. Smith",
        "is_available": True,
    },
    "4c1c7a21-5c9e-4bde-91f6-b0a8d0f6e8f1": {
        "title": "Diary of a Wimpy Kid",
        "author": "Jeff Kinney",
        "is_available": True,
    },
    "a4569799-0121-4f23-a01f-802edc88332d": {
        "title": "Arcane",
        "author": "Riot Games",
        "is_available": True,
    },
    "860d7a5b-70e2-449a-a012-06df989659e7": {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "is_available": True,
    },
}

# Borrow Records Table
borrow_records_db = {
    "77998029-0050-47d4-9e7e-150ad428d7f0": {
        "user_id": "e8b0c7b3-2fbf-4a96-8f27-fd8e9e4c7d33",
        "book_id": "7e8b4dfc-9a5a-4c2b-87bb-873cf9c6b2f3",
        "borrow_date": "2024-10-01",
        "return_date": "2024-12-10",
    },
    "d44f1d8c-905b-4ff6-8469-29acf1041897": {
        "user_id": "dab19b42-565d-49e2-a43f-8a948360f52b",
        "book_id": "e5b6d127-8f90-4326-9358-f9d3b2ef3c5d",
        "borrow_date": "2024-10-01",
        "return_date": "2024-12-10",
    },
    "32ccf7de-af5e-4ea7-8fa8-9520ddae477e": {
        "user_id": "f0722861-4ba5-49a7-b16a-ff7b71373df5",
        "book_id": "9a9e17e9-0d64-41e5-9fc3-7c2e3b2c7b98",
        "borrow_date": "2025-06-08",
        "return_date": "2025-08-10",
    },
    "54a76bf2-438a-4673-8268-53be107fe67d": {
        "user_id": "c21d40af-117a-4373-88b3-b9ec63bc3d20",
        "book_id": "4c1c7a21-5c9e-4bde-91f6-b0a8d0f6e8f1",
        "borrow_date": "2024-11-01",
        "return_date": "2024-12-10",
    },
    "f83ff015-d298-40c2-b3b6-cfd16a20eb3c": {
        "user_id": "81b075b3-f571-45de-aff0-3e667e8f6af4",
        "book_id": "fbad3e4b-df28-4f63-82d9-5d7b1d8f8d71",
        "borrow_date": "2024-10-01",
        "return_date": "2024-12-10",
    },
    "652d7bf4-8432-4211-90c2-86f857c37db1": {
        "user_id": "f0722861-4ba5-49a7-b16a-ff7b71373df5",
        "book_id": "fbad3e4b-df28-4f63-82d9-5d7b1d8f8d71",
        "borrow_date": "2025-06-12",
        "return_date": "2025-08-10",
    },
}
