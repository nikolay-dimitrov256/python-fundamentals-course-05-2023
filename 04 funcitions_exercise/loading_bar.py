def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    percent_loaded = some_number // 10
    remaining = 10 - percent_loaded
    return f"{some_number}% [{percent_loaded * '%'}{remaining * '.'}]\nStill loading..."


number = int(input())
print(loading_bar(number))
