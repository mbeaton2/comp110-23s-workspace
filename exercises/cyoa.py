"""Create Your Own Adventure"""
__author__: "730480912"

def main() -> None: 
    points: int = 0

def greet() -> None:
    print("Welcome to What are the Odds, the game where I will ask you what the odds are of you performing a task should you and I guess the same number! First let me ask you this. ")
    player = input("What is your name? ")
    pick_your_path(player)

def pick_your_path(player: str ) -> None:
    pick_your_path = input("Shall we begin? Answer with Yes, No, or Maybe ")
    if pick_your_path == True: 
        print(f"Let's go {player}! Since you said yes, your task will be more challenging. " )
        path1()

    else: 
       if pick_your_path == False:
        print("Bummer. Did I scare you? I'm sorry. Try again later... ")

def path1() -> None:
   points: int = 0
   response = input("What are the odds you get up and run laps around the lecture hall? 1-3. 1, 2, 3.. ")
   if response / 2 == 0:
      print("Gotcha! Grab your running sneakers! I'll still give you 10 points for trying. ")
      int += 10
      print(points)
   else: 
        if response / 2 != 0: 
           print("Dang...you got me. Here's 100 points! ")
        int += 100
        print(points)
if __name__ == "__main__":
  main()