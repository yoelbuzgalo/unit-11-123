import pets

def main():
    dog = pets.Pet('Golden Retriever', 'Bucky', 50, 'Gold', 4)
    print(dog.name, dog.weight)

if __name__ == "__main__":
    main()