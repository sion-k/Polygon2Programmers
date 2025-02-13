import os
import argparse
from problem import Problem
from export import export


def main():
    for directory in os.listdir(path):
        if os.path.isdir(os.path.join(path, directory)):
            problem = Problem.from_path(os.path.join(path, directory))

            print(problem.name)

            if not os.path.exists(os.path.join(output)):
                os.mkdir(os.path.join(output))

            export(problem, os.path.join(output, problem.name))


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "path", help="path containing one or more polygon problems")

    # output
    argparser.add_argument(
        "-o", "--output", help="output directory", default="output")

    args = argparser.parse_args()
    path = args.path
    path = os.path.normpath(path)

    output = args.output
    output = os.path.normpath(output)

    main()
