''' Created: 01/12/2023 '''

# External imports
import os
import requests
from dotenv import load_dotenv
from requests.models import Response

load_dotenv()

DATA_DIRECTORY = 'puzzles/data/'
COOKIE = 'SESSION_COOKIE'

class AOC():

    def __init__(self, puzzle_day: int):
        self.session_cookie = os.getenv(COOKIE)
        if not self.session_cookie:
            raise Exception(f'No {COOKIE} set in .env file...')
        self.day = puzzle_day

    def get_request(self, url: str) -> Response:
        headers = {'Cookie': f'session={self.session_cookie}'}
        response = requests.get(url, headers=headers)
        return response
    
    def load_puzzle(self) -> str:
        with open(f'{DATA_DIRECTORY}day_{self.day}.txt', 'r') as file:
            puzzle = file.read()
        return puzzle
    
    def save_puzzle(self, puzzle: str) -> None:
        with open(f'{DATA_DIRECTORY}day_{self.day}.txt', 'w') as file:
            file.write(puzzle)

    def get_puzzle(self):
        try:
            puzzle = self.load_puzzle()
        except FileNotFoundError:
            url = f'https://adventofcode.com/2023/day/{self.day}/input'
            response = self.get_request(url)
            if response.status_code != 200:
                raise Exception(f'Failed to fetch puzzle: HTTP status code {response.status_code}')
            puzzle = response.text.strip()
            self.save_puzzle(puzzle)
        return puzzle
