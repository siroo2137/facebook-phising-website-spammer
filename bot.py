import requests
import random
import string
import threading

def generate_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(16))

i = 0
lock = threading.Lock()  # Thread-safe lock
session = requests.Session()  # Use a session object for connection reuse

def worker(url, form_data):
    global i
    try:
        response = session.post(url, data=form_data)
        with lock:
            print("[{}] status code: {}".format(i, response.status_code))
            i += 1
    except requests.exceptions.RequestException as e:
        print("[{}] Error: {}".format(i, str(e)))
        with lock:
            i += 1

def main():
	while True:
		url = 'https://cdn-home.store/post.php?p1=true'
		thread_count = 20  # Adjust the number of threads as needed
		form_data = {
			'ut': 'trabajador1',
			'uu': 'happy pride month 🥳🥳🥳🥳🥳_' + generate_random_string(),
			'pp': 'happy pride month 🥳🥳🥳🥳🥳_' + generate_random_string(),
		}

		threads = []
		for _ in range(thread_count):
			thread = threading.Thread(target=worker, args=(url, form_data))
			thread.start()
			threads.append(thread)

		for thread in threads:
			thread.join()

if __name__ == '__main__':
    main()
