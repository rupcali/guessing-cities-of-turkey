import turtle
import pandas

screen = turtle.Screen()
screen.title = "Turkey Cities Game"
image = "yeni_harita.gif"
screen.addshape(image)
screen.setup(width=800, height=500)
turtle.shape(image)

# used this code to determine the coordinates of the cities

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


correct_guess = 0

data = pandas.read_csv("81_cities.csv")
city_list = data["city"].tolist()
guessed_cities = []


while len(guessed_cities) != 81:
    answer_city = (screen.textinput(title=f"{correct_guess}/81 Şehri Doğru Bildiniz",
                                    prompt="Bir şehir girin. Çıkmak için çıkış yazın.")).title()
    print(answer_city)
    if answer_city == "Çıkış":
        missing_cities = []
        for city in city_list:
            if city not in guessed_cities:
                missing_cities.append(city)
        new_data = pandas.DataFrame(missing_cities)
        new_data.to_csv("cities_to_learn.csv")
        break
    if answer_city in city_list:
        correct_guess += 1
        guessed_cities.append(answer_city)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        city_data = data[data.city == answer_city]
        t.goto(float(city_data.x), float(city_data.y))
        t.write(answer_city)


# used this part of code to see the names of the cities in their position and rearrange

# for city in city_list:
#     t = turtle.Turtle()
#     t.hideturtle()
#     t.penup()
#     city_data = data[data.city == city]
#     t.goto(float(city_data.x), float(city_data.y))
#     t.write(city)


