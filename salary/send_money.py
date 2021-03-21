import money

def send_money(salary):
    money.saved_money += salary
    print(f"发工资啦,发了{salary}")