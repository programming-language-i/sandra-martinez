import threading
import random



def sensor1():
    temperatura = random.randint(10, 12)
    print(f"sensor1 - temperatura: {temperatura}")

def sensor2():
    temperatura = random.randint(12, 18)
    print(f"sensor2 - temperatura: {temperatura}")

def sensor3():
    temperatura = random.randint(11, 15)
    print(f"sensor3 - temperatura: {temperatura}")

def sensor4():
    temperatura = random.randint(10, 19)
    print(f"sensor4 - temperatura: {temperatura}")

def sensor5():
    temperatura = random.randint(13, 17)
    print(f"sensor5 - temperatura: {temperatura}")                


def main():
    hilo1 = threading.Thread(target=sensor1)
    hilo2 = threading.Thread(target=sensor2)
    hilo3 = threading.Thread(target=sensor3)
    hilo4 = threading.Thread(target=sensor4)
    hilo5 = threading.Thread(target=sensor5)

    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()
    hilo5.start()

    hilo1.join()
    hilo2.join()
    hilo3.join()
    hilo4.join()
    hilo5.join()

if __name__ == "__main__":
    main()