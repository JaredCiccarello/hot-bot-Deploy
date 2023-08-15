import os
# import sys
from rich.console import Console
from rich.prompt import Prompt
import importlib
from rich.progress import Progress
import time
import threading
from modules.gpt_controller import perform_trades

console = Console()


def start_trading(api):
    symbol = "BTC/USD"
    investment_amount = 1000  # Starting capital

    roi_threshold = Prompt.ask("Ender the ROI threshold (%) for trading:", default="5")
    stop_loss_threshold = Prompt.ask("Enter the stop-loss threshold (%) for trading:", default="-2")

    roi_threshold = float(roi_threshold)
    stop_loss_threshold = float(stop_loss_threshold)

    trading_thread = threading.Thread(
        target=perform_trades, args=(api, symbol, investment_amount, roi_threshold, stop_loss_threshold))
    trading_thread.start()
    console.print("Trading bot started. Press Enter to go back to the main menu...")
    input()


def menu():
    while True:
        console.clear()
        os.system("clear")
        console.print(
            "Options are [bold green]ACTIVE[/bold green]"
            "\nOptions that are work in [bold medium_violet_red]PROGRESS[/bold medium_violet_red]"
            "\n1. [bold green]Help[/bold green]\n2. [bold green]AI Analysis[/bold green]\n3. [bold medium_violet_red]Start Trading: [/bold medium_violet_red](In production) \n4. [bold green]About us[/bold green] \n5. [bold red]Exit[/bold red]",
            soft_wrap=False,
        )
        choice = Prompt.ask(
            "\nChoose a task: (Enter the number)",
            choices=["1", "2", "3", "4", "5"],
            default="5",
        )

        if choice == "1":
            help_menu()

        elif choice == "2":
            choice2()

        elif choice == "3":
            start_trading(api) # this will start the trading bot
            pass

        elif choice == "4":
            about_us()

        elif choice == "5":
            console.print("Exiting...")
            break

        else:
            console.print("Invalid choice. Please try again.")


def help_menu():
    console.clear()
    console.print("This will offer an overview of the program")
    console.print("Press Enter to go back to the main menu...")
    crypto_bot = Prompt.ask(
        "Choose [bold purple]info, commands[/bold purple] (Enter the option number)",
        choices=["info", "commands"],
        default="1",
    )

    if crypto_bot == "info":
        # Provide information about the crypto bot
        print("Crypto bot information:")
        print("- This bot helps you with cryptocurrency-related tasks.")
        print(
            "- It can provide information about various cryptocurrencies, market trends, and more."
        )
        print(
            "- You can also use it to execute specific commands for trading or managing your cryptocurrencies."
        )

    elif crypto_bot == "commands":
        # Execute commands for the crypto bot
        console.print("Generating response...")
        print("If you need help ")
        console.print("press enter to exit")
        # Add your code here to handle commands
    else:
        print("Invalid option selected.")
    console.print('\nPress "enter" to [red]exit[/red]')
    input()


# def about_us():
#     console.print('\nAndrew Carroll: Andrew Carroll is a man')
#     \
#     console.print('\nSlava Makeev: Slave Makeeve was born...')

#     console.print('\nJared Ciccarello: Woke up drunk', style='bold')

#     console.print('\nPress "enter" to [red]exit[/red]')
#     input()


def choice2():
    day_choice = Prompt.ask(
        "\nChoose a dataset of [bold purple]30, 60, or 90 days[/bold purple]. (Enter the number)",
        choices=["30", "60", "90"],
        default="30",
    )
    option_choice = Prompt.ask(
        "\nChoose a strategy Conservative (C), Risky (R), Beginner (B)",
        choices=["Conservative", "Risky", "Beginner", "C", "R", "B"],
        default="4",
    )

    if option_choice.lower() == "Conservative" or option_choice.lower() == "c":
        option_choice_validated = "conservative"

    elif option_choice.lower() == "Risky".lower() or option_choice.lower() == "r":
        option_choice_validated = "risky"

    elif option_choice.lower() == "Beginner".lower() or option_choice.lower() == "b":
        option_choice_validated = "beginner"
    else:
        exit

    with Progress(console=console, transient=True) as progress:
        task = progress.add_task("[cyan]Loading...", total=10)
        for _ in range(10):
            progress.update(task, advance=1)
            time.sleep(0.2)  # Add a delay to simulate processing
        progress.stop()
    console.clear()

    user_input(day_choice, option_choice_validated)


