from datafeed.server3 import run, App, generate_csv
import os

print(__name__)

if __name__ == '__main__':
    if not os.path.isfile('test.csv'):
        print("No data found, generating...")
        generate_csv()
    run(App())
