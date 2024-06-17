class ErrorRepository:
    def __init__(self):
        self.error_codes = {}

    def translate(self, code):
        if code in self.error_codes:
            return self.error_codes[code]
        else:
            return 'Unknown error'
    def add_error(self, code, message):
        self.error_codes[code] = message
         