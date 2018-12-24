#!/usr/bin/python3

from pyrob.api import *

def _wall():
    if not wall_is_above():
        move_up()
        fill_cell()
        move_down()

    if not wall_is_beneath():
        move_down()
        fill_cell()
        move_up()
    

@task
def task_8_10():
    while not wall_is_on_the_right():
        _wall()
        move_right()
    _wall()



if __name__ == '__main__':
    run_tasks()