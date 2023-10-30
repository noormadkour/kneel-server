"""Size options module"""
import json
from nss_handler import status
from repository import db_get_all, db_get_single


class SizesView:
    def get(self, handler, url):
        """ Method for handling HTTP request to GET all sizes @ /sizes
        Args:
            handler: http handler to handle the request and return a response
            url: will be indexed into for query_params, and pk
        Returns:
            response from handler        
        """
        sql = "SELECT sz.id, sz.carets, sz.price FROM Sizes sz"

        if url["pk"] != 0:
            sql += " WHERE sz.id = ?"
            query_results = db_get_single(sql, url["pk"])
            serialized_sizes = json.dumps(dict(query_results))
        else:
            query_results = db_get_all(sql, url["pk"])
            sizes = [dict(row) for row in query_results]
            serialized_sizes = json.dumps(sizes)

        return handler.response(serialized_sizes, status.HTTP_200_SUCCESS.value)
    
    def add(self, handler, data):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def update(self, handler, data, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def delete(self, handler, pk):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)