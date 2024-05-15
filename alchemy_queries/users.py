# from alchemy_queries.connector import DBConnector
# from alchemy_queries import engine
from alchemy_queries.models import User

# users = [
#     {'id': 1, 'name': 'Margaret', 'age': 32}, {'id': 2, 'name': 'Ricky', 'age': 79},
#     {'id': 3, 'name': 'Lauren', 'age': 61}, {'id': 4, 'name': 'Jennifer', 'age': 59},
#     {'id': 5, 'name': 'Scott', 'age': 72}, {'id': 6, 'name': 'Sara', 'age': 76},
#     {'id': 7, 'name': 'Evelyn', 'age': 51}, {'id': 8, 'name': 'Malik', 'age': 58},
#     {'id': 9, 'name': 'Deborah DDS', 'age': 21}, {'id': 10, 'name': 'John', 'age': 49},
#     {'id': 11, 'name': 'Patrick', 'age': 52}, {'id': 12, 'name': 'Kelly', 'age': 42},
#     {'id': 13, 'name': 'Elizabeth', 'age': 56}, {'id': 14, 'name': 'William', 'age': 53},
#     {'id': 15, 'name': 'Douglas', 'age': 53}, {'id': 16, 'name': 'Joanna', 'age': 54},
#     {'id': 17, 'name': 'Michael', 'age': 57}, {'id': 18, 'name': 'Allison', 'age': 27},
#     {'id': 19, 'name': 'Theresa', 'age': 58}, {'id': 20, 'name': 'Thomas', 'age': 74},
#     {'id': 21, 'name': 'Sara', 'age': 67}, {'id': 22, 'name': 'Donna', 'age': 27},
#     {'id': 23, 'name': 'Tyler', 'age': 52}, {'id': 24, 'name': 'Andrew', 'age': 55},
#     {'id': 25, 'name': 'Hayden', 'age': 59}, {'id': 26, 'name': 'Juan', 'age': 68},
#     {'id': 27, 'name': 'Karen', 'age': 73}, {'id': 28, 'name': 'Tracy', 'age': 56},
#     {'id': 29, 'name': 'Sherri', 'age': 70}, {'id': 30, 'name': 'David', 'age': 40},
#     {'id': 31, 'name': 'Bryan', 'age': 72}, {'id': 32, 'name': 'Emily', 'age': 59},
#     {'id': 33, 'name': 'Jeffrey', 'age': 68}, {'id': 34, 'name': 'Patty', 'age': 27},
#     {'id': 35, 'name': 'Jessica', 'age': 55}, {'id': 36, 'name': 'Angel', 'age': 28},
#     {'id': 37, 'name': 'Julie', 'age': 58}, {'id': 38, 'name': 'Christopher', 'age': 33},
#     {'id': 39, 'name': 'Emily', 'age': 73}, {'id': 40, 'name': 'Miranda', 'age': 72},
#     {'id': 41, 'name': 'Renee', 'age': 73}, {'id': 42, 'name': 'Aaron', 'age': 61},
#     {'id': 43, 'name': 'Brian', 'age': 46}, {'id': 44, 'name': 'Jason', 'age': 38},
#     {'id': 45, 'name': 'Phillip', 'age': 51}, {'id': 46, 'name': 'Steven', 'age': 27},
#     {'id': 47, 'name': 'Daniel', 'age': 75}, {'id': 48, 'name': 'Frank', 'age': 66},
#     {'id': 49, 'name': 'Julie', 'age': 61}, {'id': 50, 'name': 'Clayton', 'age': 49},
#     {'id': 51, 'name': 'Elizabeth', 'age': 64}, {'id': 52, 'name': 'Alexa', 'age': 54},
#     {'id': 53, 'name': 'Ralph', 'age': 37}, {'id': 54, 'name': 'Christine', 'age': 78},
#     {'id': 55, 'name': 'Jason', 'age': 29}, {'id': 56, 'name': 'Scott', 'age': 23},
#     {'id': 57, 'name': 'Jonathan', 'age': 31}, {'id': 58, 'name': 'Bill', 'age': 44},
#     {'id': 59, 'name': 'Matthew', 'age': 47}, {'id': 60, 'name': 'Michael', 'age': 70},
#     {'id': 61, 'name': 'Jasmine', 'age': 35}, {'id': 62, 'name': 'Paul', 'age': 39},
#     {'id': 63, 'name': 'Joseph', 'age': 71}, {'id': 64, 'name': 'Daniel', 'age': 42},
#     {'id': 65, 'name': 'Stephanie', 'age': 39}, {'id': 66, 'name': 'Jason', 'age': 38},
#     {'id': 67, 'name': 'Gabrielle', 'age': 79}, {'id': 68, 'name': 'Shannon', 'age': 35},
#     {'id': 69, 'name': 'Hayley', 'age': 60}, {'id': 70, 'name': 'James', 'age': 78},
#     {'id': 71, 'name': 'Christina', 'age': 65}, {'id': 72, 'name': 'Lee', 'age': 24},
#     {'id': 73, 'name': 'Robert', 'age': 24}, {'id': 74, 'name': 'Jack', 'age': 46},
#     {'id': 75, 'name': 'Katie', 'age': 61}, {'id': 76, 'name': 'Christopher', 'age': 34},
#     {'id': 77, 'name': 'Jennifer', 'age': 50}, {'id': 78, 'name': 'Andrea', 'age': 77},
#     {'id': 79, 'name': 'Robert', 'age': 43}, {'id': 80, 'name': 'Matthew', 'age': 29},
#     {'id': 81, 'name': 'Shannon', 'age': 38}, {'id': 82, 'name': 'Andrea', 'age': 57},
#     {'id': 83, 'name': 'Thomas', 'age': 18}, {'id': 84, 'name': 'Kerry', 'age': 78},
#     {'id': 85, 'name': 'Cory', 'age': 19}, {'id': 86, 'name': 'Amanda', 'age': 67},
#     {'id': 87, 'name': 'Melissa', 'age': 37}, {'id': 88, 'name': 'Edward', 'age': 71},
#     {'id': 89, 'name': 'Tanya', 'age': 33}, {'id': 90, 'name': 'Nicholas', 'age': 76},
#     {'id': 91, 'name': 'Raymond', 'age': 51}, {'id': 92, 'name': 'Crystal', 'age': 33},
#     {'id': 93, 'name': 'Morgan', 'age': 58}, {'id': 94, 'name': 'Warren', 'age': 75},
#     {'id': 95, 'name': 'Jeffrey', 'age': 40}, {'id': 96, 'name': 'Cynthia', 'age': 62},
#     {'id': 97, 'name': 'Whitney', 'age': 59}, {'id': 98, 'name': 'Mark', 'age': 61},
#     {'id': 99, 'name': 'Thomas', 'age': 25}, {'id': 100, 'name': 'Alexander', 'age': 75}
# ]


# with DBConnector(engine=engine) as session:
    # for obj in users:
    #     user = User(**obj)
    #
    #     session.add(user)
    # session.commit()

    # users = [
    #     User(name="Vlad", age=26),
    #     User(name="Dmitry", age=19),
    #     User(name="Irina", age=21),
    # ]
    #
    # session.add_all(users)
    # session.commit()

    # user: User = session.query(User).get(99)
    # user: User = session.query(User).filter(User.id == 99).one()
    #
    # if user:
    #     print(f"OLD AGE {user.age}")
    #     user.age += 1
    #     session.commit()
    #
    #     print(f"NEW AGE {user.age}")
    # else:
    #     print("NOT FOUND")

    # user: User = session.query(User).filter(User.id == 97).one()
    #
    # if user:
    #     session.delete(user)
    #     session.commit()
    #
    #     print("DELETED")
    # else:
    #     print("NOT FOUND")

    # user: User = session.query(User).filter(User.id == 100).one()
    # user: User = session.query(User).filter(User.id == 100)

    # print(user)

    # if user:
    #     print(user)
    #     print(f"{user.id} | {user.name} | {user.age}")
    #
    # else:
    #     print("NOT FOUND")
