import spintax
import json
import re
from forocoches_api import ForocochesAPI
from random import randint


class UpThreads:

    def __init__(self):
        self.fc = None

    def load_config_file(self, config_file):
        with open(config_file, encoding="utf8") as config_file:
            return json.load(config_file)

    def random_thread(self, threads):
        threads_number = len(threads)
        random_int = randint(0, threads_number-1)
        return random_int

    def publish_message(self, message, thread_id):
        message = spintax.spin(message)
        self.fc.publish_message(thread_id, message)

    def update_last_post(self, old_post_id, thread):
        url = self.fc.g.doc.url
        new_post_id = re.findall(r"p=([0-9]*)", url)[0]
        if old_post_id != "":
            self.fc.delete_post(old_post_id)
        with open('config.json', 'r+', encoding="utf8") as f:
            data = json.load(f)
            data['threads'][thread]['last_post_id'] = new_post_id
            f.seek(0)
            json.dump(data, f, indent=2)

if __name__ == '__main__':
    up = UpThreads()
    config = up.load_config_file('config.json')
    thread = up.random_thread(config['threads'])
    username = config['threads'][thread]['account']
    password = config['forocoches_accounts'][username]
    up.fc = ForocochesAPI(username, password)
    thread_id = config['threads'][thread]['thread_id']
    message_spintax = config['threads'][thread]['words_up_thread']
    message_spintax = config['words_up_thread'][message_spintax]
    up.publish_message(message_spintax, thread_id)
    old_post_id = config['threads'][thread]['last_post_id']
    up.update_last_post(old_post_id, thread)
