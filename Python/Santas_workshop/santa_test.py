"""EX15 tests."""

import unittest
from EX.ex15_santas_workshop.santas_workshop import Main
from EX.ex15_santas_workshop.santas_workshop import Child
from EX.ex15_santas_workshop.santas_workshop import Toys


class TestChild(unittest.TestCase):
    """Class Child tests."""

    def test_repr(self):
        """Child repr test."""
        toy1 = Toys("Toy 1", 10, 10, 10)
        toy2 = Toys("Toy 2", 10, -5, -111)
        child = Child('John', 'USA', [toy1, toy2])
        self.assertEqual(str(child), f'name: John, country: USA, wish: [{toy1}, {toy2}]')


class TestToys(unittest.TestCase):
    """Class toys tests."""

    def test_repr(self):
        """Toy repr test."""
        toy = Toys('Toy 1', 10, 2, 50)
        self.assertEqual(str(toy), 'gift: Toy 1, material_cost: 10, production_time: 2, weight int grams: 50')

    def test_repr_values_negative(self):
        """Negative values fix test."""
        toy = Toys("Toy 1", -5, -2, -11111)
        self.assertEqual((str(toy)), 'gift: Toy 1, material_cost: 0, production_time: 0, weight int grams: 0')


class TestMain(unittest.TestCase):
    """Class main tests."""

    def test_get_id(self):
        """ID extracting test."""
        main = Main('', '', '')
        self.assertEqual(main.get_id('https://docs.google.com/spreadsheets/d/123456789/edit'), '123456789')

    def test_add_child(self):
        """Good child add test."""
        main = Main('', '', '')
        kid = Child('John', 'USA', ['Toy 1', 'Toy 2'])
        main.add_child(kid)
        self.assertEqual(len(main.get_children()), 1)

    def test_get_children(self):
        """Good children return test."""
        main = Main('', '', '')
        kid = Child('John', 'USA', ['Toy 1', 'Toy 2'])
        main.add_child(kid)
        self.assertEqual(main.get_children(), [kid])

    def test_get_toys(self):
        """Toy return test."""
        main = Main('', '', '')
        toy = Toys('Toy 1', 10, 2, 50)
        main.add_toy(toy)
        self.assertEqual(main.get_toys(), [toy])

    def test_search_toys_works(self):
        """Toy search test."""
        main = Main('', '', '')
        toy = Toys("lego", 5, 5, 5)
        main.add_toy(toy)
        self.assertEqual(main.search_storage("lego"), f"Found {toy.gift} in storage 1x")

    def test_search_toys_not_work(self):
        """Search toy method test."""
        main = Main('', '', '')
        self.assertEqual(main.search_storage("lego"), "Item lego not found 404 :(")

    def test_search_children_work(self):
        """Search child method test."""
        main = Main('', '', '')
        kid = Child('John', 'USA', ['Toy 1', 'Toy 2'])
        main.add_child(kid)
        self.assertEqual(main.search_children("John"), f"Found {kid}")

    def test_search_children_not_work(self):
        """Search child method test."""
        main = Main('', '', '')
        self.assertEqual(main.search_children("John"), "Child John not found 404 :(")

    def test_get_link(self):
        """Link generation test."""
        main = Main('', '', '')
        self.assertEqual(main.generate_link("swimming flippers"),
                         "https://cs.ttu.ee/services/xmas/gift?name=swimming%20flippers")

    def test_get_data_from_web_for_toy(self):
        """Toy generation test with only name."""
        main = Main('', '', '')
        main.add_toy("swimming flippers")
        self.assertEqual(len(main.get_toys()), 1)

    def test_sheets_API(self):
        """Google sheets API test."""
        main = Main('', '', '')
        self.assertEqual(len(list(main.get_data_from_sheets(
            "https://docs.google.com/spreadsheets/d/1AbaMB_uRin4Rsg_EKLP7-e6_SeXCCtiEXRr_noA8brg/edit#gid=0").keys())), 108)

    def test_main_method_works(self):
        """Main method test."""
        main = Main(
            "https://docs.google.com/spreadsheets/d/1kKynKfUrvgsI-lKdSNEKqzcxQQQPECTZ-0TNnLL0aKY/edit?usp=sharing",
            "https://docs.google.com/spreadsheets/d/1AbaMB_uRin4Rsg_EKLP7-e6_SeXCCtiEXRr_noA8brg/edit?usp=sharing",
            "https://docs.google.com/spreadsheets/d/17lUfaWL72seP2TLu7TR0smev-T8ktB0Yb1oxr16AV6Y/edit?usp=sharing")
        main.main_method()
        self.assertEqual(len(main.get_children()), 291)

    def test_main_method_not_work(self):
        """Main method test with broken links."""
        main = Main('', '', '')
        self.assertEqual(main.main_method(), "One or more given links is broken")

    def test_remove_from_storage_works(self):
        """Remove from storage test."""
        main = Main('', '', '')
        toy = Toys("lego", 5, 5, 5)
        main.add_toy(toy)
        main.remove_from_storage("lego")
        self.assertEqual(main.get_toys(), [])

    def test_remove_from_storage_not_work(self):
        """Remove from storage test with broken item."""
        main = Main('', '', '')
        self.assertEqual(main.remove_from_storage("lego"), "Item lego not in list 404")


if __name__ == '__main__':
    unittest.main()
