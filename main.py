import argparse
from service import get_posts
from database import create_table, insert_post, list_posts, clear_posts

def collect():
    print("Coletando dados...")
    create_table()

    posts = get_posts()

    for post in posts:
        insert_post(post)
    
    print("Dados salvos com sucesso!")

def list_data():
    posts = get_posts()

    if not posts:
        print("Nenhum dado encontrado.")
        return
    
    for post in posts:
        print(f"{post['id']} | {post['title']}")

def clear():
    clear_posts()
    print("Dados apagados!")

def main():
    parser = argparse.ArgumentParser(description="Data Collector CLI")

    parser.add_argument(
        "command",
        choices=["collect", "list", "clear"],
        help="Comando a ser executado"
    )

    args = parser.parse_args()

    if args.command == "collect":
        collect()
    elif args.command == "list":
        list_data()
    elif args.command == "clear":
        clear()

  
if __name__ == "__main__":
    main()
