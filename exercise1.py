staff = [
  {
    "name": "Ibrahim",
    "role": "admin",
    "rank": 3,
  },
  {
    "name": "Mehmet",
    "role": "moderator",
    "rank": 2,
  },
  {
    "name": "Arbesa",
    "role": "user",
    "rank": 0
  },
]


def grant_access(st):
  if (st["role"] == "moderator" or st["role"] == "admin") and st["rank"] >= 2:
    print("Open the door for ", st["name"])
  else:
    print("You shall not pass!")



inputi = ""
while inputi != "q":
  inputi = input("Tregona emrin ju lutemi ")
  if inputi == 'h':
    print("To exit the program please enter q")
  else:
    usersFound = []
    for x in staff:
      if x["name"] == inputi:
        grant_access(x)
        usersFound.append(x)

    if len(usersFound) == 0 and inputi != 'q':
      print('No user found')

