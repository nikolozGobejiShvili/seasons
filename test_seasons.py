import seasons

def read_numbers():
    assert seasons.read_numbers(61) == "sixty-one minutes"
    assert seasons.read_numbers(1029) == "one thousand and twenty-nine minutes"
    assert seasons.read_numbers(1048) == "one thousand and forty-eight minutes"