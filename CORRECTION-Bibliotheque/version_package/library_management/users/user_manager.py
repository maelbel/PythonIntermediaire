# Liste globale des utilisateurs en mémoire
users = []

def add_user(name):
    user = {"name": name, "borrowed_books": []}
    users.append(user)
    print(f"Utilisateur ajouté : {name}")

def find_user(name):
    return next((user for user in users if user["name"] == name), None)

def list_user_loans(user_name):
    user = find_user(user_name)
    
    if user:
        borrowed_books = user["borrowed_books"]
        
        if borrowed_books:
            print(f"Livres empruntés par {user_name} :")
            for book in borrowed_books:
                print(f"- {book['title']} par {book['author']}")
        else:
            print(f"{user_name} n'a emprunté aucun livre.")
    else:
        print("Utilisateur introuvable.")
