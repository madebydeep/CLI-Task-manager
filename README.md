# CLI-Task-manager
A CLI-based task manager with the ability to _add_, _update_, mark _status changes_, and even _delete_ your tasks, for an __easy and productive task management__, made with the guidance from [roadmap.sh](https://roadmap.sh/projects/task-tracker).

## 👀 Features include:
  ↳ __INSERTION__: Adding tasks using the argument `-add`. <br>
  &emsp; Example: python3 main.py -add `first_task`<br><br>
  ↳ __Updating Progress__: Updating&ensp;the&ensp;progress&ensp;made&ensp;to&ensp;a&ensp;task,&ensp;using&ensp;`-mip`&ensp;(mark In-Progress)&ensp;or&ensp;`md`&ensp;(mark Done)<br>
  &emsp; Example: python3&ensp;main.py -mip `task_id`<br>
  &emsp; Example: python3&ensp;main.py -md `task_id`<br><br>
  ↳ __Listing Tasks__: Listing&emsp;the&emsp;tasks&emsp;according&emsp;to&emsp;their&emsp;status.<br>
  &emsp; Example: python3&ensp;main.py -list `i` <sub>(Lists all the __IN-PROGRESS__ tasks)</sub><br>
  &emsp; Example: python3&ensp;main.py -list `d` <sub>(Lists all the tasks marked __DONE__)</sub><br>
  &emsp; Example: python3&ensp;main.py -list `t` <sub>(Lists all the tasks marked __TO-DO__)</sub><br>
  &emsp; Example: python3&ensp;main.py -list `a` <sub>(Lists __all__ the available tasks)</sub><br><br>
  ↳ __Deleting Tasks__: Delets&emsp;the&emsp;specified&emsp;task.<br>
  &emsp; Example: python3&emsp;main.py -delete `task_id`<br><br>

## 👀 Libraries Used:
↳ `argparse`: used in Python to pass arguments through the terminal.<br>
↳ `datetime`: used to give tasks date and time information.<br>
↳ `sys`: used to manage the task file.<br>
↳ `json`: used for manipulating the `data.json` file.<br><br>

## 👀 Simple installation guide:
↳&emsp;Download the `main.py` file.<br>
↳&emsp;Simply put it in the `IDE` of your choice, and use the above [`features`](##👀-Features-include) in the terminal.<br><br>

## 👀 Time taken:
↳&emsp;A day (for programming) and a half (for documentation).<br><br>
