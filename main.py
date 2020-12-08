# Объявляем функцию get_absolute_url и (не)позиционные аргументы 

def get_absolute_url(url, *args, **kwargs):
    for i in args:
    
    # Добавляем знак "/" к аргументу url

        url += '/' + i
    
    # Добавляем знак "?" к аргументу url
    
    url += '?'
    
    # Добавляем именованные аргументы
    
    for k, v in kwargs.items():
        url += '&' + k + '=' + v
    
    # Возвращаем полученное значение функции

    return url
