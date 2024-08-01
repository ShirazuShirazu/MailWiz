import argparse
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def getSession():
    Base = declarative_base()
    user = 'root'
    password = ''
    host = '127.0.0.1'
    port = 3306
    database = 'mailwiz'
    engine = create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def send_email(recipient):
    print(f"Sending email to {recipient}")

def create_email_folder(folder_name):
    if not folder_name:
        print("Error: Folder name is required")
        return
    print(f"Creating email folder named {folder_name}")

def main():
    parser = argparse.ArgumentParser(description="Mailwiz Command Line Interface")
    subparsers = parser.add_subparsers(dest="command")

    # Command: send_email
    send_email_parser = subparsers.add_parser("send_email", help="Send an email")
    send_email_parser.add_argument("recipient", type=str, help="Email address to send to")

    # Command: create_email_folder
    create_email_folder_parser = subparsers.add_parser("create_email_folder", help="Create a new email folder")
    create_email_folder_parser.add_argument("folder_name", type=str, help="Name of the new email folder")

    args = parser.parse_args()

    if args.command == "send_email":
        send_email(args.recipient)
    elif args.command == "create_email_folder":
        create_email_folder(args.folder_name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
