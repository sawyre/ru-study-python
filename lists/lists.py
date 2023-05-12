class ListExercise:
    @staticmethod
    def find_max(input_list: list[int]) -> int:
        """
        Поиск максимумального значения в списке
        
        :param input_list: Исходный список
        :return: Максимальное значение в списке
        """
        max_elem = input_list[0]

        for elem in input_list:
            if elem > max_elem:
                max_elem = elem

        return max_elem


    
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        max_elem = find_max(input_list)
        return [max_elem for elem in input_list if elem > 0 else elem]


    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        left_border = 0
        right_border = len(input_list) - 1

        while right_border - left_border > 1:
            center = left_border + right_border // 2
            if input_list[center] == query:
                return center
            elif input_list[center] > query:
                right_border = center
            else:
                left_border = center
        
        if input_list[right_border] == query:
            return right_border
        elif input_list[left_border] == query:
            return left_border
        else:
            return -1
