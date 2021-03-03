from typing import List


def get_even_valued_list(lst: List[int]) -> List[int]:
    """This method get all even indices and return new list of even value."""
    if lst and len(lst) > 0:
        try:
            even_values = [lst[i] for i in
                           range(0, len(lst), 2) if lst[i] % 2 == 0]
            return even_values
        except Exception as e:
            print(f'Unable to get the new list : {e}')
