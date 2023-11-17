import pets

def main():
    dog = pets.Pet('Golden Retriever', 'Bucky', 50, 'Gold', 4)
    print(dog.name, dog.weight)
    dog.feed(1800)
    print(dog.weight)
    dog.walk(1.5)
    print(dog.weight)

if __name__ == "__main__":
    main()