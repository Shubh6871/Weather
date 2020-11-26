import tkinter as tk
import requests

HEIGHT = 400
WIDTH = 600

def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/3.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
    
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
        

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There is a problem retrieving \nthat information'

	return final_str

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)



root = tk.Tk()

root.title("Weather")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape1.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bd=2,bg="Dark Grey")
frame.place(relx=0.45, rely=0.06, relwidth=0.65, relheight=0.1, anchor='n')


entry = tk.Entry(frame, font=('Brush Script MT',15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Brush Script MT',20), command=lambda: get_weather(entry.get()))
button.place(relx=0.65, relheight=1, relwidth=0.35)

lower_frame = tk.Frame(root, bd=2,bg="Dark Grey")
lower_frame.place(relx=0.34, rely=0.25, relwidth=0.42, relheight=0.3, anchor='n')

label = tk.Label(lower_frame, font=('Brush Script MT',18),anchor='nw',justify='left',bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()