calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return
def string_info(string):
    info = (len(string), string.upper(), string.lower())
    print(info)
    count_calls()
    return
def is_contains(string, list_to_search):
    a = list(map(str.upper, list_to_search))
    b = string.upper()
    if a.count(b):
        print(True)
    else:
        print(False)
    count_calls()
    return
string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)

