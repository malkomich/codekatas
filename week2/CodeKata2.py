class TeleCoffeHandler:
    # This class handles orders for teleco's breakfast

    def __init__(self):
        # Initialize the handler to connect with the DB.
        # initORMHandler is a function in this class that is not included
        # cause it is not in the scope of this kata.
        self.mORMHandler = initORMHandler()

        # Initialize the handler to connect with the payment system
        # initWalletHandler is a function in this class that is not included
        # cause it is not in the scope of this kata.
        self.mWalletHandler = initWalletHandler()

    def getFood(foodType, foodPack):
        if not isinstance (foodType, FoodType):
            raise ValueError('foodType not valid')
        if not isinstance (foodPack, FoodPack):
            raise ValueError('foodPack not valid')

        self.mORMHandler.checkEnoughExistences(foodType.value, foodPack.value)
        foodPrize = self.mORMHandler.getPrize(foodType.value)
        self.mWalletHandler.checkEnoughMoney(foodPrize)
        self.mWalletHandler.spendMoney(foodPrize)
        return self.mORMHandler.get(foodType.value, foodPack.value)

class FoodType(Enum):
    BRAVAS = 'bravas'
    PECHUGUITO = 'pechuguito'

class FoodPack(Enum):
    UNIT = 1
    PACK = 5
