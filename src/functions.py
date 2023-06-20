def read_json():
    """
    Читает файл json и возвращает его содержимое
    :return:данные в виде списка словарей
    """
    pass

def get_executed_operations(operation_list):
    """
    Функция определяет статуст перевода
    :param operation_list: Список со словарями с данными по операциям
    :return: Список из 5 успешных операций
    """
    pass

def format_from_account(input_from_account):
    '''
    Функция скрывает номер карты отправителя
    :param input_from_account: Номер счёта отправителя
    :return: Скрытый счёт отправителя
    '''
    pass

def format_to_account(input_to_account):
    """
    Функция скрывает номер карты получателя
    :param input_to_account: Номер счёта получателя
    :return: Скрытый счёт получателя
    """
    pass

def format_date(input_date):
    """
    Форматирует дату и время операции оставляя только дату в нужном формате
    :param input_date: Строка с данными о дате и времени операции
    :return: Строка с данными о дате в заданном формате
    """
    pass

def get_message(operation):
    '''
    Функция создаст структуру выводящего сообщения
    :param operation: Работаем со словарём файла operations.json
    :return: Готовое сообщение с данными
    '''
    pass
