import argparse

from awesome_codename import generate_codename


def main():
    """Command line interface."""
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, nargs='?', default=1,
                        help="Number of codenames to generate")

    args = parser.parse_args()
    if args.n < 0:
        # Easter egg: run indefinitely if a negative number is given :)
        while True:
            print(generate_codename())
    else:
        for _ in range(args.n):
            print(generate_codename())


if __name__ == "__main__":
    main()
