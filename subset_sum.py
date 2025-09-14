from typing import List

def subset_sum(arr: List, total: int) -> bool:
    """
    Subset Sum!

    Idea: keep a running set (no duplicates) of (valid) subtotals and check each new values across each

    Runtime: O(n * total)
    -> total is there because the number of (unique) valid subtotals <= total (0, 1, ..., total-1) and 
        n since we iterate across each value in the array

    Space: O(total)
    -> number of (unique) valid subtotals <= total
    """
    
    assert total > 0

    # running subtotals < total
    subtotals = set([0])

    for val in arr:
        new_values = set()
        for subtotal in subtotals:

            # We make a choice -- add the value or not
            # the choice is handled by the initial 0 existing
            # so we can iterate across all of the choices
            new_val = subtotal + val
            if new_val == total:
                return True
            elif new_val < total:
                new_values.add(new_val)

        subtotals |= new_values

    return False
