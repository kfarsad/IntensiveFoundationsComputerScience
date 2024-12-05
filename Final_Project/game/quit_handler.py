import turtle

class QuitHandler:
    @staticmethod
    def quit_game(x=None, y=None):
        """
        Close the Turtle graphics window when the quit button is clicked
        or the quit key is pressed.
        """
        print("Exiting game...")
        turtle.bye()

    @staticmethod
    def bind_quit_button(screen):
        """
        Bind the quit functionality to the 'q' key for keyboard interaction.
        """
        screen.onkey(QuitHandler.quit_game, "q")
        screen.listen()

    @staticmethod
    def bind_quit_click():
        """
        Bind the quit functionality to a mouse click on the quit button.
        """
        turtle.onscreenclick(QuitHandler.quit_game)

