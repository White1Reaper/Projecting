
import yaml
from strategies.strategy import Strategy


# Стратегия для работы с YAML
class YamlStrategy(Strategy):
    def __init__(self,file):
        self.file=file

    def read_all(self):
        try:
            with open(self.file, 'r') as f:
                return yaml.safe_load(f) or []
        except yaml.YAMLError as e:
            print(f"Ошибка разбора YAML: {e}")
            return []

    def write_all(self, data):
        with open(self.file, 'w') as f:
            yaml.dump(data, f)