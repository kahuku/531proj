def register_routes(app):
    @app.route('/')
    def index():
        return 'Hello, World!'

    @app.route('/donuts', methods=['GET'])
    def donuts():
        return {
            'donuts': [
                {
                    'id': 1,
                    'name': 'Glazed',
                    'price': 1.50,
                    'imgSrc': '',
                },
                {
                    'id': 2,
                    'name': 'Chocolate',
                    'price': 2.00,
                    'imgSrc': '',
                },
                {
                    'id': 3,
                    'name': 'Boston Cream',
                    'price': 2.50,
                    'imgSrc': '',
                }
            ]
        }
