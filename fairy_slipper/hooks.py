from pecan.hooks import PecanHook


class CORSHook(PecanHook):
    def after(self, state):
        state.response.headers['Access-Control-Allow-Origin'] = '*'
        state.response.headers['Access-Control-Allow-Methods'] = 'GET'
        state.response.headers['Access-Control-Allow-Headers'] = \
            'origin, authorization, accept'
