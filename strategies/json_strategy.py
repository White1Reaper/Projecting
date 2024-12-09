from strategies.strategy import Strategy
import json


# Стратегия для работы с JSON
class JsonStrategy(Strategy):
    def __init__(self,file):
        self.file=file

    def read_all(self):
        try:
            with open(self.file, 'r') as f:
                content = f.read()
                if not content.strip():
                    return []
                data = json.loads(content)
                return data
        except json.JSONDecodeError as e:
            print(f"Ошибка разбора JSON: {e}")
            return []

    def write_all(self, data):
        with open(self.file, 'w') as f:
            json.dump(data, f)
