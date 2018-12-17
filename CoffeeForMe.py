from User import User as User
from utils import init_db, drop_db, fill_database


def main():
    drop_db()
    init_db()
    fill_database()
    user = User()
    user.user_action()


if __name__ == "__main__":
    main()
