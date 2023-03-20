"""EX15 santas workshop."""

from __future__ import print_function
import requests
import os.path
import ast
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tqdm import tqdm


class Child:
    """Class child for to generate child objects."""

    def __init__(self, name: str, country: str, wish: list):
        """Class child constructor."""
        self.name = name
        self.country = country
        self.wish = wish

    def __repr__(self):
        """Class Child repr."""
        return f"name: {self.name}, country: {self.country}, wish: {self.wish}"


class Toys:
    """Class toys to generate toys."""

    def __init__(self, gift, material_cost, production_time, weight_in_grams):
        """Class Toys constructor."""
        self.gift = gift
        if material_cost < 0:
            self.material_cost = 0
        else:
            self.material_cost = material_cost
        if production_time < 0:
            self.production_time = 0
        else:
            self.production_time = production_time
        if weight_in_grams < 0:
            self.weight_in_grams = 0
        else:
            self.weight_in_grams = weight_in_grams

    def __repr__(self):
        """Repr for class toys."""
        return f"gift: {self.gift}, material_cost: {self.material_cost}, production_time: {self.production_time}, weight int grams: {self.weight_in_grams}"


class Main:
    """Class Main where all classes will be combined."""

    def __init__(self, nice_children_link: str, naughty_children_link: str, wish_list_link: str):
        """Class Main constructor."""
        self.children = []
        self.toys = []
        self.nice = nice_children_link
        self.naughty = naughty_children_link
        self.wish = wish_list_link

    def add_child(self, child):
        """Add good child."""
        if isinstance(child, Child):
            self.children.append(child)

    def get_children(self):
        """Return good children."""
        return self.children

    def get_toys(self):
        """Return toys from storage."""
        return self.toys

    def get_id(self, link: str):
        """Extract id from link given if possible."""
        listed = link.split("/")
        if "docs.google.com" in listed:
            return listed[-2]
        else:
            return -1

    def get_bad_children(self):
        """Return list of children who are naughty."""
        return list(self.get_data_from_sheets(self.naughty).keys())

    def get_data_from_sheets(self, link: str):
        """Google sheets reader."""
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

        # The ID and range of a sample spreadsheet.
        SAMPLE_SPREADSHEET_ID = self.get_id(link)
        if SAMPLE_SPREADSHEET_ID == -1:
            return -1
        SAMPLE_RANGE_NAME = 'A1:n'

        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return -1

            result = {}
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                result[row[0]] = row[1:]
            return result
        except HttpError as err:
            print(err)

    def add_toy(self, item):
        """Add toy into storage if input is Toy object if not pulls data from web and generates toy if possible."""
        if isinstance(item, Toys):
            self.toys.append(item)
        else:
            if isinstance(item, str):
                data = self.get_gift_data(item)
                data = ast.literal_eval(data)
                if data.get("message") is None:
                    self.toys.append(
                        Toys(data["gift"], data["material_cost"], data["production_time"], data["weight_in_grams"]))

    def remove_from_storage(self, item_name):
        """Remove toy from storage if possible."""
        filtered = self.toys
        filtered = list(filter(lambda t: t.gift == item_name, filtered))
        if len(filtered) > 0:
            self.toys.remove(filtered[0])
        else:
            return f"Item {item_name} not in list 404"

    def get_gift_data(self, item):
        """Web data puller."""
        link = self.generate_link(item)
        r = requests.get(link)
        return r.text

    def generate_link(self, name):
        """Turn wish into link."""
        link_base = "https://cs.ttu.ee/services/xmas/gift?name="
        splitted = name.split(" ")
        if len(splitted) > 1:
            word = ""
            for i in range(len(splitted)):
                if i == len(splitted) - 1:
                    break
                else:
                    word += splitted[i] + "%20"
            word += splitted[-1]
            return link_base + word
        else:
            return link_base + name

    def search_storage(self, item):
        """Search if item given is in storage."""
        items = self.toys
        filtered = list(filter(lambda t: t.gift == item, items))
        if len(filtered) > 0:
            return f"Found {item} in storage {len(filtered)}x"
        else:
            return f"Item {item} not found 404 :("

    def search_children(self, name):
        """Search if child is in good children list."""
        items = self.children
        filtered = list(filter(lambda t: t.name == name, items))
        if len(filtered) > 0:
            return f"Found {filtered[0]}"
        else:
            return f"Child {name} not found 404 :("

    def main_method(self):
        """Turn data in link into child objects with wish list containing Toy objects."""
        children = self.get_data_from_sheets(self.nice)
        wishes1 = self.get_data_from_sheets(self.wish)
        if isinstance(children, dict) and isinstance(wishes1, dict):
            children = self.get_data_from_sheets(self.nice).items()
        else:
            return "One or more given links is broken"
        for child, country in tqdm(children, desc="Generating children", total=len(children)):
            wishes = wishes1[child]
            temporary_wishes = []
            for wish in wishes:
                link = self.get_gift_data(wish)
                link = ast.literal_eval(link)
                # temporary_wishes.append(Toys(link[0], link[1], link[2], link[3]))
                self.toys.append(
                    Toys(link["gift"], link["material_cost"], link["production_time"], link["weight_in_grams"]))
                temporary_wishes.append(
                    Toys(link["gift"], link["material_cost"], link["production_time"], link["weight_in_grams"]))
            self.add_child(Child(child, country[0], temporary_wishes))


if __name__ == '__main__':
    main = Main(
        "https://docs.google.com/spreadsheets/d/1kKynKfUrvgsI-lKdSNEKqzcxQQQPECTZ-0TNnLL0aKY/edit?usp=sharing",
        "https://docs.google.com/spreadsheets/d/1AbaMB_uRin4Rsg_EKLP7-e6_SeXCCtiEXRr_noA8brg/edit?usp=sharing",
        "https://docs.google.com/spreadsheets/d/17lUfaWL72seP2TLu7TR0smev-T8ktB0Yb1oxr16AV6Y/edit?usp=sharing")
    print(main.main_method())
    print(main.children)
