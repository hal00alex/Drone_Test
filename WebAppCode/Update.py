import webbrowser 
#write-html.py 
f = open('helloworld.html', 'w') 
message = """<html> 
<head></head>
<body><p>Drone Dis-Play</p></body>
</html> """ 

f.write(message) 
f.close()

webbrowser.open_new_tab('helloworld.html')
