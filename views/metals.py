"""Metal options module"""
import json
from nss_handler import status
from repository import db_get_all, db_get_single


class MetalsView:
    def get(self, handler, url):
        """Method for handling HTTP request to GET all metals @ /metals
        Args:
            handler: http handler to handle the request and return a response
            url: will be indexed into for query_params, and pk
        Returns:
            response from handler
        """
        sql = "SELECT m.id, m.metal, m.price FROM Metals m"

        if url["pk"] != 0:
            sql += " WHERE m.id = ?"
            query_results = db_get_single(sql, url["pk"])
            serialized_metals = json.dumps(dict(query_results))
        else:
            query_results = db_get_all(sql, url["pk"])
            metals = [dict(row) for row in query_results]
            serialized_metals = json.dumps(metals)

        return handler.response(serialized_metals, status.HTTP_200_SUCCESS.value)

    def add(self, handler, data):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def update(self, handler, data, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def delete(self, handler, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)