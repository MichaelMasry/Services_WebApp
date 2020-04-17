import http.client
from Task import Task
import tkinter as tk
import json

tasks = []
Variables = []
checks = []
IP_ADDRESS = '127.0.0.1'
PORT_NUMBER = 3000
User_ID = 0
User_Name = "Test544"


def add_task_helper(name, description, time):
    ip = '127.0.0.1'
    print("Adding new task URL: " + ip)
    connection = http.client.HTTPConnection(ip, PORT_NUMBER)
    connection.request("POST", '/addnewtask?name=' + name + '&date=' + time + '&description='
                       + description + '&user_id=' + str(User_ID))
    response = connection.getresponse()
    Json = response.read()
    res = json.loads(Json)
    task_id = res["id"]
    print(response.status, response.reason)
    # new_t = Task(task_id,name,description,time)
    # tasks.append(new_t)
    show_One(task_id)


def show_One(task_id):
    ip = '127.0.0.1'
    print("Show all tasks URL: " + ip)
    connection = http.client.HTTPConnection(ip, PORT_NUMBER)
    # Add what you got from Server
    connection.request("GET", "/rvtask?id=" + str(task_id))
    response = connection.getresponse()
    Json = response.read()
    x = json.loads(Json)
    for f in x:
        t = Task(int(task_id), f["name"], f["description"], f["due_date"])
        tasks.append(t)
    print(response.status, response.reason)
    update_gui()


def remove_task(task_id):
    ind = 0
    for x in tasks:
        if task_id == x.id:
            break
        else:
            ind += 1
    tasks.pop(ind)
    ip = '127.0.0.1'
    print("Removing " + str(task_id) + " task URL: " + ip)
    connection = http.client.HTTPConnection(ip, PORT_NUMBER)
    connection.request("DELETE", "/deletetask?id=" + str(task_id))
    response = connection.getresponse()
    print(response.status, response.reason)
    show_All()


def update_gui():
    ShowText.delete('1.0', tk.END)
    for x in tasks:
        print(str(x))
        print("------------------------")
        ShowText.insert('end', str(x) + "\n" + '-------------------' + "\n")


def show_All():
    ip = '127.0.0.1'
    print("Show all tasks URL: " + ip)
    connection = http.client.HTTPConnection(ip, PORT_NUMBER)
    # Add what you got from Server
    connection.request("GET", "/allmytasks?user_id=" + str(User_ID))
    response = connection.getresponse()
    Json = response.read()
    res = json.loads(Json)
    tasks = []
    for x in res:
        t = Task(x["id"], x["name"], x["description"], x["due_date"])
        tasks.append(t)
    print(response.status, response.reason)
    update_gui()


def add_task():
    name = str(nameText.get("1.0", 'end-1c'))
    des = str(desText.get("1.0", 'end-1c'))
    time = str(timeText.get("1.0", 'end-1c'))
    add_task_helper(name, des, time)
    nameText.delete("1.0", tk.END)
    desText.delete("1.0", tk.END)
    timeText.delete("1.0", tk.END)


def callback():
    name = str(nameText.get("1.0", 'end-1c'))
    remove_task(int(name))
    nameText.delete("1.0", tk.END)


Ip = IP_ADDRESS
connection = http.client.HTTPConnection(Ip, PORT_NUMBER)
connection.request("POST", "/signup?username=" + User_Name)
response = connection.getresponse()
Json = response.read()
res = json.loads(Json)
User_ID = res["id"]
print(response.status, response.reason)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
Q_button = tk.Button(frame, text="QUIT", fg="red", command=quit)
Q_button.pack(side=tk.LEFT)
nameText = tk.Text(root, height=1, width=30)
nameText.pack(side=tk.LEFT)
desText = tk.Text(root, height=1, width=30)
desText.pack(side=tk.LEFT)
timeText = tk.Text(root, height=1, width=30)
timeText.pack(side=tk.LEFT)
AddButton = tk.Button(frame, text="ADD", fg="green", command=add_task)
AddButton.pack(side=tk.LEFT)
SHButton = tk.Button(frame, text="SHOW ALL", fg="blue", command=show_All)
SHButton.pack(side=tk.LEFT)
RemoveButton = tk.Button(frame, text="REMOVE", fg="black", command=callback)
RemoveButton.pack(side=tk.LEFT)
ShowText = tk.Text(root, height=10, width=30)
ShowText.pack(side=tk.RIGHT)
root.mainloop()
