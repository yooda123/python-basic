from asyncio import to_thread


hello = "Hello, world!"
print(hello)

today = "今日は　いい天気です"
print(hello + today)

# format
world = "hello {}".format("世界")
print(world)

print("{} {}".format(hello, today))

name = "Emily"
print("Hey, {}!! How are you doing?".format(name))

balance = 100
print("balance: {}".format(balance))


# fstring
print(f"{hello} {today}")

print(f"Hey, {name}!! How are you doing?")

print(f"balance: {balance}")