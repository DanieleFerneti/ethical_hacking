import requests


def lettura_file(filename):
    username_list = []

    with open(filename) as f:
        for line in f:
            username_list.append(line.strip())
    return username_list


def find_dir(filename, target_url):
    file = lettura_file(filename)
    for l in file:
        test_url = target_url + l
        request(test_url)


def request(url):
    try:
        get_response = requests.get(url)
        if get_response:
            print("[+] Discovered directory or file: " + url)
    except(requests.exceptions.ConnectionError):
        pass


def main():
    filename = "/root/Desktop/common_dir_and_files.txt"
    target_url = "http://192.168.186.129/mutillidae/"
    #url = "http://192.168.186.1/mutillidae/" #IP NON CONNESSO
    #print(request(url))

    find_dir(filename, target_url)


if  __name__ == "__main__":
    main()