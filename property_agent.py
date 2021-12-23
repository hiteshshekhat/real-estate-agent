from utils import get_valid_input


class Property:
    def __init__(self, square_feet="", bedrooms="", bathrooms="", **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def display(self):
        print("#" * 20)
        print("Property Deatils")
        print("")
        print(f"Square Feet : {self.square_feet}")
        print(f"Bedrooms : {self.bedrooms}")
        print(f"Bathrooms : {self.bathrooms}")
        print("")
        return ""

    @staticmethod
    def prompt_init():
        return dict(
            square_feet=input("Enter square feet : "),
            bedrooms=input("Enter bedrooms : "),
            bathrooms=input("Enter bathrooms : "),
        )


# init = Property.prompt_init()
# print(init)
# # print(**init)
# p = Property(**init)
# print(p.dispaly())


class Apartment(Property):
    laundry_options = ("coin", "ensuite", "none")
    balcony_options = ("yes", "no", "solarium")

    def __init__(self, laundry="", balcony="", **kwargs):
        super().__init__(**kwargs)
        self.laundry = laundry
        self.balcony = balcony

    def display(self):
        super().display()
        print("APARMENT DETAIL")
        print(f"Laundry type : {self.laundry}")
        print(f"BAlcony type : {self.balcony}")
        print()

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input("Enter laundry type :", Apartment.laundry_options)
        balcony = get_valid_input("Enter balcony type :", Apartment.balcony_options)
        parent_init.update(
            {
                "laundry": laundry,
                "balcony": balcony,
            }
        )
        return parent_init


class House(Property):
    garrage_options = ("attached", "detached", "none")
    fence_option = ("yes", "no")

    def __init__(self, no_of_stories="", garrage="", fence="", **kwargs):
        super().__init__(**kwargs)
        self.garrage = garrage
        self.fence = fence
        self.no_of_stories = no_of_stories

    def display(self):
        super().display()
        print("HOUSE DETAIL")
        print(f"How many storeies House has ??")
        print(f"Garrage facility : {self.garrage}")
        print(f"Fence availability : {self.fence}")
        print()

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        no_of_stories = input("How many stories house have ?? : ")
        garrage = get_valid_input("Enter garrage facility type", House.garrage_options)
        fence = get_valid_input("Enter fence availability", House.fence_option)
        parent_init.update(
            {
                "no_of_stories": no_of_stories,
                "garrage": garrage,
                "fence": fence,
            }
        )
        return parent_init


class Purchase:
    def __init__(self, price="", taxes="", **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAIL")
        print(f"Selling price : {self.price}")
        print(f"Taxes : {self.taxes}")

    @staticmethod
    def prompt_init():
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "),
        )



class Rental:
    def __init__(self, rent="", utilities="",furnished='', **kwargs):
        super().__init__(**kwargs)
        self.rent = rent
        self.utilities = utilities
        self.furnished=furnished

    def display(self):
        super().display()
        print("RENTAL DETAIL")
        print(f"Rent : {self.rent}")
        print(f"Number of utilities : {self.utilities}")
        print(f'Is the property furnished ??? {self.furnished}')

    @staticmethod
    def prompt_init():
        return dict(
            rent=input("What is the rent ? "),
            utilities=input("How many utilities are included ? "),
            furnished =get_valid_input('Is the property furnished ?', ('yes','no'))
        )



class HouseRental(Rental,House):
    @staticmethod
    def prompt_init():
        house_init = House.prompt_init()
        house_init.update(Rental.prompt_init())
        return house_init


class HousePurchase(Purchase,House):
    @staticmethod
    def prompt_init():
        house_init = House.prompt_init()
        house_init.update(Purchase.prompt_init())
        return house_init

    

class ApartmentRental(Rental,Apartment):
    @staticmethod
    def prompt_init():
        apartment_init = Apartment.prompt_init()
        apartment_init.update(Rental.prompt_init())
        return apartment_init


class ApartmentPurchase(Purchase,Apartment):
    @staticmethod
    def prompt_init():
        apartment_init = Apartment.prompt_init()
        apartment_init.update(Purchase.prompt_init())
        return apartment_init


class Agent:
    type_map = {
        ('house','purchase') : HousePurchase,
        ('house','rental') : HouseRental,
        ('apartment','purchase') : ApartmentPurchase,
        ('apartment','rental') : ApartmentRental,
    }

    def __init__(self):
        self.property_list = []

    def display_property(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = get_valid_input('What is the type of property ??', ('house','apartment'))
        payment_type = get_valid_input('What to do with the property', ('rental','purchase'))
        PropertyClass = self.type_map[(property_type,payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
        print('Property added')



a = Agent()
a.add_property()
a.add_property()
a.add_property()
a.add_property()

a.display_property()
