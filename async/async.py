import asyncio
import json


async def task_2(first_names, last_names, usernames):
    with open("second_data.json", "w") as file:
        data = {
            "first_names": first_names,
            "last_names": last_names,
            "usernames": usernames
        }
        content = json.dumps(data)
        file.write(content)
    return "Successful"


async def task_1():
    with open("first_data.json", "r") as file:
        data = json.load(file)
        print("task_1")
        first_names = []
        last_names = []
        usernames = []
        for i in data["users"]:
            first_names.append(i["first_name"])
            last_names.append(i["last_name"])
            usernames.append(i["username"])

        await task_2(first_names, last_names, usernames)


async def main():
    await asyncio.gather(task_1())

if __name__ == "__main__":
    asyncio.run(main())
