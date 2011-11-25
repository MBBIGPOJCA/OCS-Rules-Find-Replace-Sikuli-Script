# Collect input from user on find and replace data
findString = "18" #input('Enter the find string:')
repString = "22" #input('Enter the replacement string:')

def expEditor():
    switchApp("Fuzzy Expert System Editor")
    anApp = App("Fuzzy Expert System Editor").window()
    topLeftX = anApp.getX()
    topLeftY = anApp.getY()
    setROI(topLeftX + 315,topLeftY + 70, 120, 430)

def ruleEditor():
    switchApp("Edit Statement")
    anApp = App("Edit Statement").window()
    setROI(anApp)

def sortClick():
    x.sort(lambda a,b: a.y-b.y)
    # Loop through collection
    for item in x:
        # click and edit
        click(item)

# Main code to do the find and replace
def findReplace():
    type('c', KEY_CTRL)
    oldText = Env.getClipboard()
    newText = oldText.replace(findString, repString)
    type(newText)

# Specific Assertion keystrokes
def typeAssertion():
    ruleEditor()
    click(Pattern("1322004321171.png").targetOffset(-57,0))
    if exists("XAnewasserti.png"):
        click(Pattern("XAnewasserti.png").targetOffset(-41,25))    

# Specific Comparison keystrokes 
def typeComparison():
    type(Key.TAB,KEY_SHIFT)
    findReplace()
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    findReplace()
    ruleEditor()
    click(Pattern("1322004321171.png").targetOffset(-57,0))

# Specific Assignment keystrokes
def typeAssignment():
    type(Key.TAB,KEY_SHIFT)
    findReplace()
    type(Key.TAB)
    type(Key.TAB)
    findReplace()
    ruleEditor()
    click(Pattern("1322004321171.png").targetOffset(-57,0))

#Assertion
expEditor()
if exists(Pattern("1321543588117-1.png").similar(0.95)):
    # Make a list of these icons
    x = list(findAll(Pattern("1321543588117-1.png").similar(0.95)))
    x.sort(lambda a,b: a.y-b.y)
    # Loop through collection
    for item in x:
        # click and edit
        click(item)
        type('e', KEY_ALT)
        # Is this an Assertion? 
        ruleEditor()
        if find("QAssertion.png").below().exists("Text.png"):
            findReplace()
            typeAssertion()    

#Comparison
expEditor()
if exists(Pattern("1321547477865.png").similar(0.95)):
    # Make a list of these icons
    x = list(findAll(Pattern("1321547477865.png").similar(0.95)))
    x.sort(lambda a,b: a.y-b.y)
    # Loop through collection
    for item in x:
        # click and edit
        click(item)
        type('e', KEY_ALT)
        # Is this an Comparison? 
        ruleEditor()
        if find("EFuzzystatem-1.png").below().exists("Compare.png"):
            typeComparison() 

#Assignment
expEditor()
if exists(Pattern("1321547612803.png").similar(0.95)):
    # Make a list of these icons
    x = list(findAll(Pattern("1321547612803.png").similar(0.95)))
    x.sort(lambda a,b: a.y-b.y)
    # Loop through collection
    for item in x:
        # click and edit
        click(item)
        type('e', KEY_ALT)
        # Is this an Assignment? 
        ruleEditor()
        if find("QAssertion-1.png").below().exists("Locaoutputob.png"):
                if find("Locaoutputob-1.png").right().exists("Assign-1.png"):
                    typeAssignment()

                else:
                    findReplace()
                    ruleEditor()
                    click(Pattern("1322004321171.png").targetOffset(-57,0))
      