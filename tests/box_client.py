from tests.client import ApiClient


class BoxClient(ApiClient):
    def __init__(self, url):
        self.api_client = ApiClient(url)

    def get_box(self, box_id):
        return self.api_client.get(f'/api/box/{box_id}')

    def create_box(self, box_data):
        data = {'name': box_data['name'], 'make_date': box_data['make_date']}
        return self.api_client.post('/api/box', data)

    def delete_box(self, box_id):
        return self.api_client.delete(f'/api/box/{box_id}')
