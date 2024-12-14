from controllers.observer import Observer
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer) -> None:
        self.observers.append(observer)
        print("наблюдатель добавлен")
    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)
            print("уведомление получил!")
