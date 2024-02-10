// Define EventType as an object
const EventType = {
    NODE_SELECTED: 'node_selected',
    ZOOM_CHANGED: 'zoom_changed',
    HTML_CHANGED: 'html_changed'
};

// Define the VisualizerObserver class
class VisualizerObserver {
    constructor() {
        this._observers = {};
    }

    // Method to attach an observer to an event type
    attach(eventType, observer) {
        if (!(eventType in this._observers)) {
            this._observers[eventType] = [];
        }
        this._observers[eventType].push(observer);
    }

    // Method to detach an observer from an event type
    detach(eventType, observer) {
        if (eventType in this._observers) {
            const index = this._observers[eventType].indexOf(observer);
            if (index !== -1) {
                this._observers[eventType].splice(index, 1);
            }
        }
    }

    // Method to notify observers of an event
    notify(eventType, data = null, data2 = null) {
        if (eventType in this._observers) {
            this._observers[eventType].forEach(observer => observer(eventType, data, data2));
        }
    }
}


let visualizer_observer = new VisualizerObserver();