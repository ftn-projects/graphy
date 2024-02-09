import time


class Platform(object):
    def __init__(self):
        self.__workspaces: Dict[int, Workspace] = {}

    def addWorkspace(self, workspace: Workspace):
        self.__workspaces[workspace.id] = workspace

    def getWorkspace(self, id: int) -> Workspace:
        return self.__workspaces.get(id)