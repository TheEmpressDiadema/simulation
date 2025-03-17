class Menu:
    
    def __init__(self):
        self._items = [
            "1. Начать",
            "2. Пауза",
            "3. Выход"
        ]
    
    @property
    def items(self):
        return self._items