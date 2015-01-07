import easygui
flavor = easygui.buttonbox("What's your favorite color?",choices = ["red","green","blue"])
easygui.msgbox("You picked "+flavor)

color = easygui.choicebox("Color",choices = ["R","G","B"])
print (color)