def user_input(days, option):
    if days == "30" or days == "60" or days == "90":
        module_name = f"modules.gpt_controller"
        module = importlib.import_module(module_name)
        get_option = getattr(module, "get_option")
        get_option(days, option)
        end_programm()
    else:
        exit


def end_programm():
    console.print('\nPress "enter" to [red]exit[/red]')
    input()
    exit


def about_us():
    while True:
        console.clear()
        console.print("[bold cyan]The HotBot Team[/bold cyan]")
        console.print("Select a team member to learn more:")
        console.print("1. [bold yellow]Andrew Carroll[/bold yellow]")
        console.print("2. [bold yellow]Slava Makeev[/bold yellow]")
        console.print("3. [bold yellow]Jared Cicarrello[/bold yellow]")
        console.print("4. [bold red]Back to main menu[/bold red]")

        choice = Prompt.ask(
            "Choose a team member (Enter the number)",
            choices=["1", "2", "3", "4"],
            default="4",
        )

        if choice == "1":
            show_bio(
                "Andrew Carroll",
                "Storytelling, Magic, Software Dev",
                '''
                __
               / _\ #
               \c /  #
               / \___ #
               \`----`#==>  
               |  \  #
    ,%.-"""---'`--'\#_
   %%/             |__`|
  .%'\     |   \   /  //
  ,%' >   .'----\ |  
     < <<`       ||
      `\\\       ||
        )\\      )\\
\n^^^^^"""^^^^^^""^^^^^^^^^^
                     ''',
                "https://github.com/iamandrewcarroll",
            )

        elif choice == "2":
            show_bio(
                "Slava Makeev",
                "Outdoors, Adventure, Software Dev",
                """
     ; 
     ;;
     ;';.
     ;  ;;
     ;   ;;
     ;    ;;
     ;    ;;
     ;   ;'
     ;  ' 
,;;;,; 
;;;;;;
`;;;;'     """,
                "https://github.com/S-Makeev",
            )

        elif choice == "3":
            show_bio(
                "Jared Cicarrello",
                "Software Dev, Marine, Civil Service",
                """
                          \ : /
                        '-: __ :-'
                        -:  _ :--
                          ,==.
                          \\\//
                        .-~~-.
                      ,",-""-.".
                      | |      | |
                      | |      | |
                      ". `,",-" ,'
                        `| |_,-' 
                      -' |   | '-
            ,sSSSSs,    (   )
            sS';:'`Ss   )  (  
           ; ~ <  ~  /  (  )
            S, ''  SJ (  ;/
            sL_~~_;(S_)  _7
/\        'J)_.-' />'-' `Z
\ \         /-;-A'-'|'--'-j\\
 \ \        )  |/   :    /  \\
  \ \       | | |    '._.'|  L
   \ \      | | |       | \  J
    \ \    _/ | |       |  ',|
     \ L.,' | | |       |   |/
    _;-r-<_.| \=\    __.;  _/
      {_}"  L-'  '--'   / /|
            |   ,      |  \|
            |   |      |   ")
            L   ;|     |   /|
           /|    ;     |  / |
          | |    ;     |  ) |
         |  |    ;|    | /  |
         | ;|    ||    | |  |
         L-'|____||    )/   |
             % %/ '-,- /    /
             |% |   \%/_    |
          ___%  (   )% |'-; |
        C;.---..'   >%,(   "'
                   /%% /
                  Cccc' """,
                "https://github.com/JaredCiccarello",
            )

        elif choice == "4":
            break

        else:
            console.print("Invalid choice. Please try again.")


def show_bio(name, interests, avatar, github_link):
    console.clear()
    console.print(f"[bold yellow]{name}[/bold yellow]")
    console.print(f"Heart: {interests}")
    console.print("Avatar:")
    console.print(avatar)
    console.print(f"GitHub: [link={github_link}]{github_link}[/link]")
    console.print("Press Enter to go back to the team members...")
    input()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        console.print("\nCtrl+C detected. Exiting...")
