"""
Space Traveller - graphical user interface
"""

import sys

from space_game import game

class SpaceGame:

    @staticmethod
    def get_command() -> str:
        return input("\nenter command: ")

    @staticmethod
    def main():
        while not game.is_solved():
            print()
            print("location: ", game.location.name)
            print("          ", game.location.description)
            print()
            print("cargo   : ", game.cargo)
            print("crew    : ", ", ".join(game.crew))
            print()

            commands = game.get_commands()
            print("Available commands:\n")
            for i, cmd in enumerate(commands, 1):
                print(f"[{i}] {cmd.name}")
            print("[x] Exit")

            key = SpaceGame.get_command()
            print("-" * 60)
            if key == "x":
                return
            else:
                cmd = commands[int(key) - 1]
                message = cmd.execute()

                if message:
                    print(f"**{message}**\n")
