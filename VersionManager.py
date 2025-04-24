import copy

class VersionManager:
    def __init__(self):
        self.versions = []
        self.current_index = -1

    def save_version(self, world):
        # Only keep versions up to current if user undid something
        self.versions = self.versions[:self.current_index + 1]
        self.versions.append(copy.deepcopy(world))
        self.current_index += 1

    def undo(self):
        if self.current_index > 0:
            self.current_index -= 1
            return copy.deepcopy(self.versions[self.current_index])
        return None

    def redo(self):
        if self.current_index < len(self.versions) - 1:
            self.current_index += 1
            return copy.deepcopy(self.versions[self.current_index])
        return None
