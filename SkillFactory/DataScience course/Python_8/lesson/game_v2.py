"""Игра угадай число
Компьютер сам загадывает число и сам угадывает"""
import numpy as np

def randome_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break #выход из цикла если угадали
    
    return(count)

def score_game(randome_predict) ->int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш подход

    Args:
        randome_predict (_type_): функция угадывания

    Returns:
        int: среднее число попыток
    """
    
    count_ls=[]
    np.random.seed(1) # фиксируем seed для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(randome_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток ")
    return score
    
if __name__ == "__main__":
#RUN
    score_game(randome_predict)

#print(f"Количество попыток: {randome_predict(10)}")