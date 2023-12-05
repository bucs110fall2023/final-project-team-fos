#import your controller
from src.controller import Controller
 
def main():
    #Create an instance on your controller object
    controller = Controller()
    #Call your mainloop
    controller.mainloop() 
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

main()