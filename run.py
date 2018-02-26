from bokahilla import app


"""
 Modern convention is to write web applications using an "MVC" - "Model View Controller" structure.
 This allow your code to be segmented into logical sections which will be maintained on different cyles by different teams,
 may be shared between different applications, and may even be in different languages / formats.
 
    • Model - the business logic of the application
    • View - the template to be completed / look and feel of the page
    • Controller - top code that runs the model and renders the view
 
    Although convention is to talk "MVC", there's a fourth element that's needed - and indeed that's needed first
    • Router - How particular URLs map onto particular controllers
"""

# for development server
if __name__ == '__main__':
    app.run(debug=True)




