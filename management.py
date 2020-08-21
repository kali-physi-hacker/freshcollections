import argparse
import sys
import subprocess


command = f"['python', 'manage.py', '{' '.join(sys.argv[3:])}', '--settings=estore.settings."


def main():
    parser = argparse.ArgumentParser(description="Example: python management.py dev -c 'runserver'")
    parser.add_argument("mode", help="Environment Mode (prod for production and dev for development)")
    parser.add_argument("-c", "--command", help="Command to execute")
    options = parser.parse_args()

    global command

    if options.mode == "dev" or options.mode == "development":
        command += "dev']"
    elif options.mode == "prod" or options.mode == "production":
        command += "prod']"

    subprocess.call(eval(command))
    # print(command)


main()
