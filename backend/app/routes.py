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
                    'imgSrc': 'https://531proj.kahuku.dev/donuts/glazed.png',
                },
                {
                    'id': 2,
                    'name': 'Chocolate',
                    'price': 2.00,
                    'imgSrc': 'https://531proj.kahuku.dev/donuts/chocolate.png',
                },
                {
                    'id': 3,
                    'name': 'Boston Cream',
                    'price': 2.50,
                    'imgSrc': 'https://531proj.kahuku.dev/donuts/boston-cream.png',
                },
                {
                    'id': 4,
                    'name': 'Maple Bar',
                    'price': 2.50,
                    'imgSrc': 'https://531proj.kahuku.dev/donuts/maple-bar.png',
                },
                {
                    'id': 5,
                    'name': 'Bear Claw',
                    'price': 3.00,
                    'imgSrc': 'https://531proj.kahuku.dev/donuts/bear-claw.png',
                }
            ]
        }
