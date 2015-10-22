# How to Execute the user defined python methods using variables, read from Excel sheet
def ExecuteKeyword(driver, User_keyword, Argument)    # User_keyword = ClickLink , Argument = SignInLink
            function = globals()[User_Keyword]
            function(driver,Arguments)            # Equivalent to ClickLink(driver,SingnInLink)
