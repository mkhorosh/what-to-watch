python "C:\Users\Marina\rep\what_to_watch\want.py"
set /p page=<"C:\\Users\\Marina\\rep\\what_to_watch\\page.txt"
if NOT %page% == "null" explorer %page%
pause