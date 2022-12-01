def main():
    with open('input.txt') as f:
        contents = f.read()
        elves_str = contents.strip().split('\n\n')
        elves = []
        for elf in elves_str:
            calories_str = elf.split('\n')
            elves.append(sum([int(x) for x in calories_str]))
        print(max(elves))

if __name__ == "__main__":
    main()
