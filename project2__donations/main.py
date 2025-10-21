donations = {
    "morteza": 300,
    "ali": 200,
    "reza": 400,
    "sara": 800,
}

def get_donation(donation_list):
    count = 0
    count_plus = 0
    avg = 0
    max_donate_value = list(donation_list.values())[0]
    max_donate_person = ""

    for key, value in donation_list.items():
        count += 1
        count_plus += value
        if value > max_donate_value:
            max_donate_value = value
            # max_donate_person = key      # easy way
    index_of_max_value = list(donation_list.values()).index(max_donate_value)
    max_donate_person = list(donation_list.keys())[index_of_max_value]
    avg += int(count_plus / count)

    return count_plus, avg, max_donate_person

jam, motavaset, bishtarin_donate = get_donation(donations)

print(f"jame donate ha: {jam}\nva motavaset donate ha: {motavaset}\nbishtarin donate tavasot [{bishtarin_donate}] anjam gerefteh")
