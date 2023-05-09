import psycopg2
from config import host, user, password,db_name

list_files_csv = ["links", "movies", "ratings", "tags"]

def open_csv(file_csv):
    with open("DataSet/" + file_csv + ".csv") as file:
        return file.readlines()

def write_table(list_files_csv, cursor):
    for file_csv in list_files_csv:
        for list in globals()[file_csv]:
            for number in range(len(list)):
                if list[number].isdigit():
                    list[number] = int(list[number])
    for file_csv in list_files_csv:
        convert = tuple(globals()[file_csv])
        for list in convert:
            cursor.execute(
                f"INSERT INTO {file_csv} {tuple(list)};"
            )

for file_csv in list_files_csv:
    locals()[file_csv] = []
    for value in open_csv(file_csv):
        globals()[file_csv].append(value[:-2].split(','))

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    with connection.cursor() as cursor:
        write_table(list_files_csv, cursor)
        print("SELECT +")
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")