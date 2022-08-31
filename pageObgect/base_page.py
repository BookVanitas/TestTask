class BasePage:

    @staticmethod
    def foo(point: int) -> int:
        # реализовал "автомат", в котором могут быть ошибки (на негативных тестах) ;)
        sale = 0.01
        if 100 < point <= 200:
            sale = 0.03
        elif 200 < point <= 500:
            sale = 0.05
        elif 500 < point:
            sale = 0.1

        return sale
