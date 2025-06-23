
# cause there all py.file so we can import the function 
from website import create_app

app = create_app()
# if i running this file than i can do 
if __name__ == '__main__':
  app.run(debug=True)
 
