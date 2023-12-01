''' Created: 01/12/2023 '''

import os
import requests
from dotenv import load_dotenv

load_dotenv()

class AOC():

    def __init__(self, puzzle_day: int):
        self.session_cookie = os.getenv('SESSION_COOKIE')
        if not self.session_cookie:
            raise Exception('No session_cookie set in .env file...')
        self.day = puzzle_day

    def get_request(self, url: str):
        headers = {'Cookie': f'session={self.session_cookie}'}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f'Request to {url} failed. Status code: {response.status_code}')
        return response.text.strip()
    
    def get_puzzle(self):
        url = f'https://adventofcode.com/2023/day/{self.day}/input'
        return self.get_request(url)
