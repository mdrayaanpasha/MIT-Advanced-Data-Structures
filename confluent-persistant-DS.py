class Node:
    def __init__(self, tasks, next_node, version):
        self.tasks = tasks  
        self.next_node = next_node  
        self.version = version


class CPDS:
    def __init__(self, initial_tasks=None):
        self.versions = 0
        initial_tasks = initial_tasks if initial_tasks is not None else []
        self.root = Node(initial_tasks, None, self.versions)

    def insert_task_latest(self, task):
        self.root.tasks.append(task)  

    def insert_new_day(self, tasks):
        self.versions += 1
        new_node = Node(tasks, self.root, self.versions)
        self.root = new_node

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.root.tasks):
            self.root.tasks.pop(task_index)
        else:
            print("Task index out of range!")

    def traverse_tasks_latest(self):
        for i, task in enumerate(self.root.tasks):
            print(f"Task {i}: {task}")

    def traverse_version(self, version):
        if version > self.versions or version < 0:
            print("The Version Doesn't Exist!")
            return

        temp = self.root
        while temp and temp.version != version:
            temp = temp.next_node

        if temp:
            for i, task in enumerate(temp.tasks):
                print(f"Task {i}: {task}")

    def merge_days(self, version1, version2):
        if version1 > self.versions or version1 < 0 or version2 > self.versions or version2 < 0:
            print("One of the Versions Doesn't Exist!")
            return

        temp = self.root
        v1_tasks, v2_tasks = None, None
        while temp:
            if temp.version == version1:
                v1_tasks = temp.tasks
            if temp.version == version2:
                v2_tasks = temp.tasks
            temp = temp.next_node

        if v1_tasks is not None and v2_tasks is not None:
            new_version_tasks = list(set(v1_tasks + v2_tasks)) 
            self.versions += 1
            new_version = Node(new_version_tasks, self.root, self.versions)
            self.root = new_version
        else:
            print("One of the Versions Doesn't Exist in the Linked List!")


cpds = CPDS(['Initial task'])
cpds.insert_task_latest('Task 1')
cpds.insert_new_day(['Day 2 Task 1', 'Day 2 Task 2'])
cpds.insert_task_latest('Day 2 Task 3')
cpds.traverse_tasks_latest()
cpds.traverse_version(0)
cpds.merge_days(0, 1)
cpds.traverse_tasks_latest()
