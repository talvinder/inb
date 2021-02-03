
# * importing LinkedIn
import LinkedIn
# * importing `LinkedInConnections`
import LinkedInConnections
# * importing `LinkedInJobs`
import LinkedInJobs
# * importing `OS`
import os
# * importing `readline` this we need to import becuase when
# * we take input from the terminal window and we press arrow
# * keys then the characters that corresponds to the pressed
# * key gets printed and we don't need that we need the cursor
# * moving on pressing arrow keys.
import readline
# * importing `getpass` to take user password
import getpass
# * importing `colorama`
import colorama


class Main(object):
    """
    Class Main is the main class that gets executed after the user

    hits the command `./run.sh` on the terminal screen, this class 

    gives the `cli` (Command Line Interface) to the user. We don't

    have `GUI` (Graphical User Interface) here because I don't have

    any deign Idea in my mind yet.  
    """

    def __init__(self):
        """
        Method __init__() initialize the commands and required variables,

        it also prints the Logo on the screen.
        """
        self.init_commands()    # ? initialize commands

        self.init_vars()        # ? initialize variable

        self.home()             # ? prints the logo

        self.run()              # ? start taking input

    def init_vars(self):
        """
        Method init_vars() intialize the dictionary that holds

        the user's details like credentials and jobs search, etc.
        """
        self.data = {
            "user_email": "",
            "user_password": "",
            "job_keywords": "",
            "job_location": "",
            "driver_path": "/Python/LinkedIn Automater/driver/chromedriver",
            "headless": True
        }

    def init_commands(self):
        """
        Method init_commands() initialize the commands that LinkedIn

        Automater provides for now we have following commands,

        ! Commands:
            * exit: exit from the program
            * help: prints the commands and their usage 
            * show: shows the entered details
            * devdetails: prints the developer details
            * linkedin: activates the automation process
            * clear: clears the screen
        """
        self.commands = {
            "exit": quit,
            "help": self._help,
            "show": self.show,
            "devdetails": self.dev_details,
            "linkedin": self.handle_linkedin_commands,
            "clear": self.home
        }

    def style(self, style):
        styles = {
            "bright": colorama.Style.BRIGHT,
            "dim": colorama.Style.DIM,
            "normal": colorama.Style.NORMAL,
            "reset": colorama.Style.RESET_ALL
        }

        return styles.get(style, colorama.Style.RESET_ALL)

    def colorFore(self, color):
        colors = {
            "red": colorama.Fore.RED,
            "green": colorama.Fore.GREEN,
            "blue": colorama.Fore.BLUE,
            "reset": colorama.Fore.RESET,
            "lightred": colorama.Fore.LIGHTRED_EX,
            "lightgreen": colorama.Fore.LIGHTGREEN_EX,
            "lightblue": colorama.Fore.LIGHTBLUE_EX
        }

        return colors.get(color, colorama.Fore.RESET)

    def _help(self):
        """
        Method _help() provides a manual to the user, this guide

        is contains every information that a user needs in order to

        start linkedin automation.
        """
        print(f""" {self.style("bright")}""")
        print(
            f""" {self.colorFore("green")}command -> config.user.email""")
        print(
            f""" {self.colorFore("blue")}saves the given user's name as a credential field""")
        print(
            f""" {self.colorFore("blue")}usage -> config.user.email=example@gmail.com{self.colorFore("reset")}""")
        print()
        print(f""" {self.colorFore("green")}command -> config.user.password""")
        print(f""" {self.colorFore("blue")}saves the user's password as a credential field by prompting a password console""")
        print(f""" {self.colorFore("blue")}usage -> config.user.password""")
        print(f""" {self.colorFore("blue")}Passowrd: {self.colorFore("reset")}""")
        print()
        print(f""" {self.colorFore("green")}command -> config.job.keywords""")
        print(f""" {self.colorFore("blue")}saves the job keywords""")
        print(
            f""" {self.colorFore("blue")}usage -> config.job.keywords=Data Science{self.colorFore("reset")}""")
        print()
        print(f""" {self.colorFore("green")}command -> config.job.location""")
        print(f""" {self.colorFore("blue")}saves the job location""")
        print(
            f""" {self.colorFore("blue")}usage -> config.job.location=Sanfransisco{self.colorFore("reset")}""")
        print()
        print(f""" {self.colorFore("green")}Available Locations:\n""")
        print(f""" {self.colorFore("green")}-> India""")
        print(f""" {self.colorFore("green")}-> USA""")
        print(f""" {self.colorFore("green")}-> California""")
        print(f""" {self.colorFore("green")}-> Sanfransisco BA""")
        print(f""" {self.colorFore("green")}-> Sanfransisco CA""")
        print()
        print(
            f""" {self.colorFore("blue")}If you want to select more than one location simple enter like this:""")
        print(f""" {self.colorFore("blue")}config.job.location=India+USA+California+Sanfransisco BA+Sanfransisco CA  (default search location)""")
        print(f""" {self.colorFore("blue")}Or""")
        print(
            f""" {self.colorFore("blue")}config.job.location=[India]+[USA]+[California]+[Sanfransisco BA]+[Sanfransisco CA]""")
        print(f""" {self.colorFore("blue")}'[]' means that these terms may or may not be there in the location key, if you leave that field empty,""")
        print(
            f""" {self.colorFore("blue")}it will by default search in all the location.{self.colorFore("reset")}""")
        print()
        print(f""" {self.colorFore("green")}command -> show""")
        print(
            f""" {self.colorFore("blue")}puts the entered user details on the screen{self.colorFore("reset")}""")
        print()
        print(f""" {self.colorFore("green")}command -> linkedin""")
        print(f""" {self.colorFore("blue")}activates the given linkedin process""")
        print()
        print(f""" {self.colorFore("blue")}usage -> linkedin send""")
        print(
            f""" {self.colorFore("green")}flag [send] starts the process of sending invitation""")
        print(
            f""" {self.colorFore("green")}linkedin [send] [--auto][--guided] [--headless]""")
        print()
        print(
            f""" {self.colorFore("blue")}usage -> linkedin [invitation-manager] [show/withdraw] [--send/--recieve] [--headless]""")
        print(
            f""" {self.colorFore("green")}flag [invitation-manager] handles the invitation manager tab""")
        print()
        print(
            f""" {self.colorFore("green")}flag [show] shows the given type of invitation that you have in your account like send or recieved""")
        print()
        print(
            f""" {self.colorFore("green")}flag [withdraw] withdraws all the pending invitations""")
        print(
            f""" {self.colorFore("blue")}usage -> linkedin [mynetwork] [sendmessage] [--headless]""")
        print(
            f""" {self.colorFore("green")}flag [mynetwork] is the connection tab""")
        print()
        print(
            f""" {self.colorFore("green")}flag [sendmessage] sends a formal greet message to connections{self.colorFore("reset")}""")
        print()
        print(f""" {self.colorFore("green")}command -> devdetails""")
        print(
            f""" {self.colorFore("blue")}prints the developer details like media links, emails and LinkedIn{self.colorFore("reset")}""")

    def show(self):
        """
        Method show() gets executed once the user hit the command

        `show` this basically prints the information that user had

        entered.
        """
        print(f""" {self.colorFore("green") + self.style("bright")}%s""" % (
            self.data["user_email"] if self.data["user_email"] else "use config.user.email to add user email"))
        print(f""" {self.colorFore("green") + self.style("bright")}%s""" % (
            "*"*len(self.data["user_password"]) if self.data["user_password"] else "use config.user.password to add user password"))

        # ! we print the information about job keys once we have any of
        # ! these two field otherwise we don't show it
        if self.data["job_keywords"] or self.data["job_location"]:
            print(f""" {self.colorFore("green") + self.style("bright")}Job Keywords -> %s""" %
                  (self.data["job_keywords"] if self.data["job_keywords"] else None))
            print(f""" {self.colorFore("green") + self.style("bright")}Job Location -> %s""" %
                  (self.data["job_location"] if self.data["job_location"] else None))

        try:
            ch = input(
                f""" {self.colorFore("green") + self.style("bright")}Show password anyway? [y/N]: """) if self.data["user_password"] else "n"
            if ch.lower() == "y":
                print(f""" {self.colorFore("green") + self.style("bright")}%s""" % (
                    self.data["user_email"] if self.data["user_email"] else "use config.user.email to add user email"))
                print(f""" {self.colorFore("green") + self.style("bright")}%s""" % (
                    self.data["user_password"] if self.data["user_password"] else "use config.user.password to add user password"))
        except KeyboardInterrupt:
            print(
                f"""\n {self.colorFore("green") + self.style("bright")}Piece{self.style("reset")}""")
            quit()

    def dev_details(self):
        """
        Method dev_details() gets executed once the user hits the 

        command `devdetails` it basically shows the user's network

        profiles and mail address.
        """
        print(
            f""" {self.colorFore("green") + self.style("bright")}Name -> Ayush Joshi""")
        print(f""" {self.colorFore("green")}Email:""")
        print(f""" {self.colorFore("green")}-> ayush854032@gmail.com (primary)""")
        print(f""" {self.colorFore("green")}-> joshiayush.joshiayush@gmail.com""")
        print(
            f""" {self.colorFore("green")}GitHub -> https://github.com/JoshiAyush""")
        print(
            f""" {self.colorFore("green")}LinkedIn -> https://www.linkedin.com/in/ayush-joshi-3600a01b7/{self.colorFore("reset")}""")

    def _input(self):
        """
        Method _input() is a dedicated input method for our LinkedIn

        `cli` (Command Line Interface), it also handles the Keyboard

        interrupt error.

        ! return:
            * returns the entered value
        """
        try:
            inp = input(
                f"""\n {self.colorFore("green") + self.style("bright")}LinkedIn/> """)
            print(end=f"""{self.style("reset")}""")
            return inp

        except KeyboardInterrupt:
            print(
                f"""\n {self.colorFore("green") + self.style("bright")}Piece{self.style("reset")}""")
            quit()              # ? exit program silently

    def clear(self):
        """
        Method clear() clears the terminal screen

        for windows we use command `cls` and for linux

        based system we use command `clear`
        """
        if os.name == 'nt':
            _ = os.system('cls')
        elif os.name == 'posix':
            _ = os.system('clear')

    def gotoxy(self, x, y):
        """
        Method gotoxy() sets the console cursor position.

        ! Args:
            * x: column number for the cursor
            * y: row number for the cursor
        """
        print("%c[%d;%df" % (0x1B, y, x), end='')

    def terminal_size(self):
        """
        Method terminal_size() returns the size of the terminal when 

        the LinkedIn Automator program executed, this functionality

        is required in order to set the Home Logo according to the

        terminal size.

        ! return:
            * terminal size
        """
        return os.get_terminal_size()

    def get_coords(self):
        """
        Method get_coords() returns the co-ordinates that are

        needed to set the Home Logo nearly to the center according

        to the terminal size.

        ! return:
            * co-ordinates that sets the Logo nearly to the center 
        """
        if self.terminal_size()[0] >= 150:
            return [48, 5]                      # ? return [48, 5] if full size
        elif self.terminal_size()[0] >= 80:
            return [15, 2]                      # ? return [15, 2] if half size
        else:
            # ? else return [15, 2] (predicted)
            return [15, 2]

    def home(self):
        """
        Method home() prints the home logo on the screen which makes 

        the application more professional.
        """
        self.clear()                # ? clears the screen first

        x, y = self.get_coords()    # ? get the co-ordinates
        print(self.colorFore("green") + self.style("bright"))
        self.gotoxy(x, y)           # ? apply co-ordinates
        print(r"\\                      \\  //                  \\  \\             ")
        self.gotoxy(x, y+1)         # ? apply co-ordinates
        print(r"\\        ()            \\ //                   \\  \\             ")
        self.gotoxy(x, y+2)         # ? apply co-ordinates
        print(r"\\        \\  \\\\\\\\  \\//    \\\\\\\\        \\  \\  \\\\\\\\\  ")
        self.gotoxy(x, y+3)         # ? apply co-ordinates
        print(r"\\        \\  \\    \\  \\\\    \\ ===//  \\\\\\\\  \\  \\     \\  ")
        self.gotoxy(x, y+4)         # ? apply co-ordinates
        print(r"\\        \\  \\    \\  \\ \\   \\        \\    \\  \\  \\     \\  ")
        self.gotoxy(x, y+5)         # ? apply co-ordinates
        print(r"\\\\\\\\  \\  \\    \\  \\  \\  \\\\\\\\  \\\\\\\\  \\  \\     \\  ")

        # ? show a tip to automation
        print("\n Type help for more information!", end="\n")
        print(self.colorFore("reset"))

    def Error(self):
        """
        Method Error() gets called when the entered command is

        not recognized.
        """
        if self.command:
            print(
                f""" {self.colorFore("red")}`{self.command}` is not recognized as an internal command{self.colorFore("reset")}""")

    def linkedin_command_usage(self):
        """
        Method linkedin_command_usage() shows how you can use the linkedin

        command in case you missed the flags with the linkedin command or 

        mistakenly applied wrong flags with the linkedin command.
        """
        print(self.style("bright"))
        print(
            f""" {self.colorFore("green")}Missing flags [send] [invitation-manager] [mynetwork]""")
        print(f""" {self.colorFore("blue")}Usage:""")
        print(f""" {self.colorFore("blue")}command -> linkedin""")
        print(f""" {self.colorFore("blue")}activates the given linkedin process""")
        print(f""" {self.colorFore("blue")}usage -> linkedin send""")
        print(
            f""" {self.colorFore("green")}flag [send] starts the process of sending invitation""")
        print(
            f""" {self.colorFore("blue")}usage -> linkedin invitation-manager [show/withdraw] [--send/--recieve]""")
        print(
            f""" {self.colorFore("green")}flag [invitation-manager] handles the invitation manager tab""")
        print(
            f""" {self.colorFore("green")}flag [show] shows the given type of invitation that you have in your account like send or recieved""")
        print(
            f""" {self.colorFore("green")}flag [withdraw] withdraws all the pending invitations""")
        print(
            f""" {self.colorFore("blue")}usage -> linkedin mynetwork sendmessage""")
        print(
            f""" {self.colorFore("green")}flag [mynetwork] is the connection tab""")
        print(
            f""" {self.colorFore("green")}flag [sendmessage] sends a formal greet message to connections""")
        print(self.colorFore("reset"))

    def handle_linkedin_commands(self):
        """
        Method handle_linkedin_commands() calls the main LinkedIn classes

        according to the commands given by the user, it checks the flags

        that are applied with the `linkedin` command and calls the LinkedIn

        classes accordingly.
        """
        if self.command.split(" ")[1] == "send":
            if self.data["user_email"] and self.data["user_password"]:
                LinkedInConnections.LinkedInConnectionsAuto(self.data)
            else:
                print(
                    " Need credentials first use config.user.email/password to add them")
        elif self.command.split(" ")[1] == "invitation-manager":
            pass
        elif self.command.split(" ")[1] == "mynetwork":
            pass
        else:
            print("'%s' is not a linkedin command" %
                  (self.command.split(" ")[1]))

    def handle_configs(self):
        """
        Method handle_configs() basically saves the user's configurations

        that are passed by hitting the command `config.user.email/password`

        or `config.job/keywords/location`.
        """
        if "config.user.email" in self.command:
            self.data["user_email"] = self.command[self.command.find(
                "=")+1:].strip()
        elif "config.user.password" == self.command:
            self.data["user_password"] = getpass.getpass(prompt=" Password: ")
        elif "config.job.keywords" in self.command:
            self.data["job_keywords"] = self.command[self.command.find(
                "=")+1:].strip()
        elif "config.job.location" in self.command:
            self.data["job_location"] = self.command[self.command.find(
                "=")+1:].strip()
        else:
            self.Error()

    def run(self):
        """
        Method run() runs a infinite loop and starts the `cli`

        (Command Line Interface) and it actually starts listening

        to the commands and then it takes action accordingly.
        """
        while True:
            # ? get the command
            self.command = self._input()

            # ? parse the command
            if self.command.split(" ")[0] == "linkedin" and len(self.command.split(" ")) > 1:
                # ? handle the linkedin commands
                self.handle_linkedin_commands()
            elif self.command == "linkedin":
                # ? show the linkedin command usage
                self.linkedin_command_usage()
            elif "=" in self.command or "config.user.password" in self.command:
                # ? handle the config command
                self.handle_configs()
            else:
                # ? get() method of dictionary data type returns
                # ? value of passed argument if it is present
                # ? in dictionary otherwise second argument will
                # ? be assigned as default value of passed argument
                self.commands.get(self.command, self.Error)()


# ! Execute program
if __name__ == "__main__":
    Main()
