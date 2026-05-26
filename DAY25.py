class Room:
    def __init__(self, name):
        self.name = name
        self.next = None


def print_maze_path(start, steps=15):
    current = start
    count = 0

    while current and count < steps:
        print(current.name, end=" -> ")
        current = current.next
        count += 1

    print("END")

def detect_cycle(start):
    slow = start
    fast = start

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

a = Room("Entrance")
b = Room("Hallway")
c = Room("Treasure Room")
d = Room("Exit")

a.next = b
b.next = c
c.next = d

print("Maze A Path:")
print_maze_path(a)

print("Cycle Detected:", detect_cycle(a))

x = Room("Start")
y = Room("Tunnel")
z = Room("Dark Chamber")

x.next = y
y.next = z
z.next = y

print("\nMaze B Path:")
print_maze_path(x)

print("Cycle Detected:", detect_cycle(x))

s = Room("Trap Room")
s.next = s

print("\nMaze C Path:")
print_maze_path(s)

print("Cycle Detected:", detect_cycle(s))