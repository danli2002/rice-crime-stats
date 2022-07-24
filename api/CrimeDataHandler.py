from flask_restful import Api, Resource, reqparse
from api.data import CrimeDataParser
import json

CRIME_DATA_URL = 'https://rupdadmin.rice.edu/crimelog/unskinned/'

class CrimeDataHandler(Resource):
    def get(self):
        cdp = CrimeDataParser()
        crime_data_html = cdp.get_crime_data_html(CRIME_DATA_URL)
        crime_df = cdp.create_df(crime_data_html)
        u_locations = json.dumps(cdp.find_unique_locations(crime_df).tolist())
        return {
            'status': 'SUCCESS',
            'message': u_locations
        }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()
        print(args)

        request_type = args['type']
        request_json = args['message']

        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = f'successful message: {ret_msg}'
        else:
            message = 'failed msg'

        final_ret = {"status": "Success", "message": message}
        return final_ret