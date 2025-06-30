#class to grab data from sleeper API

import requests

base_url = "https://api.sleeper.app/v1"

class SleeperClient:
    def _init_(self, league_id):
        self.league_id = league_id
