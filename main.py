from ursina import *


class Utilities:
    @staticmethod
    def create_text(text_str, pos):
        if isinstance(pos, tuple):
            return Text(
                text=text_str,
                position=pos,
                font='Assets/font.ttf'
            )
        elif isinstance(pos, int):
            return Text(
                text=text_str,
                position=(-0.35, 0.25+pos, -0.1),
                font='Assets/font.ttf'
            )
        else:
            return Text(text_str)

    @staticmethod
    def create_button(text_str, pos):
        return Button(
            scale=(0.5, 0.1),
            text=Text(
                text=text_str,
                position=(-0.05, pos-0.98, -0.1),
                font='Assets/font.ttf',
                scale=2,
            )
        )


def main_menu():
    title = Text(
        text='Untitled Tech Game',
        position=(-0.35, 0.25, -0.1),
        font='Assets/font.ttf',
        scale=3
    )

    play_button = Button(
        scale=(0.5, 0.1),
        text=Text(
            text='Play',
            position=(-0.05, 0.02, -0.1),
            font='Assets/font.ttf',
            scale=2,
        )
    )

    multiplayer_button = Button(
        position=(0, -0.1),
        scale=(0.5, 0.1),
        text=Text(
            text='Multiplayer',
            position=(-0.12, -0.08, -0.1),
            font='Assets/font.ttf',
            scale=2,
        )
    )

    events_button = Button(
        position=(0, -0.2),
        scale=(0.5, 0.1),
        text=Text(
            text='Events',
            position=(-0.08, -0.18, -0.1),
            font='Assets/font.ttf',
            scale=2,
        )
    )


def main():
    app = Ursina()

    main_menu()

    EditorCamera()
    app.run()


if __name__ == '__main__':
    main()
