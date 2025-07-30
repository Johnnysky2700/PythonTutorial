
# Global scope
name = "Sky"
count = 1

# Local scope
def another():
    color = "blue"
    global count 
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Sky")

another()