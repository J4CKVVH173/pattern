class Singleton:

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


s = Singleton()

s.lol = 12

s_new = Singleton()

print(s_new.lol, '\n')

print(s, '<===>', s_new)

