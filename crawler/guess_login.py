import requests


def lettura_file(filename):
    username_list = []
    with open(filename) as f:
        for line in f:
            username_list.append(line.strip())
    return username_list


def login(target_url, data_dict):
    response = requests.post(target_url, data = data_dict)
    print(response.content)

def main():
    filename = "/root/Desktop/passwords.txt"
    target_url = "http://192.168.186.129/dvwa/login.php"
    data_dict = {"username": "Kinder Merendero",
                 "password": "Kinder",
                 "Login": "submit"}
    login(target_url, data_dict)


if  __name__ == "__main__":
    main()

