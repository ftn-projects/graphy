class JsonError(ValueError):
    def __init__(self, json: any):
        super().__init__('invalid json: ' + str(json))
