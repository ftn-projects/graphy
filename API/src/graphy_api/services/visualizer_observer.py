from enum import Enum


class EventType(Enum):
    NODE_SELECTED = "node_selected"
    ZOOM_CHANGED = "zoom_changed"


class VisualizerObserver:
    _observers = {}

    def attach(self, event_type: EventType, observer):
        if event_type not in self._observers:
            self._observers[event_type] = []
        self._observers[event_type].append(observer)

    def detach(self, event_type: EventType, observer):
        if event_type in self._observers:
            if observer in self._observers[event_type]:
                self._observers[event_type].remove(observer)

    def notify(self, event_type: EventType, data=None):
        if event_type in self._observers:
            for observer in self._observers[event_type]:
                observer(event_type, data)
