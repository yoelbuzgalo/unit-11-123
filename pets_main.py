import pets

def main():
    dog = pets.Pet('Golden Retriever', 'Bucky', 50, 'Gold', 4)
    print(dog.get_name(), dog.get_weight())
    dog.feed(1800)
    print(dog.get_weight())
    dog.walk(1.5)
    print(dog.get_weight())

if __name__ == "__main__":
    main()