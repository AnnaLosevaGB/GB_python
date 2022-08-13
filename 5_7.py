import json

with open('text_7.txt', 'r', encoding='utf-8') as file_7:
    company = [{}]
    count = 0
    all_profit = 0
    for line in file_7:
        now_list = list(line.split())
        profit = float(now_list[2]) - float(now_list[3])
        company[0][now_list[0]] = profit
        if profit > 0:
            count += 1
            all_profit += profit
    company.append({'average_profit': round(all_profit / count, 2)})
    with open('text_77.json', 'w', encoding='utf-8') as file_77:
        json.dump(company, file_77, ensure_ascii=False, indent=4)
