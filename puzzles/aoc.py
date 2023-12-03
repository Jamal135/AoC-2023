''' Created: 01/12/2023 '''

import os
import requests
from dotenv import load_dotenv

load_dotenv()

DATA_DIRECTORY = 'puzzles/data/'

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
    
    def load_puzzle(self):
        with open(f'{DATA_DIRECTORY}day_{self.day}.txt', 'r') as file:
            contents = file.read()
        return contents
    
    def save_puzzle(self, response):
        with open(f'{DATA_DIRECTORY}day_{self.day}.txt', 'w') as file:
            file.write(response)

    def get_puzzle(self):
        try:
            puzzle = self.load_puzzle()
        except FileNotFoundError:
            url = f'https://adventofcode.com/2023/day/{self.day}/input'
            puzzle = self.get_request(url)
            self.save_puzzle(puzzle)
        return puzzle
