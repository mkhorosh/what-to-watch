python "C:\Users\Marina\PycharmProjects\what-to-watch\want.py"
set /p page=<"C:\\Users\\Marina\\PycharmProjects\\what-to-watch\\page.txt"
if NOT %page% == "null" explorer %page%
exit