import curses
import math
from curses.textpad import Textbox, rectangle


def get_login(stdscr):
    stdscr.clear()

    curses.echo()
    stdscr.addstr(0, 0, "user: ")
    username = stdscr.getstr().decode("utf-8")

    stdscr.refresh()
    stdscr.clear()

    stdscr.addstr(0, 0, f"user: {username} ")
    stdscr.addstr(2, 0, "password:")

    curses.noecho()
    stdscr.refresh()
    password = stdscr.getstr().decode("utf-8")

    stdscr.clear()
    return (username, password)


def draw_options(stdscr, opts):
    spacing = 20
    c = curses.getsyx()
    for pos, opt in enumerate(opts):
        # stdscr.addstr(c[0], c[1] + spacing * pos, f"| f{pos + 1} : {opt} |")
        stdscr.addstr(c[0] + pos, c[1], f"f{pos + 1} : {opt}")

    stdscr.refresh()


def draw_select_menu(stdscr, opts):
    curses.setsyx(0, 0)
    draw_options(stdscr, opts)


def draw_edit_view(stdscr):
    # todo: show function and allow deletes from here
    # should implement del
    pass


def draw_add_entry(stdscr, name):
    stdscr.clear()
    stdscr.addstr(0, 0, "Add: (hit Ctrl-G to send)")

    editwin = curses.newwin(5, 30, 2, 1)
    rectangle(stdscr, 1, 0, 1 + 5 + 1, 1 + 30 + 1)
    stdscr.refresh()
    box = Textbox(editwin)

    box.edit()

    message = box.gather()
    # dest.send() or something


def draw_opt_view(stdscr, option):
    # stdscr.clear()

    while True:
        max = stdscr.getmaxyx()
        overwin = curses.newwin(
            5, 40, math.ceil(max[0] / 2) - 2, math.ceil(max[1] / 2) - 20
        )
        overwin.border()

        overwin.addstr(2, 2, "| a: add | e : edit | b : back |")
        overwin.refresh()
        stdscr.refresh()

        selection = stdscr.getkey()

        if selection == "a":
            draw_add_entry(stdscr, option)
        elif selection == "e":
            draw_edit_view(stdscr)
        elif selection == "b":
            break
    stdscr.clear()


def update(stdscr):
    tables = ("bus", "schedule", "depots", "routes", "drivers")

    curses.curs_set(0)
    stdscr.clear()
    stdscr.keypad(True)

    login = get_login(stdscr)

    while True:
        draw_select_menu(stdscr, tables)
        c = stdscr.get_wch()

        if c == "q":
            break
        elif c == curses.KEY_F1:
            draw_opt_view(stdscr, tables[0])
        elif c == curses.KEY_F2:
            draw_opt_view(stdscr, tables[1])
        elif c == curses.KEY_F3:
            draw_opt_view(stdscr, tables[2])
        elif c == curses.KEY_F4:
            draw_opt_view(stdscr, tables[3])
        elif c == curses.KEY_F5:
            draw_opt_view(stdscr, tables[4])


def main():
    curses.wrapper(update)
